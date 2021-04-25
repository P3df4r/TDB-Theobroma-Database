#bibliotecas
from Bio.Blast.Applications import *
import time

#funções blast (biopython)
def blastNN (query, nt, output):
    time_S = time.time()
    code = NcbiblastnCommandline(cmd=blast, query=query, db=nt, strand="plus", evalue=0.001, outfmt=5,
                                 out=output)
    print("Input code: ", code)
    stdout, stderr = code()
    blast_result = open(output, "r")
    save = blast_result.read()
    time_E = time.time()
    if (time_E - time_S) / 60 < 60:
        print("Tempo decorrido: ", round((time_E - time_S), 4), "segundos")
    else:
        print("Tempo decorrido: ", round((time_E - time_S) / 60, 4), "minutos")
    print(save)
    return save
def blastPP (query, nt, output):
    time_S = time.time()
    code = NcbiblastpCommandline(cmd=blast, query=query, db=nt, strand="plus", evalue=0.001, outfmt=5,
                                 out=output)
    print("Input code: ", code)
    stdout, stderr = code()
    blast_result = open(output, "r")
    save = blast_result.read()
    time_E = time.time()
    if (time_E - time_S) / 60 < 60:
        print("Tempo decorrido: ", round((time_E - time_S), 4), "segundos")
    else:
        print("Tempo decorrido: ", round((time_E - time_S) / 60, 4), "minutos")
    print(save)
    return save
def blastNP (query, nt, output):
    time_S = time.time()
    code = NcbiblastxCommandline(cmd=blast, query=query, db=nt, strand="plus", evalue=0.001, outfmt=5,
                                 out=output)
    print("Input code: ", code)
    stdout, stderr = code()
    blast_result = open(output, "r")
    save = blast_result.read()
    time_E = time.time()
    if (time_E - time_S) / 60 < 60:
        print("Tempo decorrido: ", round((time_E - time_S), 4), "segundos")
    else:
        print("Tempo decorrido: ", round((time_E - time_S) / 60, 4), "minutos")
    print(save)
    return save
def blastPN (query, nt, output):
    time_S = time.time()
    code = NcbitblastnCommandline(cmd=blast, query=query, db=nt, strand="plus", evalue=0.001, outfmt=5,
                                 out=output)
    print("Input code: ", code)
    stdout, stderr = code()
    blast_result = open(output, "r")
    save = blast_result.read()
    time_E = time.time()
    if (time_E - time_S) / 60 < 60:
        print("Tempo decorrido: ", round((time_E - time_S), 4), "segundos")
    else:
        print("Tempo decorrido: ", round((time_E - time_S) / 60, 4), "minutos")
    print(save)
    return save

#print blast
print('Digite a opção desejada de Blast para execução: '
      '\n1 BlastN'
      '\n2 BlastP'
      '\n3 BlastX'
      '\n4 tBlastN')

print('Blast desejado: ')
blast = int(input())

print("Digite o arquivo query: ")
query = input()
print("Digite o arquivo referência: ")
nt = input()
print("Digite o arquivo de saída: ")
output = input()

#Execução blast
if blast == 1:
    blast = "C:/Program Files/NCBI/blast-2.10.1+/bin/blastn"
    blastNN(query, nt, output)
else:
    if blast == 2:
        blast = "C:/Program Files/NCBI/blast-2.10.1+/bin/blastp"
        blastPP(query, nt, output)
    else:
        if blast == 3:
            blast = "C:/Program Files/NCBI/blast-2.10.1+/bin/blastx"
            blastNP(query, nt, output)
        else:
            if blast == 4:
                blast = "C:/Program Files/NCBI/blast-2.10.1+/bin/tblastn"
                blastPN(query, nt, output)