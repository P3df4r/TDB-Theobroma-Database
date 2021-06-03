from Bio import Phylo
from Bio.Align.Applications import ClustalwCommandline

def fasta (quantidade):
    for i in range(quantidade):
        mfasta = input("Insira o nome do {} fasta: \n". format(i+1))
        arquivo = open(mfasta, "r")
        save = arquivo.read()
        output = open("mfasta.fasta", "a")
        output.write(save)
    multifasta= save
    return multifasta

def clustal (multifasta):
    alinhar = ClustalwCommandline(clustalww64, infile="mfasta.fasta")
    stdout, stderr = alinhar()
    print(alinhar)
    return

#inserção fasta
multifasta = 0
clustalww64 = "C:\Program Files (x86)\ClustalW2\clustalw2.exe"
quantidade = int(input("Digite a quantidade de fasta: \n"))

#geração multifasta
fasta(quantidade)

#clustalW
clustal(multifasta)

tree = Phylo.read("mfasta.dnd", "newick")
Phylo.draw(tree)