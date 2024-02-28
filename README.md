### Version PT/BR

#### Desenvolvido por: Pedro Augusto, José Perdigão e Dr. Vincícius Abreu

# TDB - THEOBROMA DATABASE

# Para instalação inicial, siga os seguintes comandos:

Instale o docker para seu sistema (No exemplo abaixo, utilizaremos Ubuntu/Debian)
> sudo apt install docker.io

Instale a ultima versão do mongoDB
> sudo docker pull mongo:latest

Crie uma conexão(network) para ser usada entre os dockers
> sudo docker network create tdb_brige

Colete o ID da conexão(network)
> sudo docker network ls

Construa o container "tdb_docker", sendo esse o principal da aplicação, 
> sudo docker build --tag tdb_docker --network NETWORK_ID .

Construa o container "theobroma_mongodb", sendo esse o banco de dados
> sudo docker run -d -p 27017:27017 -v ~/data/db --network NETWORK_id --name theobroma_mongodb mongo:latest

Colete o ID do container "tdb_docker":
> sudo docker ps

Execute o seguinte comando para entrar no container "tdb_docker":
> sudo docker exec -i -t CONTAINER_ID "/bin/bash"

 Execute o script denominado "data.sh":
> sudo bash data.sh

Acesse no navegador:
> localhost:5000

## Instalação Individual

-> Ferramentas utilizadas:

- Python version 3.9.4 (https://www.python.org/downloads/)
- Biopython version 1.78 (https://biopython.org/wiki/Download)
- NCBI-Blast version 2.11.0+ (https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download)

