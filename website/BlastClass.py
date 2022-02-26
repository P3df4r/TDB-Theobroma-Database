#!/usr/bin/env python3
#coding: utf-8
import os
from Bio.Blast import NCBIWWW
from Bio import SeqIO
output = None

class Blast:

    bValToBin = ["" for _ in range(0, 5)]
    bValToBin[1] = "blastn"
    bValToBin[2] = "blastp"
    bValToBin[3] = "blastx"
    bValToBin[4] = "tblastn"

    def __init__(self, output):
        self.output = output
    def blastNN (self, subject, query):
        if (query != "genomas/treeNC_030850.1.fasta"):
            teste = SeqIO.read("genomas/treeNC_030850.1.fasta", format='fasta')
            teste1 = NCBIWWW.qblast("blastn", "nt", teste.seq, format_type='XML')
            out = open('downloads/output.xml', 'a')
            out.write(teste1.read())
        if (query != "genomas/treeCM001879.1.fasta"):
            teste = SeqIO.read("genomas/treeCM001879.1.fasta", format='fasta')
            teste1 = NCBIWWW.qblast("blastn", "nt", teste.seq, format_type='XML')
            out = open('downloads/output.xml', 'a')
            out.write(teste1.read())
    def blastPP (self, subject, query):
        if (query != "genomas/treeNC_030850.1.fasta"):
            teste = SeqIO.read("genomas/treeNC_030850.1.fasta", format='fasta')
            teste1 = NCBIWWW.qblast("blastp", "nt", teste.seq, format_type='XML')
            out = open('downloads/output.xml', 'a')
            out.write(teste1.read())
        if (query != "genomas/treeCM001879.1.fasta"):
            teste = SeqIO.read("genomas/treeCM001879.1.fasta", format='fasta')
            teste1 = NCBIWWW.qblast("blastp", "nt", teste.seq, format_type='XML')
            out = open('downloads/output.xml', 'a')
            out.write(teste1.read())
    def blastNP (self, subject, query):
        if (query != "genomas/treeNC_030850.1.fasta"):
            teste = SeqIO.read("genomas/treeNC_030850.1.fasta", format='fasta')
            teste1 = NCBIWWW.qblast("blastx", "nt", teste.seq, format_type='XML')
            out = open('downloads/output.xml', 'a')
            out.write(teste1.read())
        if (query != "genomas/treeCM001879.1.fasta"):
            teste = SeqIO.read("genomas/treeCM001879.1.fasta", format='fasta')
            teste1 = NCBIWWW.qblast("blastx", "nt", teste.seq, format_type='XML')
            out = open('downloads/output.xml', 'a')
            out.write(teste1.read())
    def blastPN (self, subject, query):
        if (query != "genomas/treeNC_030850.1.fasta"):
            teste = SeqIO.read("genomas/treeNC_030850.1.fasta", format='fasta')
            teste1 = NCBIWWW.qblast("tblastn", "nt", teste.seq, format_type='XML')
            out = open('downloads/output.xml', 'a')
            out.write(teste1.read())
        if (query != "genomas/treeCM001879.1.fasta"):
            teste = SeqIO.read("genomas/treeCM001879.1.fasta", format='fasta')
            teste1 = NCBIWWW.qblast("tblastn", "nt", teste.seq, format_type='XML')
            out = open('downloads/output.xml', 'a')
            out.write(teste1.read())

    def run(self, subject, blast, query):
        bTypeSwitch = {
            "blastn"  : self.blastNN, 
            "blastp"  : self.blastPP, 
            "blastx"  : self.blastNP, 
            "tblastn"  : self.blastPN 
        }
        blastBin = self.bValToBin[blast]
        bTypeSwitch[blastBin](subject, query)
        #teste = NCBIWWW.qblast("blastn", query, subject, format_type='text')
