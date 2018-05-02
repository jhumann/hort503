params.file = '*.fa'
input_fasta = Channel.fromPath( params.file )
sprot_db = Channel.fromPath( '/data/hort503_01_s18/example-data/swissprot' )

process split_seq {

//  module "python3"
  publishDir "Project03_results/splitSeq", mode: "copy"

  input:
    file input_fa from input_fasta
  output:
    file '*.fasta' into split_files mode flatten

  """
    python3 /data/hort503_01_s18/jhumann/Project03/splitSeq.py ${input_fa}
  """
}

process blastp {

//  module "blast"
  publishDir "Project03_results/blastOutput", mode: "copy"

  input:
    file input_file from split_files
  output:
    file '*.txt' into blast_results mode flatten

  """
    blastp -query ${input_file} -db /data/hort503_01_s18/example-data/swissprot -num_threads ${task.cpus} -outfmt 6 -evalue 1e-6 -out ${input_file}.txt
  """
}

/*
process mergeResults {

  publishDir "Project03_results/combinedResults", mode: "copy"

  input:
    file results from blast_results
  output:
    file 'mergedBlast.txt' into blast_merge

  """
  cat ${results} >> mergedBlast.txt
  """
}

process reformatResults {

// module "python3"
  publishDir "Project03_results/finalResult", mode: "copy"

  input:
    file merged from blast_merge
  output:
    file 'sortedBlastResults.txt' into final_result

  """
  python3 /data/hort503_01_s18/jhumann/Project03/formatBlastResults.py ${merged}
  """
}
*/
