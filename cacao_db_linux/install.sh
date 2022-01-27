#!/bin/bash

#Instala dependencias
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
echo ----------------------------Instalando Sequenceserver----------------------------------------
sudo gem install sequenceserver
echo ------------------------------Preparando Genomas-----------------------------------------------

#Baixa os FASTA
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/208/745/GCF_000208745.1_Criollo_cocoa_genome_V2/GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz -P ../website/static/jbrowse2/
gunzip ../website/static/jbrowse2/CF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna.gz
mv ../website/static/jbrowse2/GCF_000208745.1_Criollo_cocoa_genome_V2_genomic.fna ../website/static/jbrowse2/treeNC_030850.1.fa
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/403/535/GCA_000403535.1_Theobroma_cacao_20110822/GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz -P ../website/static/jbrowse2/
gunzip ../website/static/jbrowse2/GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna.gz
mv ../website/static/jbrowse2/GCA_000403535.1_Theobroma_cacao_20110822_genomic.fna ../website/static/jbrowse2/treeCM001879.1.fa
