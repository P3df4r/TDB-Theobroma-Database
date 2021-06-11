#!/usr/bin/env python3
#coding: utf-8
from sys import platform
from Bio import Phylo
from Bio.Align.Applications import ClustalwCommandline
import matplotlib.pyplot as plt
import matplotlib

class Arvore:
    def run(self, listaFastas):
        clustalww64 = "../cacao_db_linux/clustalW/clustalw2"
        if platform != "linux":
            clustalww64 = "C:\Program Files (x86)\ClustalW2\clustalw2.exe"
        save = ""
        for ifasta in listaFastas:
            with open(ifasta, "r") as arquivo:
                save += arquivo.read()
        with open("mfasta.fasta", "w") as output:
            output.write(save)
        ClustalwCommandline(clustalww64, infile="mfasta.fasta")()
        Phylo.convert("mfasta.dnd", "newick", "mfasta.nex", "nexus")
        tree = Phylo.read("mfasta.nex", "nexus")
        fig = plt.figure(figsize=(17, 10), dpi=100) 
        matplotlib.rc("font", size=8)       
        matplotlib.rc("xtick", labelsize=10)
        matplotlib.rc("ytick", labelsize=10)
        axes = fig.add_subplot(1, 1, 1)
        Phylo.draw(tree, axes=axes)
        fig.savefig("downloads/tree.pdf")
