echo ---------------------------------------DOCKER-------------------------------------------------------------
docker pull mongo:latest
docker pull ubuntu:latest
docker network create tdb_net -d bridge
docker run -d -p 27017:27017 -v ~/data/db --network tdb_net --name theobroma_mongodb mongo:latest #"theobroma_mongodb" é o nome do banco de dados que deve ser acessado por "docker exec -i -t theobroma_mongodb /bin/bash"
docker start theobroma_mongodb
docker run -d -p 4002:4002 --network tdb_net --name TheobromaDB mongo:latest
docker start theobroma_mongodb
docker cp install.sh TheobromaDB:/.
docker cp pre-database.sh TheobromaDB:/.
docker cp prep-database.py TheobromaDB:/.
docker cp requeriments.txt TheobromaDB:/.
docker cp website TheobromaDB:/.
docker network connect --ip 10.10.36.122 tdb_net theobroma_mongodb
docker network connect --ip 10.10.36.123 tdb_net TheobromaDB
docker exec -d TheobromaDB bash install.sh
bash copy_containers.sh
#docker exec -d TheobromaDB python3 website/website.py
