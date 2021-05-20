#Aplicação web Flask

Instale as dependências
```
apt-get install ncbi-blast+
pip install biopython
pip install Flask
```

Configure no cabeçalho do arquivo `website.py` os valores padrões
```
HOST_ADDR="localhost"
DATABASE="sample.fna"
XML_NAME="resultado.xml"
QUERY_DEFAULT="userSeq.txt"
```

Execute a aplicação
```
python3 website.py
```

Acesse no navegador
```
localhost:5000
```

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

-> Arquivo Blastdb_*.py
Esse formato de uso do blast é utilizado para multifasta, a qual obtem-se diversos fasta dentro de um único arquivo para a criação do "database". Para realizar a operação com essa variação, utilizar o comando

makeblastdb -in organismo.fasta -dbtype nucl/prot -out organismo_db -title nome_do_db

ATENÇÃO: Caso esteja trabalhando com NUCLEOTÍDIO, utilizar a variação "nucl" após o -dbtype. No caso de PRTEÍNA, utilizar "prot"
