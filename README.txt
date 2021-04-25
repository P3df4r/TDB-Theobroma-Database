  ______      ___        ______      ___        ______       _______  .______
 /      |    /   \      /      |    /   \      /  __  \     |       \ |   _  \
|  ,----'   /  ^  \    |  ,----'   /  ^  \    |  |  |  |    |  .--.  ||  |_)  |
|  |       /  /_\  \   |  |       /  /_\  \   |  |  |  |    |  |  |  ||   _  <
|  `----. /  _____  \  |  `----. /  _____  \  |  `--'  |    |  '--'  ||  |_)  |
 \______|/__/     \__\  \______|/__/     \__\  \______/     |_______/ |______/


Desenvolvido por: Pedro Augusto

-> Ferramentas utilizadas:

Python version 3.9.4 (https://www.python.org/downloads/) 
Biopython version 1.78 (https://biopython.org/wiki/Download)
NCBI-Blast version 2.11.0+ (https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)

-> Instalações necessárias (Windows/Linux):

ATENÇÃO: USE INSTALAÇÕES PADRÕES (Windows: Disco C e Linux: usr/bin/)

pip install ncbi-Blast+
pip install biopython

-> Formatos recomendados: .fna/.fasta

-> Manual:
- arquivo query: arquivo principal a ser analisado (colocar com extensão. Ex: TN.fasta ou TN.fna)
- arquivo referência: arquivo a ser comparado e utilizado como referência (colocar com extensão. Ex: TN.fasta ou TN.fna)

-> Arquivo de saída: A critério do usuário. Recomenda-se extensão '.xml' para organismos maiores que 10 mb. Para arquivos menores, '.txt' torna-se interessante
