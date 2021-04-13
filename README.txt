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

-> Instalações necessárias (windows/Linux):

ATENÇÃO: USE INSTALAÇÕES PADRÕES (Windows: Disco C/Linux: usr/bin/)

pip install ncbi-Blast+
pip install biopython

-> Formatos recomendados: .fna/.fasta

-> Manual:
- query: arquivo principal a ser analisado (colocar com extensão. Ex: TN.fasta ou TN.fna)
- nt: arquivo a ser comparado com o principal (ou organismo modelo) (colocar com extensão. Ex: BR.fasta ou BR.fna)

-> Arquivo de saída: A critério do usuário. Recomenda-se extensão '.xml' para organismos maiores que 10 mb. Para arquivos menores, '.txt' torna-se interessante.

-> Possíveis erros:

- Erro ao executar o Python (Windows)

Ocorrer devido a não identificação do Python pelo sistema, sendo necessário executar sua instalação pelo Store do Windows.

- Erro na instalação das bibliotecas

Ocorre principalmente na instalação do biopython/ncbi devido a dificuldade de obter o "pip". O pip vem junto com a instalação do python no sistema, entretanto, caso não exista, torna-se necessário baixar o código do "pip" e copiar o mesmo nos scripts do python, para executar de forma correta.

- Erro na "execução não encontrada" ou "não reconhecido como um comando interno"

Esse erro ocorre devido a pasta que encontra-se instalado o biopython ou o blast. Utilizar o comando "locate 'blast necessário'" no linux para verificar o local de instalação. No windows, abrir explorador de arquivos (Tecla Windows + E), teclar F3 e localizar o blast desejado.

Após a obtenção da localização, alterar a variável da função desejada. Segue a abaixo as variáveis de cada função:

Blastn -> Utilizada no BlastNN.py
Blastp -> Utilizada no BlastPP.py
blastx -> Utilizada no BlastNP.py
tblastn -> Utilizada no BlastPN.py
