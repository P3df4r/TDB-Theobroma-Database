gt gff3 -sortlines -tidy -retainids $1 > $2-sorted.gff3
bgzip $2-sorted.gff3
tabix $2-sorted.gff3.gz

