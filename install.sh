#!/bin/bash

echo -----------------------------------Instalando dependências------------------------------------------------
apt update -y
apt install python3 -y
apt install python3-pip -y
apt install docker.io -y
pip install -r requeriments.txt
apt install wget -y
apt install curl -y
apt install samtools -y
pip install Bio
pip install pymongo
pip install flask
pip install flask_login
pip install matplotlib
pip install bioinfokit

curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install nodejs -y

wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.15.0/ncbi-blast-2.15.0+-x64-linux.tar.gz
tar -xf ncbi-blast-2.15.0+-x64-linux.tar.gz

echo -------------------------------------Preparando Genomas---------------------------------------------------
mkdir website/static/dados/
mkdir website/static/dados/Criollo_new
cp pre* website/static/dados/Criollo_new/
mkdir website/static/dados/Matina_new
cp pre* website/static/dados/Matina_new/
mkdir website/static/dados/C1074
cp pre* website/static/dados/C1074/
mkdir website/static/blast_db

#BAIXANDO, DESCOMPACTANDO E RENOMEANDO GENOMAS E ANOTAÇÕES
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/403/535/GCA_000403535.1_Theobroma_cacao_20110822/GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/403/535/GCA_000403535.1_Theobroma_cacao_20110822/GCA_000403535.1_Theobroma_cacao_20110822_genomic.gff.gz

wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/208/745/GCF_000208745.1_Criollo_cocoa_genome_V2/GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/208/745/GCF_000208745.1_Criollo_cocoa_genome_V2/GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.gff.gz

wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/036/013/995/GCA_036013995.1_ASM3601399v1/GCA_036013995.1_ASM3601399v1_genomic.fna.gz
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/036/013/995/GCA_036013995.1_ASM3601399v1/GCA_036013995.1_ASM3601399v1_genomic.gff.gz

gunzip GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz
mv GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna Matina.fasta
cp Matina.fasta website/static/dados/Matina_new/.
gunzip GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz
mv GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna Criollo.fasta
cp Criollo.fasta website/static/dados/Criollo_new/.
gunzip GCA_036013995.1_ASM3601399v1_genomic.fna.gz
mv GCA_036013995.1_ASM3601399v1_genomic.fna C1074.fasta
cp C1074.fasta website/static/dados/C1074/.

gunzip GCA_000403535.1_Theobroma_cacao_20110822_genomic.gff.gz
mv GCA_000403535.1_Theobroma_cacao_20110822_genomic.gff Matina.gff
cp Matina.gff website/static/dados/Matina_new/.
gunzip GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.gff.gz
mv GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.gff Criollo.gff
cp Criollo.gff website/static/dados/Criollo_new/.
gunzip GCA_036013995.1_ASM3601399v1_genomic.gff.gz
mv GCA_036013995.1_ASM3601399v1_genomic.gff C1074.gff
cp C1074.gff website/static/dados/C1074/.

#PREPARANDO BANCO DE DADOS DO BLAST
echo ----------------------------------Preparando banco de dados BLAST-----------------------------------------
ncbi-blast-2.15.0+/bin/makeblastdb -in /website/static/dados/Matina_new/Matina.fasta -title Matina_nucl -dbtype nucl -out /website/static/blast_db/Matina_nucl_db
ncbi-blast-2.15.0+/bin/makeblastdb -in /website/static/dados/Criollo_new/Criollo.fasta -title Criollo_nucl -dbtype nucl -out /website/static/blast_db/Criollo_nucl_db
ncbi-blast-2.15.0+/bin/makeblastdb -in /website/static/dados/C1074/C1074.fasta -title C1074_nucl -dbtype nucl -out /website/static/blast_db/C1074_nucl_db

echo ----------------------------------Preparando banco de dados mongo-----------------------------------------

cp pre-database.sh /website/static/dados/Criollo_new/
cp /website/static/dados/Criollo_new/prep-database.py /website/static/dados/Criollo_new/
cp pre-database.sh /website/static/dados/Matina_new/
cp /website/static/dados/Matina_new/prep-database.py /website/static/dados/Matina_new/
cp pre-database.sh /website/static/dados/C1074/
cp /website/static/dados/C1074/prep-database.py /website/static/dados/C1074/

cp Matina.fasta website/static/dados/Matina_new/.
cp Criollo.fasta website/static/dados/Criollo_new/.
cp C1074.fasta website/static/dados/C1074/.

mv Matina.gff website/static/dados/Matina_new/.
cp Criollo.gff website/static/dados/Criollo_new/.
cp C1074.gff website/static/dados/C1074/.

samtools faidx website/static/dados/Criollo_new/Criollo.fasta -o website/static/dados/Criollo_new/Criollo.fasta.fai
bash website/static/dados/Criollo_new/pre-database.sh Criollo
samtools faidx website/static/dados/Matina_new/Matina.fasta -o website/static/dados/Matina_new/Matina.fasta.fai
bash website/static/dados/Matina_new/pre-database.sh Matina
samtools faidx website/static/dados/C1074/C1074.fasta -o website/static/dados/C1074/C1074.fasta.fai
bash website/static/dados/C1074/pre-database.sh C1074


echo ------------------------------------Preparando Jbrowse2--------------------------------------------------
npm install -g @jbrowse/cli
jbrowse add-assembly website/static/dados/Criollo_new/Criollo.fasta --load inPlace
jbrowse add-track website/static/dados/Criollo_new/Criollo.gff --load inPlace
cp config.json website/static/dados/Criollo_new/.
rm config.json

jbrowse add-assembly website/static/dados/Matina_new/Matina.fasta --load inPlace
jbrowse add-track website/static/dados/Matina_new/Matina.gff --load inPlace
cp config.json website/static/dados/Matina_new/.
rm config.json

jbrowse add-assembly website/static/dados/C1074/C1074.fasta --load inPlace
jbrowse add-track website/static/dados/C1074/C1074.gff --load inPlace
cp config.json website/static/dados/C1074/.
rm config.json
