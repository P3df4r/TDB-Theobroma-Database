#!/usr/bin/env python3
#coding: utf-8

import os
from flask import Flask, flash, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
import Blast

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

    mBlast = request.form["modoBlast"]
    uInput = request.form["nucleotideo"]

    if "file" in request.files:
        arquivo = request.files["file"]
        filename = secure_filename(arquivo.filename)
        if arquivo.filename != "":
            arquivo.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    if len(uInput) > 0:
        filename = "userSeq.txt"
        arquivo = open(os.path.join(app.config["UPLOAD_FOLDER"], filename), "w")
        arquivo.write(uInput)
        arquivo.close

    Blast.run(tipoAValor[mBlast], os.path.join(app.config["UPLOAD_FOLDER"], filename), "sample.fna", "resultado.xml")
    return render_template("download.html")

@app.route("/download")
def downloadxml():
    return send_file("resultado.xml", as_attachment=True)

if __name__ == "__main__":
    app.run(host="192.168.10.68", debug=True)
