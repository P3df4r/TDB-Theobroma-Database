echo ------------------------
cat *.gff > $1
sed '/#/d' $1
python3 prep-database.py $1 > $1.temp
mv $1.temp $1
docker cp $1 b1959af1d9b9:/data_TDB/$1
echo UPADO
docker exec TheobromaDB bash -c "mongoimport --host=0.0.0.0:27017 --collection='$1' --file=data_TDB/$1 --type=csv --headerline"

