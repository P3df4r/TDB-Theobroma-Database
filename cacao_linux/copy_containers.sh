docker cp tdb_docker:/home/ubuntu/Criollo/Criollo tdb_mongo:/data_TDB/.
docker cp tdb_docker:/home/ubuntu/Matina/Matina tdb_mongo:/data_TDB/.
docker cp tdb_docker:/home/ubuntu/C1074/C1074 tdb_mongo:/data_TDB/.
docker exec tdb_mongo bash -c "mongoimport --host=0.0.0.0:27017 --collection='Criollo' --file=data_TDB/Criollo --type=csv --headerline"
docker exec tdb_mongo bash -c "mongoimport --host=0.0.0.0:27017 --collection='Matina' --file=data_TDB/Matina --type=csv --headerline"
docker exec tdb_mongo bash -c "mongoimport --host=0.0.0.0:27017 --collection='C1074' --file=data_TDB/C1074 --type=csv --headerline"

