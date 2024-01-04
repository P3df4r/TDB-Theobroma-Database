#!/usr/bin/env python3
#coding: utf-8
import os
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from sys import platform
from Bio import Phylo
from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline
import matplotlib.pyplot as plt
import matplotlib

class Arvore:
	
    def run(self, fasta, genoma):
        print('Iniciando alinhamento')
        list_genome = {'0':'./static/dados/Criollo_new/Criollo.fasta', '6':'./static/dados/exemplos/ncbi_dataset/data/gene.fna'}
        temp_fasta = open(os.path.join(fasta), 'r')
        temp_database = open(os.path.join(list_genome[genoma]), "r")
        fastao = temp_fasta.read() + '\n' + temp_database.read()      
        with open('teste.txt', "w") as arquivo:
            arquivo.write(fastao)
        print('Alinhando')
        comand_line = ClustalwCommandline('clustalw', infile='teste.txt', outfile='./uploads/tree_clustalw.aln', type='dna', output="clustal")()
        read_tree = AlignIO.read('./uploads/tree_clustalw.aln', 'clustal')
        calculo = DistanceCalculator('identity')
        distance_matrix = calculo.get_distance(read_tree)
        contrutor = DistanceTreeConstructor()
        arvore = contrutor.upgma(distance_matrix)
        #tree = Phylo.read("./uploads/tree_clustalw.aln", "n")
        fig = plt.figure(figsize=(200, 80), dpi=300) 
        plt.rcParams.update({'font.size':90})
        axes = fig.add_subplot(1, 1, 1)
        figura = plt.gcf()
        Phylo.draw(arvore, axes=axes, do_show=False)
        #Phylo.draw(arvore, axes=axes, branch_labels=None)
        fig.savefig("downloads/tree.pdf")
