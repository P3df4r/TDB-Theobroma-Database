from Bio.Blast.Applications import *
import time

print("Digite o arquivo query: ")
query = input()
print("Digite o arquivo do database: ")
nt = input()
tblastn1 = "C:/Program Files/NCBI/blast-2.10.1+/bin/tblastn"
print("Digite o arquivo de saída: ")
output = input()

#help(NcbiblastnCommandline)

time_S = time.time()
code = NcbiblastpCommandline(cmd=tblastn1, query=query, subject=nt, strand="plus", evalue=0.001, outfmt=5, out=output)
print("Input code: ", code)
stdout, stderr = code()
blast_result = open(output, "r")
save = blast_result.read()
time_E = time.time()
print(save)
if (time_E - time_S)/60 < 60:
    print("Tempo decorrido: ", round((time_E - time_S), 4), "segundos")
else:
    print("Tempo decorrido: ", round((time_E - time_S)/60, 4), "minutos")