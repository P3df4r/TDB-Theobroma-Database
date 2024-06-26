import os
import Bio
from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline
from bioinfokit.analys import Fasta


class Align:

    def run(self, fasta, genoma, modo):
        print('Iniciando alinhamento')
        list_genome = {'0':'./static/dados/Criollo_new/Criollo.fasta', '1':'./static/dados/Matina_new/Matina.fasta', '2':'./static/dados/C1074P/C1074P.fasta','3':'./static/dados/C174P/C174P.fasta','4':'./static/dados/C174/C174.fa','5':'./static/dados/C1074/C1074.fasta','6':'./static/dados/example/atpA_2.fasta'}
        temp_fasta = open(os.path.join(fasta), 'r')
        temp_database = open(os.path.join(list_genome[genoma]), "r")
        #print(temp_fasta)
        #print(temp_database)
        fastao = temp_fasta.read() + '\n' + temp_database.read()      
        with open('./uploads/temp_clustal.txt', "w") as arquivo:
            arquivo.write(fastao)
        print('Alinhando')
        if modo == '0':
            comand_line = ClustalwCommandline('clustalw', infile='./uploads/output.fasta', outfile='./uploads/clustalw.aln', type='dna')()
        else:
            comand_line = ClustalwCommandline('clustalw', infile='./uploads/temp_clustal.txt', outfile='./uploads/clustalw.aln', type='protein')()
        print('Alinhado')
        #clustal_result = AlignIO.read('./uploads/clustalw.aln', "clustal")
        #teste = Fasta.multi_to_single_line(file='./uploads/clustalw.aln')
        #os.rename('./output.fasta', './uploads/output.fasta')
        clustal_result = open('./uploads/clustalw.aln','r')
        result_clustal = clustal_result.read()
        print('alinhado')
        return result_clustal
