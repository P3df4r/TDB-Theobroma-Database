#!/bin/bash

echo -----------------------------------Instalando dependências------------------------------------------------
apt update
apt install python3
apt install python3-pip
apt install docker.io
pip install -r requeriments.txt
apt install wget


wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.15.0/ncbi-blast-2.15.0+-x64-linux.tar.gz
tar -xf ncbi-blast-2.15.0+-x64-linux.tar.gz

#wget https://github.com/nodejs/node/archive/refs/heads/main.zip
#unzip main.zip
#cd node-main
#./configure
#make
#make install
#cd ..

echo ---------------------------------------DOCKER-------------------------------------------------------------
docker pull mongo:latest
#docker network create tdb_brige
#docker build . --tag tdb_docker --progress=auto --network tdb_bridge
#docker exec -i -t tdb_docker "/bin/bash"
#cd ./website
#nohup python3 website.py &
#exit
#docker run -d -p 27017:27017 -v ~/data/db --network tdb_bridge --name theobroma_mongodb mongo:latest #"theobroma_mongodb" é o nome do banco de dados que deve ser acessado por "docker exec -i -t theobroma_mongodb /bin/bash"
docker run -d -p 27017:27017 -v ~/data/db --name theobroma_mongodb mongo:latest

echo -------------------------------------Preparando Genomas---------------------------------------------------

mkdir ../website/static/dados/
mkdir ../website/static/dados/Criollo_new
cp pre* ../website/static/dados/Criollo_new/
cp headfix.txt ../website/static/dados/Criollo_new/
mkdir ../website/static/dados/Matina_old
cp pre* ../website/static/dados/Matina_old/
cp headfix.txt ../website/static/dados/Matina_old/
mkdir ../website/static/dados/C1074
cp pre* ../website/static/dados/C1074/
cp headfix.txt ../website/static/dados/C1074/
mkdir ../website/static/blast_db

#BAIXANDO, DESCOMPACTANDO E RENOMEANDO GENOMAS E ANOTAÇÕES
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/403/535/GCA_000403535.1_Theobroma_cacao_20110822/GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/403/535/GCA_000403535.1_Theobroma_cacao_20110822/GCA_000403535.1_Theobroma_cacao_20110822_genomic.gff.gz

wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/208/745/GCF_000208745.1_Criollo_cocoa_genome_V2/GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/208/745/GCF_000208745.1_Criollo_cocoa_genome_V2/GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.gff.gz

wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/036/013/995/GCA_036013995.1_ASM3601399v1/GCA_036013995.1_ASM3601399v1_genomic.fna.gz
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/036/013/995/GCA_036013995.1_ASM3601399v1/GCA_036013995.1_ASM3601399v1_genomic.gff.gz

gunzip GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz
mv GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna Matina.fasta
mv Matina.fasta ../website/static/dados/Matina_old
gunzip GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz
mv GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna Criollo.fasta
mv Criollo.fasta ../website/static/dados/Criollo_new
gunzip GCA_036013995.1_ASM3601399v1_genomic.fna.gz
mv GCA_036013995.1_ASM3601399v1_genomic.fna C1074.fasta
mv C1074.fasta ../website/static/dados/C1074

gunzip GCA_000403535.1_Theobroma_cacao_20110822_genomic.gff.gz
mv GCA_000403535.1_Theobroma_cacao_20110822_genomic.gff Matina.gff
mv Matina.gff ../website/static/dados/Matina_old
gunzip GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.gff.gz
mv GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.gff Criollo.gff
mv Criollo.gff ../website/static/dados/Criollo_new
gunzip GCA_036013995.1_ASM3601399v1_genomic.gff.gz
mv GCA_036013995.1_ASM3601399v1_genomic.gff C1074.gff
mv C1074.gff ../website/static/dados/C1074

#PREPARANDO BANCO DE DADOS DO BLAST
echo ----------------------------------Preparando banco de dados BLAST-----------------------------------------
ncbi-blast-2.15.0+/bin/makeblastdb -in ../website/static/dados/Matina_old/Matina.fasta -title Matina_nucl -dbtype nucl -out ../website/static/blast_db/Matina_nucl_db
ncbi-blast-2.15.0+/bin/makeblastdb -in ../website/static/dados/Criollo_new/Criollo.fasta -title Criollo_nucl -dbtype nucl -out ../website/static/blast_db/Criollo_nucl_db
#ncbi-blast-2.15.0+/bin/makeblastdb -in ./website/static/dados/C174P/C174P.fasta -title C174P_nucl -dbtype nucl -out ./website/static/blast_db/C174P_nucl_db
#ncbi-blast-2.15.0+/bin/makeblastdb -in ./website/static/dados/C174/C174.fasta -title C174_nucl -dbtype nucl -out ./website/static/blast_db/C174_nucl_db
#ncbi-blast-2.15.0+/bin/makeblastdb -in ./website/static/dados/C1074P/C1074P.fasta -title C1074P_nucl -dbtype nucl -out ./website/static/blast_db/C1074P_nucl_db
ncbi-blast-2.15.0+/bin/makeblastdb -in ../website/static/dados/C1074/C1074.fasta -title C1074_nucl -dbtype nucl -out ../website/static/blast_db/C1074_nucl_db

echo ----------------------------------Preparando banco de dados mongo-----------------------------------------

cp pre-database.sh Criollo_new/
cp prep-database.py Criollo_new/
cp pre-database.sh Matina_old/
cp prep-database.py Matina_old/
cp pre-database.sh C1074/
cp prep-database.py C1074/
#mkdir ./website/static/dados/C1074P/prep_db
#mkdir ./website/static/dados/C174/prep_db
#mkdir ./website/static/dados/C174P/prep_db

cd ../website/static/dados/Criollo_new/
bash pre-database.sh Criollo
cd ../Matina_old/
bash pre-database.sh Matina
cd ../C1074/
bash pre-database.sh C1074
#cd ../C1074P
#bash ../../../pre-database.sh C1074P
#cd ../C174
#bash ../../../pre-database.sh C174
#cd ../C174P
#bash ../../../pre-database.sh C174P
cd ../



echo ------------------------------------Preparando Jbrowse2--------------------------------------------------
npm install -g @jbrowse/cli
cd Criollo_new
cp jbrowse add-assembly Criollo.fasta --load inPlace
cd ../Matina_old
cp jbrowse add-assembly Matina.fasta --load inPlace
cd ../C1074
cp jbrowse add-assembly C1074.fasta --load inPlace
#cp C1074P/C1074P.fasta . | jbrose add-assembly C1074P.fasta --load inPlace
#cp C174/C174.fasta . | jbrowse add-assembly C174.fasta --load inPlace
#cp C174P/C174P.fasta . | jbrowse add-assembly C174P.fasta --load inPlace

python3 ../website/website.py
