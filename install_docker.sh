echo ---------------------------------------DOCKER-------------------------------------------------------------
docker pull mongo:latest
docker pull ubuntu:latest
docker run -d -p 27017:27017 -v ~/data/db --name theobroma_mongodb mongo:latest #"theobroma_mongodb" é o nome do banco de dados que deve ser acessado por "docker exec -i -t theobroma_mongodb /bin/bash"
docker start theobroma_mongodb
docker run -d -p 4002:4002 --name TheobromaDB mongo:latest
docker start theobroma_mongodb
docker cp install.sh TheobromaDB:/.
docker cp pre-database.sh TheobromaDB:/.
docker cp prep-database.py TheobromaDB:/.
docker cp requeriments.txt TheobromaDB:/.
docker cp website TheobromaDB:/.
docker exec TheobromaDB bash install.sh
bash copy_containers,sh
