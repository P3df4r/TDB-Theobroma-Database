#!/usr/bin/env python3
import os
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast.Applications import NcbiblastxCommandline
from Bio.Blast.Applications import NcbitblastnCommandline

class Blast:

    bValToBin = ["" for _ in range(0, 5)]
    bValToBin[1] = "blastn"
    bValToBin[2] = "blastp"
    bValToBin[3] = "blastx"
    bValToBin[4] = "tblastn"

    output = ''
    def __init__(self, output):
        self.output = output
    def blastNN(self, database, blast, query):
        if database == "Criollo":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/Criollo_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "Matina":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/Matina_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C1074":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C1074_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C174":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C174_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C1074P":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C1074p_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C174P":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C174P_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            blastn()

    def blastPP (self, database, blast, query):
        if database == "Criollo":
            blastp = NcbiblastpCommandline(query=query, db="static/blast_db/Criollo_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastp()
        if database == "Matina":
            blastp = NcbiblastpCommandline(query=query, db="static/blast_db/Matina_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastp()
        if database == "C1074":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C1074_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C174":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C174_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C1074P":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C1074P_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C174P":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C174P_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastn()
    def blastNP (self, database, blast, query):
        if database == "Criollo":
            blastx = NcbiblastxCommandline(query=query, db="static/blast_db/Criollo_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastx()
        if database == "Matina":
            blastx = NcbiblastxCommandline(query=query, db="static/blast_db/Matina_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastx()
        if database == "C1074":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C1074_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C174":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C174_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C1074P":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C1074P_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C174P":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C174P_prot_db", outfmt="0", out=self.output, evalue="0.001", gapextend="2", word_size=5)
            blastn()
    def blastPN (self, database, blast, query):
        if database == "Criollo":
            tblastn = NcbitblastnCommandline(query=query, db="static/blast_db/Criollo_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            tblastn()
        if database == "Matina":
            tblastn = NcbitblastnCommandline(query=query, db="static/blast_db/Matina_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            tblastn()
        if database == "C1074":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C1074_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C174":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C174_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C1074P":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C1074P_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            blastn()
        if database == "C174P":
            blastn = NcbiblastnCommandline(query=query, db="static/blast_db/C174P_nucl_db", out=self.output, outfmt="0", evalue="0.001", gapextend="2", word_size=5)
            blastn()
    def run(self, database, blast, query):
        bTypeSwitch = {
            "blastn"  : self.blastNN,
            "blastp"  : self.blastPP,
            "blastx"  : self.blastNP,
            "tblastn"  : self.blastPN
        }
        blastBin = self.bValToBin[blast]
        bTypeSwitch[blastBin](database, blastBin, query)
