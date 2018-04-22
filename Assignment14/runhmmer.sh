#!/bin/bash

# check number of input parameters:
if [ $# -ne 3 ]; then
  echo "Wrong number of parameters."
  echo "Usage: runhmmer.sh <query_fasta> <db_fasta> <output_name>"
  exit
fi

export query=$1
export db=$2
export output=$3

# run muscle to generate multiple sequence alignment
/data/hort503_01_s18/jhumann/bin/muscle -in $query -out $query.aln

# run hmmbuild to generate hmm file from muscle alignment file
/data/hort503_01_s18/jhumann/bin/bin/hmmbuild $query.aln.hmm $query.aln

# rum hmmsearch with Drosphilia sequences
/data/hort503_01_s18/jhumann/bin/bin/hmmsearch $query.aln.hmm $db > $output
