#!/usr/bin/env python3
#coding: utf-8
import os
import subprocess
import BlastClass
import ArvoreFilo
import alignments
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
import docker


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
ARVORE_INST=ArvoreFilo.Arvore()
ALIGN_INST=alignments.Align()
BLAST_INST=BlastClass.Blast(
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

users = {'admin':{'pw':'admin'}}


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


@app.route("/index.html")
@flask_login.login_required
def index():
    count = estatistic()
    sequence_status = "is-hidden"
    if platform == "linux":
        seqspid = os.system("pidof sequenceserver")
        if seqspid != 256:
            sequence_status = ""
    SEQUENCE_BAR_STATUS = sequence_status
    return render_template("./index.html", counts=count, home_bar_classes="is-active", sequence_bar_classes=sequence_status, blast_classes="is-hidden", search_classes="is-hidden", search_detail_classes="is-hidden", paper_classes="is-active", est_classes="is-active")


@app.route("/blast_run", methods=['GET', 'POST'])
def runBlast():
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
        return render_template("blast.html")
    query = os.path.join(upFolder, filename)
    BLAST_INST.run(DATABASES[bValor][dbValor], bValor, query)
    with open('./downloads/output.txt', "r") as f:
        content = f.read()
    print(content)
    return render_template("./blast.html", content=content)

@app.route("/download/blast")
def downloadxml():
    return send_file(
        os.path.join(DOWNLOADS_FOLDER, TEXT_NAME), 
        as_attachment=True, 
        #cache_timeout=0
        )

@app.route('/tree_run', methods=['GET', 'POST'])
def generate_tree():
    genoma = request.form.get("escolhaGenoma")
    uInput = request.form.get("input_manual")
    tree_data = request.files['file_tree']
    upFolder = app.config["UPLOAD_FOLDER"]
    if tree_data.filename != "":
            filename = secure_filename(tree_data.filename)
            tree_data.save(os.path.join(upFolder, filename))
    if len(uInput) > 0:
        filename = QUERY_DEFAULT
        with open(os.path.join(upFolder, filename), "w") as arquivo:
            arquivo.write(uInput)
    input_tree = os.path.join(upFolder, filename)
    teste = ARVORE_INST.run(input_tree, genoma)
    return render_template("tree.html", tree_result=teste)
    
@app.route('/tree')
def tree():
    return render_template("tree.html")

@app.route('/align', methods=['GET', 'POST'])
def generate_align(): 
    genoma = request.form.get("escolhaGenoma")
    modo = request.form.get('escolha_clustal')
    uInput = request.form.get("input_manual")
    genome_data = request.files['file_clustal']
    upFolder = app.config["UPLOAD_FOLDER"]
    if genome_data.filename != "":
            filename = secure_filename(genome_data.filename)
            genome_data.save(os.path.join(upFolder, filename))
    if len(uInput) > 0:
        filename = QUERY_DEFAULT
        with open(os.path.join(upFolder, filename), "w") as arquivo:
            arquivo.write(uInput)
    fasta = open(os.path.join(upFolder, filename), "r")
    input_clustal = os.path.join(upFolder, filename)
    result_clustal = ALIGN_INST.run(input_clustal, genoma, modo)
    print(result_clustal)
    return render_template("clustalw.html", output_clustal_fmt=result_clustal)
    
@app.route('/show_align')
def show_align():
	upFolder = app.config["UPLOAD_FOLDER"]
	return (open(os.path.join(upFolder, "clustalw.aln"), "r"))

@app.route('/clustalw')
def clustalw():
    return render_template("clustalw.html")
    
@app.route('/jbrowse')
def jbrowse():
    return render_template("jbrowse.html", home_bar_classes="is-active")

@app.route('/download')
def download_page():
    return render_template("download.html")

@app.route('/about')
def about():
    return render_template("about.html")
    
@app.route('/blast')
def blast():
    return render_template("blast.html")

@app.route('/search_engine', methods=['POST'])
def search_engine():
    busca = request.form.get("search_input")
    client = docker.DockerClient()
    container = client.containers.get('theobroma_mongodb')
    ip_add = container.attrs['NetworkSettings']['IPAddress']
    client = MongoClient(ip_add)
    db = client.test
    result = []
    i = 0
    tabelas = db.list_collection_names()
    print('pesquisando')
    for a in range(len(tabelas)):
        for x in db[tabelas[a]].find( {"$or": [
    #for collection_name in db.list_collection_names():
    #    collection = db[collection_name]
    #    x = collection.find({"$or": [
            {"Strain":{"$regex": busca, "$options": "i"}},
            {"Cromossome": {"$regex": busca, "$options": "i"}},
            {"Software": {"$regex": busca, "$options": "i"}},
            {"Function": {"$regex": busca, "$options": "i"}},
            {"Start": {"$regex": busca, "$options": "i"}},
            {"Stop": {"$regex": busca, "$options": "i"}},
            {"Score": {"$regex": busca, "$options": "i"}},
            {"Strand": {"$regex": busca, "$options": "i"}},
            {"Phase": {"$regex": busca, "$options": "i"}},
            {"3_prime_partial=": {"$regex": busca, "$options": "i"}},
            {"5_prime_partial=": {"$regex": busca, "$options": "i"}},
            {"ID=": {"$regex": busca, "$options": "i"}},
            {"Name=": {"$regex": busca, "$options": "i"}},
            {"Parent=": {"$regex": busca, "$options": "i"}},
            {"Target=": {"$regex": busca, "$options": "i"}},
            {"cazy=": {"$regex": busca, "$options": "i"}},
            {"classification=": {"$regex": busca, "$options": "i"}},
            {"cog=": {"$regex": busca, "$options": "i"}},
            {"conversion_envent=": {"$regex": busca, "$options": "i"}},
            {"description=": {"$regex": busca, "$options": "i"}},
            {"domains=": {"$regex": busca, "$options": "i"}},
            {"ec_number=": {"$regex": busca, "$options": "i"}},
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
            {"retrocopy_host=": {"$regex": busca, "$options": "i"}},
            {"retrocopy_parental=": {"$regex": busca, "$options": "i"}},
            {"sequence_ontology=": {"$regex": busca, "$options": "i"}},
            {"signal_peptide=": {"$regex": busca, "$options": "i"}},
            {"tIR=": {"$regex": busca, "$options": "i"}},
            {"tSD=": {"$regex": busca, "$options": "i"}},
            {"tair10=": {"$regex": busca, "$options": "i"}},
            {"tcacao=": {"$regex": busca, "$options": "i"}},
            {"topology=": {"$regex": busca, "$options": "i"}},
            {"tpm=": {"$regex": busca, "$options": "i"}},
            {"transmembrane_domain=": {"$regex": busca, "$options": "i"}},
            {"transposed_gene=": {"$regex": busca, "$options": "i"}},
            ]}, {'_id': 0}):
        #for doc in x:
        #    tmp = list(dict(doc).values())
        #    result.append(tmp)
            i = i + 1
            tmp = list(dict(x).values())
            result.append(tmp)
            if len(result) > 100:
                break
    client.close()
    print(tmp)
    #print(result)
    return render_template("search.html", results=result)

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
    collector = []
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
        temp_paper = []
        temp = ""
        nome = Entrez.esummary(db="pubmed", id=doi[i])
        record = Entrez.read(nome)
        #temp += record[0]["Title"] + " DOI: " + doi[i] + " Publish Date: " + record[0]["PubDate"]+"\t"
        #papers += temp
        collector.append({'title':record[0]["Title"], 'doi':doi[i], "data":record[0]["PubDate"]})
        #collector.append(temp_paper)
        temp_paper = []
    print(collector)
    papers = collector
    return papers


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("4002"), debug=True)
