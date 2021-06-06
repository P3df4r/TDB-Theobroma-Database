#!/usr/bin/env python3
#coding: utf-8
from Bio.Blast.Applications import NcbiblastnCommandline as BlastN
from Bio.Blast.Applications import NcbiblastpCommandline as BlastP
from Bio.Blast.Applications import NcbiblastxCommandline as BlastX
from Bio.Blast.Applications import NcbitblastnCommandline as tBlastN

class Blast:
    bValToBin = ["" for _ in range(0, 5)]
    bValToBin[1] = "/usr/bin/blastn"
    bValToBin[2] = "/usr/bin/blastp"
    bValToBin[3] = "/usr/bin/blastx"
    bValToBin[4] = "/usr/bin/tblastn"
    output = None
    dbList = None
    def __init__(self, databases, output):
        self.output = output
        self.dbList = databases
    def blastNN(self, database, blast, query):
        BlastN(
            cmd=blast, 
            query=query, 
            subject=self.dbList[database], 
            strand="plus", 
            evalue=0.001, 
            outfmt=5, 
            out=self.output
        )()
    def blastPP (self, database, blast, query):
        BlastP(
            cmd=blast, 
            query=query, 
            subject=self.dbList[database], 
            strand="plus", 
            evalue=0.001, 
            outfmt=5, 
            out=self.output
        )()
    def blastNP (self, database, blast, query):
        BlastX(
            cmd=blast, 
            query=query, 
            subject=self.dbList[database], 
            strand="plus", 
            evalue=0.001, 
            outfmt=5, 
            out=self.output
        )()
    def blastPN (self, database, blast, query):
        tBlastN(
            cmd=blast, 
            query=query, 
            subject=self.dbList[database], 
            strand="plus", 
            evalue=0.001, 
            outfmt=5, 
            out=self.output
        )()
    def run(self, database, blast, query):
        bTypeSwitch = {
            "/usr/bin/blastn"  : self.blastNN, 
            "/usr/bin/blastp"  : self.blastPP, 
            "/usr/bin/blastx"  : self.blastNP, 
            "/usr/bin/tblastn" : self.blastPN
        }
        blastBin = self.bValToBin[blast]
        bTypeSwitch[blastBin](database, blastBin, query)

