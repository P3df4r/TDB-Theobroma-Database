from Bio import Phylo
from Bio.Align.Applications import ClustalwCommandline
import matplotlib.pyplot as plt
import matplotlib

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

print("Gerando árvore")
Phylo.convert("mfasta.dnd", "newick", "mfasta.nex", 'nexus')
tree = Phylo.read('mfasta.nex', 'nexus')
fig = plt.figure(figsize=(17, 10), dpi=100) 
matplotlib.rc('font', size=8)       
matplotlib.rc('xtick', labelsize=10)
matplotlib.rc('ytick', labelsize=10)
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(tree, axes=axes)
fig.savefig("mfasta.pdf")
