#!/usr/bin/env python3
#coding: utf-8
import os
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast.Applications import NcbitblastnCommandline
output = None

class Blast:

    bValToBin = ["" for _ in range(0, 5)]
    bValToBin[1] = "blastn"
    bValToBin[2] = "blastp"
    bValToBin[3] = "blastx"
    bValToBin[4] = "tblastn"

    output = None
    def __init__(self, output):
        self.output = output
    def blastNN(self, database, blast, query):
        if database == "Criollo":
            blastn = NcbiblastnCommandline(query=query, db="genomas/Criollo/Criollo_nucl_db", out=self.output, outfmt=0)
            blastn()
        if database == "Matina":
            blastn = NcbiblastnCommandline(query=query, db="genomas/Matina/Matina_nucl_db", out=self.output, outfmt=0)
            blastn()
    def blastPP (self, database, blast, query):
        if database == "Criollo":
            blastp = NcbiblastpCommandline(query=query, db="genomas/Criollo/Criollo_prot_db", outfmt=0, out=self.output)
            blastp()
        if database == "Matina":
            blastp = NcbiblastpCommandline(query=query, db="genomas/Matina/Marina_prot_db", outfmt=0, out=self.output)
            blastp()
    def blastNP (self, database, blast, query):
        if database == "Criollo":
            blastx = NcbiblastxCommandline(query=query, db="genomas/Criollo/Criollo_prot_db", outfmt=0, out=self.output)
            blastx()
        if database == "Matina":
            blastx = NcbiblastxCommandline(query=query, db="genomas/Matina/Matina_prot_db", outfmt=0, out=self.output)
            blastx()
    def blastPN (self, database, blast, query):
        if database == "Criollo":
            tblastn = NcbitblastnCommandline(query=query, db="genomas/Criollo/Criollo_nucl_db", outfmt=0, out=self.output)
            tblastn()
        if database == "Matina":
            tblastn = NcbitblastnCommandline(query=query, db="genomas/Matina/Matina_nucl_db", outfmt=0, out=self.output)
            tblastn()
    def run(self, database, blast, query):
        bTypeSwitch = {
            "blastn"  : self.blastNN,
            "blastp"  : self.blastPP,
            "blastx"  : self.blastNP,
            "tblastn"  : self.blastPN
        }
        blastBin = self.bValToBin[blast]
        bTypeSwitch[blastBin](database, blastBin, query)
