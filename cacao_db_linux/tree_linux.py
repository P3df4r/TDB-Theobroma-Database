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
    print("Multifasta criado...")
    return multifasta

def clustal (multifasta):
    print("Preparando alinhamento:")
    alinhar = ClustalwCommandline(clustalwL, infile="mfasta.fasta")
    stdout, stderr = alinhar()
    print(alinhar)
    return

#inserção fasta
multifasta = 0
clustalwL = "clustalW/clustalw2"
quantidade = int(input("Digite a quantidade de fasta: \n"))

#geração multifasta
fasta(quantidade)

#clustalW
clustal(multifasta)

print("Gerando árvore")
tree = Phylo.read("mfasta.dnd", "newick")
Phylo.draw(tree)
