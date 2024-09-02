echo ------------------------
cat *.gff > $1
sed '/#/d' $1 > $1.temp
python3 prep-database.py $1
mv $1_temp_mod.gff $1
