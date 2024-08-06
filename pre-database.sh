echo ------------------------
cat *.gff > $1
sed '/#/d' $1
python3 prep-database.py $1 > $1.temp
mv $1.temp $1


