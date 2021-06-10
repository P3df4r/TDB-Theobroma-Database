#!/bin/bash

echo Criando banco de dados
echo Digite um nome para o banco de dados
read nome
echo Digite o nome do arquivo
read fasta
mkdir $nome
mv $fasta $nome
cd $nome
pwd
makeblastdb -dbtype nucl -title $nome -in $fasta
cd ..
echo Iniciando sequence server
sequenceserver -s -d $nome
echo Iniciando website
cd ..
cd website
pwd
python3 website.py

