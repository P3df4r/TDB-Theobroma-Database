#!/usr/bin/env python3
#coding: utf-8
import os
import subprocess
import BlastClass
import ArvoreFilo
from sys import platform
from flask import Flask, render_template, request, send_file, flash, redirect, url_for, jsonify
import flask_login
from flask_login import LoginManager, UserMixin
from werkzeug.utils import secure_filename
import pandas as pd
import sys
import time
import json
from pymongo import MongoClient
from Bio import Entrez


HOST_ADDR="localhost"
DATABASES={ #cada lista corresponde a um blast e suas opções
    1 : ["Criollo", "Matina", "C1074", "C174", "C1074P", "C174P"],
    2 : ["Criollo", "Matina", "C1074", "C174", "C1074P", "C174P"],
    3 : ["Criollo", "Matina", "C1074", "C174", "C1074P", "C174P"],
    4 : ["Criollo", "Matina", "C1074", "C174", "C1074P", "C174P"],
}

QUERY_DEFAULT="userSeq.fasta"
UPLOADS_FOLDER="uploads"
DOWNLOADS_FOLDER="downloads"
TEXT_NAME="output.txt"
TREE_NAME="tree.pdf"
ARVORE_INST = ArvoreFilo.Arvore()
BLAST_INST = BlastClass.Blast(
    os.path.join(
        DOWNLOADS_FOLDER, 
        TEXT_NAME
    )
)
SEQUENCE_BAR_STATUS=""

login_manager = LoginManager()

app = Flask(__name__)
app.secret_key = b'BDk^iUe99W*0r0S!eM9!8A'
app.config["UPLOAD_FOLDER"] = UPLOADS_FOLDER

login_manager.init_app(app)

users = {'admin':{'pw':'cacauadmin'}}


class User(UserMixin):
  pass

@login_manager.user_loader
def user_loader(username):
  if username not in users:
    return

  user = User()
  user.id = username
  return user

@login_manager.request_loader
def request_loader(request):
  username = request.form.get('username')
  if username not in users:
    return

  user = User()
  user.id = username

  user.is_authenticated = request.form['pw'] == users[username]['pw']

  return user

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    username = request.form.get('username')
    if request.form.get('pw') == users[username]['pw']:
      user = User()
      user.id = username
      flask_login.login_user(user)
      return redirect(url_for('index'))
  return render_template('loginpage.html')


@app.route("/index")
@flask_login.login_required
def index():
    count = estatistic()
    sequence_status = "is-hidden"
    if platform == "linux":
        seqspid = os.system("pidof sequenceserver")
        if seqspid != 256:
            sequence_status = ""
    SEQUENCE_BAR_STATUS = sequence_status
    return render_template("index.html", counts=count, home_bar_classes="is-active", sequence_bar_classes=sequence_status, blast_classes="is-hidden", search_classes="is-hidden", search_detail_classes="is-hidden", paper_classes="is-active", est_classes="is-active")


@app.route("/index", methods=['GET', 'POST'])
def runBlast():
    filename = ""
    genoma1 = request.form.get("genoma1")
    genoma2 = request.form.get("genoma2")
    #genomaU = request.form.get("tree-nucleotideo")
    if genoma1 or genoma2:
        listaFastas = []
        if genoma1:
            listaFastas.append("a/{}.fasta".format(genoma1))
        if genoma2:
            listaFastas.append("a/{}.fasta".format(genoma2))
        if "file" in request.files:
            arquivo = request.files["file"]
            if arquivo.filename != "":
                filename = secure_filename(arquivo.filename)
                arquivo.save(os.path.join("./static/blast_db", filename))
                listaFastas.append("static/blast_db/{}".format(filename))
        if len(genomaU) > 0:
            filename = "userTree.fasta"
            with open(os.path.join("genomas/", filename), "w") as arquivo:
                arquivo.write(genomaU)
                listaFastas.append("genomas/{}".format(filename))
        ARVORE_INST.run(listaFastas)
        return redirect(url_for("downloadtree"))

    upFolder = app.config["UPLOAD_FOLDER"]
    mBlast = request.form.get("modoBlast")
    uInput = request.form.get("nucleotideo")
    genoma = request.form.get("escolhaGenoma")
    bValor = int(mBlast)
    dbValor = int(genoma)

    if "file" in request.files:
        arquivo = request.files["file"]
        if arquivo.filename != "":
            filename = secure_filename(arquivo.filename)
            arquivo.save(os.path.join(upFolder, filename))
    if len(uInput) > 0:
        filename = QUERY_DEFAULT
        with open(os.path.join(upFolder, filename), "w") as arquivo:
            arquivo.write(uInput)

    if filename == "":
        flash("Não foi fornecido arquivo nem sequência.")
        return render_template("index.html", blast_bar_classes="is-active", sequence_bar_classes=SEQUENCE_BAR_STATUS,
                               home_classes="is-hidden")

    query = os.path.join(upFolder, filename)
    BLAST_INST.run(DATABASES[bValor][dbValor], bValor, query)
    return redirect(url_for("downloadxml"))

@app.route("/download/blast")
def downloadxml():
    return send_file(
        os.path.join(DOWNLOADS_FOLDER, TEXT_NAME), 
        as_attachment=True, 
        #cache_timeout=0
        )

@app.route('/jbrowse')
def jbrowse():
    return render_template("jbrowse.html", home_bar_classes="is-active")

@app.route('/search_engine', methods=['POST'])
def search_engine():
    busca = request.form.get("search_input")
    client = MongoClient("mongodb://172.17.0.2:27017")
    db = client.test
    # tmp = []
    # tmp = db.Tabela1.find( { "$or": [  { Software: busca }, { ID: busca}  ], {'_id': 0}  } )
    # cursor = db.Tabela1.find({"Software":"EVM"})
    # tmp = db.Tabela1.find({"Software": busca}, {'_id': 0})
    # tmp.batch_size(100000)
    # result_tmp = list(tmp)
    result = []
    i = 0
    print(busca)
    #for x in db.Tabela1.find( {"$or": [
    #        {"Chromossome": {"$regex": busca, "$options": "i"}},
    #        {"Program": {"$regex": busca, "$options": "i"}},
    #        {"Function": {"$regex": busca, "$options": "i"}},
    #        {"ID": {"$regex": busca, "$options": "i"}}
    #        ]}, {'_id': 0}) :
    #for x in db.Tabela1.find({ 'Cromossome\tSoftware\tFunction\tStart\tStop\tIG\tLecture\t3_prime_partial=\t5_prime_partial=\tID=\t Name=\tParent=\tanticodon=\tcacao=\tcazy=\tclassification=\tcog=\tdescription=\tdomains=\tec_number=\tfpkm=\tgene_ontology=\tidentity=\tltr_identity=\tmethod=\tmotif=\tnlr=\tnote=\tpfam=\tplantTFDB=\tplantiSMASH=\tprgDB=\tproduct=\tpseudogene=\tsequence_ontology=\ttIR=\ttSD=\ttair10=\ttopology=\ttpm=\ttsd=': { "$regex": busca, "$options": "i" } }, {'_id':0} ) :
    for x in db.Tabela1.find( {"$or": [
            {"Cromossome": {"$regex": busca, "$options": "i"}},
            {"Program": {"$regex": busca, "$options": "i"}},
            {"Function": {"$regex": busca, "$options": "i"}},
            {"Start": {"$regex": busca, "$options": "i"}},
            {"Stop": {"$regex": busca, "$options": "i"}},
            {"IG": {"$regex": busca, "$options": "i"}},
            {"Lecture": {"$regex": busca, "$options": "i"}},
            {"3_prime_partial=": {"$regex": busca, "$options": "i"}},
            {"5_prime_partial=": {"$regex": busca, "$options": "i"}},
            {"ID=": {"$regex": busca, "$options": "i"}},
            {"Name=": {"$regex": busca, "$options": "i"}},
            {"Parent=": {"$regex": busca, "$options": "i"}},
            {"anticodon=": {"$regex": busca, "$options": "i"}},
            {"cacao=": {"$regex": busca, "$options": "i"}},
            {"cazy=": {"$regex": busca, "$options": "i"}},
            {"classification=": {"$regex": busca, "$options": "i"}},
            {"cog=": {"$regex": busca, "$options": "i"}},
            {"description=": {"$regex": busca, "$options": "i"}},
            {"domains=": {"$regex": busca, "$options": "i"}},
            {"ec_number=": {"$regex": busca, "$options": "i"}},
            {"fpkm=": {"$regex": busca, "$options": "i"}},
            {"gene_ontology=": {"$regex": busca, "$options": "i"}},
            {"identity=": {"$regex": busca, "$options": "i"}},
            {"ltr_identity=": {"$regex": busca, "$options": "i"}},
            {"method=": {"$regex": busca, "$options": "i"}},
            {"motif=": {"$regex": busca, "$options": "i"}},
            {"nlr=": {"$regex": busca, "$options": "i"}},
            {"note=": {"$regex": busca, "$options": "i"}},
            {"pfam=": {"$regex": busca, "$options": "i"}},
            {"planTFDB=": {"$regex": busca, "$options": "i"}},
            {"platiSMASH=": {"$regex": busca, "$options": "i"}},
            {"prgDB=": {"$regex": busca, "$options": "i"}},
            {"product=": {"$regex": busca, "$options": "i"}},
            {"pseudogene=": {"$regex": busca, "$options": "i"}},
            {"sequence_ontology=": {"$regex": busca, "$options": "i"}},
            {"tIR=": {"$regex": busca, "$options": "i"}},
            {"tSD=": {"$regex": busca, "$options": "i"}},
            {"tair10=": {"$regex": busca, "$options": "i"}},
            {"topology=": {"$regex": busca, "$options": "i"}},
            {"tpm=": {"$regex": busca, "$options": "i"}},
            {"tsd=": {"$regex": busca, "$options": "i"}}
            ]}, {'_id': 0}):

        i = i + 1
        tmp = list(dict(x).values())
        result.append(tmp)
        print(result)
        if i == 1000:
            break
    # for elemento in result_tmp:
    #     i = i + 1
    #     result.append(list(dict(elemento).values()))
    #     if i == 50000:
    #         break
    # print(client.list_database_names())
    client.close()
    #print(result)
    return render_template("index.html", home_classes="is-hidden", home_bar_classes="is-hidden", sequence_bar_classes="is-hidden", search_classes="is-active", blast_bar_classes="is-hidden", blast_classes="is-hidden", search_detail_classes="is-hidden", results=result)

def estatistic():
#    terms = ["chr", "gene", "exon", "intron", "transposon", "mRNA", "rRNA", "tRNA", "CDS"]
#    terms =["chr"]
#    terms2 = {}
    count = 0
#    temp2 = 0
#    arq = open("./static/annotation/DB/DBFinal_VERSION_ABR.csv", "r")
#    teste = arq.read()
#    for i in range(len(terms)):
#        temp2 = str(teste.count(terms[i]))
#        count.append(temp2)
#        terms2.update({terms[i]:temp2})
    #count = str(count)
#    print(count)
    #print(terms2)
    return count

@app.after_request
def after_request(response):
    response.headers.add('Accept-Ranges', 'bytes')
    response.headers.pop('Content-Encoding', None)
    return response

@app.route('/logout')
def logout():
  flask_login.logout_user()
  return 'Logged out'

@app.route('/last_paper')
#Search last papers with title "Theobroma", using Entrez of Biopython and "import os"
def search ():
    doi = []
    parameter_number_papers = int(10)
    Entrez.email = "pedfar321@gmail.com" #The email from Pedro Augusto, send a message whenever you want
    procura = Entrez.esearch(db="pubmed", retmax=parameter_number_papers, term="Theobroma[title]", mindate="2018")
    save_temp = Entrez.read(procura)
    papers = ""
    #Treatament of Entrez collection
    save = str(save_temp.get("IdList"))
    temp = save.replace("[", '')
    save = temp
    temp = save.replace("]", "")
    save = temp
    temp = save.replace("'", "")
    save = temp
    temp = save.replace(",", "")
    save = temp
    doi = save.split(" ")
    #Add all information of Entrez collection
    for i in range(len(doi)):
        temp = ""
        nome = Entrez.esummary(db="pubmed", id=doi[i])
        record = Entrez.read(nome)
        temp += record[0]["Title"] + " DOI: " + doi[i] + " Publish Date: " + record[0]["PubDate"]+"\n"
        papers += temp
    return papers


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("4002"), debug=True)
