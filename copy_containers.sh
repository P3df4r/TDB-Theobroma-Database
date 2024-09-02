docker cp TheobromaDB:website/static/Criollo_new/Criollo .
docker cp Criollo theobroma_mongodb:/data_TDB/.
docker cp TheobromaDB:Matina .
docker cp website/static/Matina_old/Matina theobroma_mongodb:/data_TDB/.
docker cp TheobromaDB:website/static/C1074/C1074 .
docker cp C1074 theobroma_mongodb:/data_TDB/.
docker exec theobroma_mongodb bash -c "mongoimport --host=0.0.0.0:27017 --collection='Criollo' --file=data_TDB/Criollo --type=csv --headerline"
docker exec theobroma_mongodb bash -c "mongoimport --host=0.0.0.0:27017 --collection='Matina' --file=data_TDB/Matina --type=csv --headerline"
docker exec theobroma_mongodb bash -c "mongoimport --host=0.0.0.0:27017 --collection='C1074' --file=data_TDB/C1074 --type=csv --headerline"

