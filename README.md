### Version PT/BR

#### Desenvolvido por: Pedro Augusto, José Perdigão e Dr. Vincícius Abreu

# TDB - THEOBROMA DATABASE

# Para instalação inicial, siga os seguintes comandos:

Execute o primeiro script, denomindao "install.sh"
> sudo bash install.sh
Colete o ID do container:
> sudo docker ps
Execute o container:
> sudo docker exec -i -t CONTAINER_ID
Execute o segundo script, denomindao "data.sh":
> sudo bash data.sh
Acesse no navegador:
> localhost:5000

## Instalação Individual

-> Ferramentas utilizadas:

- Python version 3.9.4 (https://www.python.org/downloads/)
- Biopython version 1.78 (https://biopython.org/wiki/Download)
- NCBI-Blast version 2.11.0+ (https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)

-> Instalações necessárias:

ATENÇÃO: USE INSTALAÇÕES PADRÕES (Linux: usr/bin/)

- pip install ncbi-Blast+
- pip install biopython

### Version EN

#### Developed by: Pedro Augusto, José Perdigão, Amanda Alcântra and Dr. Vincícius Abreu

# TDB - THEOBROMA DATABASE

### Flask web application 


To configure and use the application for the first time, use the following command

> ../TDB-Theobroma-Database/cacao_db_linux/install.sh

Note: If the application does not work, use the following command in the same directory

> chmod +x install.sh

To run the application already configured, use the following command:

> ../TDB-Theobroma-Database/website/python3 website.py

Accessing in the browser:

> localhost:5000

### Individual Installation

-> Tools used:

- Python version 3.9.4 (https://www.python.org/downloads/) 
- Biopython version 1.78 (https://biopython.org/wiki/Download)
- NCBI-Blast version 2.11.0+ (https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)

-> Required installations:

WARNING: USE STANDARD INSTALLATIONS (Linux: usr/bin/)

- pip install ncbi-Blast+
- pip install biopython
