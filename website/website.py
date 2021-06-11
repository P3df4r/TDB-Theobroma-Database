#!/usr/bin/env python3
#coding: utf-8
import os
import BlastClass
import ArvoreFilo
from sys import platform
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename

HOST_ADDR="localhost"
DATABASES={
    1 : ["genomas/protNC_030850.1.fasta", "genomas/protCM001879.1.fasta"], 
    2 : ["genomas/NC_030850.1.fasta", "genomas/CM001879.1.fasta"]
}
QUERY_DEFAULT="userSeq.fasta"
UPLOADS_FOLDER="uploads/"
DOWNLOADS_FOLDER="downloads/"
XML_NAME="resultado.xml"
TREE_NAME="tree.pdf"
ARVORE_INST = ArvoreFilo.Arvore()
BLAST_INST = BlastClass.Blast(
    os.path.join(
        DOWNLOADS_FOLDER, 
        XML_NAME
    )
)
SEQUENCE_BAR_STATUS=""

app = Flask(__name__)
app.secret_key = b'BDk^iUe99W*0r0S!eM9!8A'
app.config["UPLOAD_FOLDER"] = UPLOADS_FOLDER

@app.route("/")
def home():
    sequence_status = "is-hidden"
    if platform == "linux":
        seqspid = os.system("pidof sequenceserver")
        if seqspid != 256:
            sequence_status = ""
    SEQUENCE_BAR_STATUS = sequence_status
    return render_template("index.html", home_bar_classes="is-active", sequence_bar_classes=sequence_status, blast_classes="is-hidden")

@app.route("/", methods=["POST"])
def runBlast():
    filename = ""
    genoma1 = request.form.get("genoma1")
    genoma2 = request.form.get("genoma2")
    genomaU = request.form.get("tree-nucleotideo")
    if genoma1 or genoma2:
        listaFastas = []
        if genoma1:
            listaFastas.append("genomas/{}.fasta".format(genoma1))
        if genoma2:
            listaFastas.append("genomas/{}.fasta".format(genoma2))
        if "file" in request.files:
            arquivo = request.files["file"]
            if arquivo.filename != "":
                filename = secure_filename(arquivo.filename)
                arquivo.save(os.path.join("genomas/", filename))
                listaFastas.append("genomas/{}".format(filename))
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
        return render_template("index.html", blast_bar_classes="is-active", sequence_bar_classes=SEQUENCE_BAR_STATUS, home_classes="is-hidden")

    query = os.path.join(upFolder, filename)
    BLAST_INST.run(DATABASES[bValor][dbValor], bValor, query)
    return redirect(url_for("downloadxml"))

@app.route("/download/blast")
def downloadxml():
    return send_file(
        os.path.join(DOWNLOADS_FOLDER, XML_NAME), 
        as_attachment=True, 
        cache_timeout=0
    )

@app.route("/download/tree")
def downloadtree():
    return send_file(
        os.path.join(DOWNLOADS_FOLDER, TREE_NAME), 
        as_attachment=True, 
        cache_timeout=0
    )

if __name__ == "__main__":
    app.run(host=HOST_ADDR, debug=True)

