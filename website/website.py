#!/usr/bin/env python3
#coding: utf-8
import os
import BlastClass
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename

HOST_ADDR="localhost"
DATABASES=["database1.fna", "databaseN.fna"]
QUERY_DEFAULT="userSeq.txt"
UPLOADS_FOLDER="uploads/"
DOWNLOADS_FOLDER="downloads/"
XML_NAME="resultado.xml"
BLAST_INST = BlastClass.Blast(
    DATABASES, 
    os.path.join(
        DOWNLOADS_FOLDER, 
        XML_NAME
    )
)

app = Flask(__name__)
app.secret_key = b'BDk^iUe99W*0r0S!eM9!8A'
app.config["UPLOAD_FOLDER"] = UPLOADS_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def runBlast():
    upFolder = app.config["UPLOAD_FOLDER"]
    mBlast = request.form["modoBlast"]
    uInput = request.form["nucleotideo"]
    genoma = request.form["escolhaGenoma"]
    bValor = int(mBlast)
    dbValor = int(genoma)
    filename = ""

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
        return redirect(request.url)

    query = os.path.join(upFolder, filename)
    BLAST_INST.run(dbValor, bValor, query)
    return redirect(url_for("downloadxml"))

@app.route("/download")
def downloadxml():
    return send_file(
        os.path.join(DOWNLOADS_FOLDER, XML_NAME), 
        as_attachment=True, 
        cache_timeout=0
    )

if __name__ == "__main__":
    app.run(host=HOST_ADDR, debug=True)

