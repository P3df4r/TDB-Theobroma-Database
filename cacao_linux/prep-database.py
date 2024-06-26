import sys

output_filename = sys.argv[1]
input_filename = sys.argv[1]

with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    first_line = input_file.readline().split('\t')
    termos = list(map(str, first_line))
    output_file.write('\t'.join(first_line))
    new_termos = termos[10:]
    temp_line = []
    for a in input_file:
        marcador = ''
        temp = a.replace('\n', '').split('\t')
        temp_dados_cut = temp[8:] #Coluna q inicia os dados especificos
        temp_termos_cut = termos[9:] #coluna que inicia os termos especificos
        temp_write = temp[:8] #Colunas que contem os termos em comum
        temp_write_2 = input_filename + '\t'+ '\t'.join(temp_write) + '\t'
        output_file.write(temp_write_2)
        for i in temp_termos_cut:
            for b in temp_dados_cut:
                marcador = False
                if i in b:
                    marcador = True
                    dado_mod = b.replace(i, '')
                    temp_line.append(dado_mod)
                    break
            if marcador == False:
                temp_line.append('No Information')
        output_file.write('\t'.join(temp_line) + '\n')
        temp_line = []
#Fechando os arquivos
input_file.close()
output_file.close()

