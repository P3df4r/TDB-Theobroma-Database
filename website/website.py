#!/usr/bin/env python3
#coding: utf-8
import os
import Blast
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

HOST_ADDR="localhost"
DATABASE="sample.fna"
XML_NAME="resultado.xml"
QUERY_DEFAULT="userSeq.txt"

app = Flask(__name__)
app.secret_key = b'BDk^iUe99W*0r0S!eM9!8A'
app.config["UPLOAD_FOLDER"] = "./"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def runBlast():
    tipoAValor = {}
    tipoAValor["BlastN"]  = 1
    tipoAValor["BlastP"]  = 2
    tipoAValor["BlastX"]  = 3
    tipoAValor["tBlastN"] = 4
    upFolder = app.config["UPLOAD_FOLDER"]
    mBlast = request.form["modoBlast"]
    uInput = request.form["nucleotideo"]
    bValor = tipoAValor[mBlast]

    filename = ""
    if "file" in request.files:
        arquivo = request.files["file"]
        filename = secure_filename(arquivo.filename)
        if arquivo.filename != "":
            arquivo.save(os.path.join(upFolder, filename))
    if len(uInput) > 0:
        filename = QUERY_DEFAULT
        arquivo = open(os.path.join(upFolder, QUERY_DEFAULT), "w")
        arquivo.write(uInput)
        arquivo.close

    print(os.path.join(app.config["UPLOAD_FOLDER"], XML_NAME))
    #Blast.run(bValor, os.path.join(upFolder, filename), DATABASE, XML_NAME)
    return render_template("download.html")

@app.route("/download")
def downloadxml():
    return send_file(os.path.join(app.config["UPLOAD_FOLDER"], XML_NAME), as_attachment=True)

if __name__ == "__main__":
    app.run(host=HOST_ADDR, debug=True)
