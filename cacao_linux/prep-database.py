import sys

output_filename = '{}_mod.gff'.format(sys.argv[1])
input_filename = sys.argv[1]

def collect_terms(file):
    fixed_terms_TDB = ['Strain','Chromossome','Software','Function','Start','Stop','score','strand','phase','3_prime_partial=','5_prime_partial=','ID=','Name=','Parent=','Target=','cazy=','classification=','cog=','conversion_event=','description=','domains=','ec_number=','gene_ontology=','identity=','ltr_identity=','method=','motif=','nlr=','note=','pfam=','plantTFDB=','plantiSMASH=','prgDB=','pseudo=','retrocopy_host=','retrocopy_parental=','sequence_ontology=','signal_peptide=','tIR=','tSD=','tair10=','tcacao=','topology=','tpm=','transmembrane_domain=','transposed_gene=','tsd=']
    fixed_terms = []
    termos = []
    for i in file:
        mod = list(i.replace(';', ',').replace('\t', ',').replace('\n', '').split(','))
        for a in mod:
            if a.find('=') != -1:
                termos.append(a[:a.find('=') + 1])
    new_terms = list(set(termos))
    return fixed_terms_TDB
    #return new_terms
        
def collect_data(file, terms, out):
    out.write(','.join(terms) + '\n')
    for i in file:
        data_temp = []
        mod = list(i.replace(';', ',').replace('\t', ',').replace('\n', '').split(','))
        for b in terms:
            marcador = False
            for a in range(len(mod) - 1):
                print('comparando {} com {}'.format(b,mod[a]))
                if mod[a].find('=') == -1 and mod[a] not in data_temp:
                    data_temp.append(mod[a])
                    marcador = True
                    break
                if b in mod[a]:
                    data_temp.append(mod[a])
                    marcador = True
                    break
            if marcador == False:
                data_temp.append('No information')
        print(terms)
        print(data_temp)
        break
        out.write(','.join(data_temp) + '\n')

with open(input_filename, 'r') as input_file, open(input_filename, 'r') as file_temp, open(output_filename, 'w') as output_file:
    terms = collect_terms(input_file)
    collect_data(file_temp, terms, output_file)
#Fechando os arquivos
input_file.close()
output_file.close()

