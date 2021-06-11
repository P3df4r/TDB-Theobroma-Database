#!/usr/bin/env python3
#coding: utf-8
import os
from Bio.Blast.Applications import NcbiblastnCommandline as BlastN
from Bio.Blast.Applications import NcbiblastpCommandline as BlastP
from Bio.Blast.Applications import NcbiblastxCommandline as BlastX
from Bio.Blast.Applications import NcbitblastnCommandline as tBlastN

class Blast:
    bValToBin = ["" for _ in range(0, 5)]
    bValToBin[3] = "/usr/bin/blastn"
    bValToBin[1] = "/usr/bin/blastp"
    bValToBin[2] = "/usr/bin/blastx"
    bValToBin[4] = "/usr/bin/tblastn"
    if os.name == "nt":
        bValToBin[3] = "C:/Program Files/NCBI/blast-2.10.1+/bin/blastn"
        bValToBin[1] = "C:/Program Files/NCBI/blast-2.10.1+/bin/blastp"
        bValToBin[2] = "C:/Program Files/NCBI/blast-2.10.1+/bin/blastx"
        bValToBin[4] = "C:/Program Files/NCBI/blast-2.10.1+/bin/tblastn"
    output = None
    def __init__(self, output):
        self.output = output
    def blastNN(self, database, blast, query):
        BlastN(
            cmd=blast, 
            query=query, 
            subject=database, 
            evalue=0.001, 
            outfmt=5, 
            out=self.output
        )()
    def blastPP (self, database, blast, query):
        BlastP(
            cmd=blast, 
            query=query, 
            subject=database, 
            evalue=0.001, 
            outfmt=5, 
            out=self.output
        )()
    def blastNP (self, database, blast, query):
        BlastX(
            cmd=blast, 
            query=query, 
            subject=database, 
            evalue=0.001, 
            outfmt=5, 
            out=self.output
        )()
    def blastPN (self, database, blast, query):
        tBlastN(
            cmd=blast, 
            query=query, 
            subject=database, 
            evalue=0.001, 
            outfmt=5, 
            out=self.output
        )()
    def run(self, database, blast, query):
        bTypeSwitch = {
            "/usr/bin/blastn"  : self.blastNN, 
            "/usr/bin/blastp"  : self.blastPP, 
            "/usr/bin/blastx"  : self.blastNP, 
            "/usr/bin/tblastn" : self.blastPN, 
            "C:/Program Files/NCBI/blast-2.10.1+/bin/blastn"  : self.blastNN, 
            "C:/Program Files/NCBI/blast-2.10.1+/bin/blastp"  : self.blastPP, 
            "C:/Program Files/NCBI/blast-2.10.1+/bin/blastx"  : self.blastNP, 
            "C:/Program Files/NCBI/blast-2.10.1+/bin/tblastn" : self.blastPN
        }
        blastBin = self.bValToBin[blast]
        bTypeSwitch[blastBin](database, blastBin, query)

