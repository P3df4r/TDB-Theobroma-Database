echo ---------------------------------------DOCKER-------------------------------------------------------------
docker pull mongo:latest
docker pull ubuntu:latest
docker run -d -p 27017:27017 -v ~/data/db --name theobroma_mongodb mongo:latest #"theobroma_mongodb" é o nome do banco de dados que deve ser acessado por "docker exec -i -t theobroma_mongodb /bin/bash"
docker start theobroma_mongodb
#docker run -d -p 27017:27017 -v ~/data/db --name TheobromaDB mongo:latest
docker cp install.sh theobroma_mongodb:/.
docker exec theobroma_mongodb bash install.sh
