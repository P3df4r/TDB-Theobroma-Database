#!/bin/bash

#Instalando dependencias
echo 
-----------------------------Instalando Python3--------------------------------------------
sudo apt-get install python3
echo -----------------------------Instalando Biopython--------------------------------------------
sudo pip install biopython
echo -----------------------------Instalando Blast------------------------------------------------
sudo apt-get install ncbi-blast+
echo -----------------------------Instalando Flask------------------------------------------------
sudo pip install Flask
echo ----------------------------Instalando Matplotlib--------------------------------------------
sudo pip install matplotlib
echo -----------------------------Instalando Ruby-------------------------------------------------
sudo apt-get install ruby-full
#echo ----------------------------Instalando Sequenceserver----------------------------------------
#sudo gem install sequenceserver
echo ----------------------------Instalando Login----------------------------------------
sudo pip install flask-login
echo -----------------Permissões Clustalw2-----------------
cd clustalW
chmod +x clustalw2
cd ../
echo ------------------------------Preparando Genomas-----------------------------------------------

#Baixando fasta de DNA
#Criollo
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/208/745/GCF_000208745.1_Criollo_cocoa_genome_V2/GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz
cp GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz ../website/static/jbrowse2/
cp GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz ../website/genomas/
gunzip GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz
mv GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna Criollo.fasta
mv Criollo.fasta ../website/genomas/
gunzip ../website/static/jbrowse2/GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz
mv ../website/static/jbrowse2/GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna ../website/static/jbrowse2/treeNC_030850.1.fa
#Matina
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/403/535/GCA_000403535.1_Theobroma_cacao_20110822/GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz
cp GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz ../website/static/jbrowse2/
cp GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz ../website/genomas
gunzip GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz
mv GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna Matina.fasta
mv Matina.fasta ../website/genomas/
gunzip ../website/static/jbrowse2/GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz
mv ../website/static/jbrowse2/GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna ../website/static/jbrowse2/treeCM001879.1.fa
#Baixando fasta de proteina
#Criollo
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/208/745/GCF_000208745.1_Criollo_cocoa_genome_V2/GCF_000208745.1_Criollo_cocoa_genome_V2_protein.faa.gz
gunzip GCF_000208745.1_Criollo_cocoa_genome_V2_protein.faa.gz
mv GCF_000208745.1_Criollo_cocoa_genome_V2_protein.faa Criollo.faa
mv Criollo.faa ../website/genomas/
#Matina
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/403/535/GCA_000403535.1_Theobroma_cacao_20110822/GCA_000403535.1_Theobroma_cacao_20110822_protein.faa.gz
gunzip GCA_000403535.1_Theobroma_cacao_20110822_protein.faa.gz
mv GCA_000403535.1_Theobroma_cacao_20110822_protein.faa Matina.faa
mv Matina.faa ../website/genomas/

#Criação do makeblastdb
echo ------------------------------Criando banco de dados-------------------------------
cd ../website/genomas/
mkdir Criollo
mkdir Matina
mv Criollo.fasta Criollo/
mv Criollo.faa Criollo/
mv Matina.fasta Matina/
mv Matina.faa Matina/
cd Criollo/
makeblastdb -in Criollo.fasta -title Criollo_nucl -dbtype nucl -out Criollo_nucl_db
makeblastdb -in Criollo.faa -title Criollo_prot -dbtype prot -out Criollo_prot_db
cd ../Matina/
makeblastdb -in Matina.fasta -title Matina_nucl -dbtype nucl -out Matina_nucl_db
makeblastdb -in Matina.faa -title Matina_prot -dbtype prot -out Matina_prot_db
cd ..
#echo Iniciando sequence server
#sequenceserver -s -d Criollo/Criollo_nucl_db
echo -------------------------------Iniciando website-----------------------------
cd ..
pwd
python3 website.py
