Nextflow script: 'Project03.nf'

BASH script: 'ReformatBlast.sh'

Pipeline author: Jodi Humann


The purpose of this Nextflow pipeline and BASH script is to take a large fasta file of 
protein sequences, divide it into smaller files, identify protein homologs using 
protein BLAST, and output a file indicating the number of matches for each input 
protein sequence.

This Nextflow pipeline contains two processes.  

1.) Python script called 'splitSeq.py' that will divide a larger fasta file
    into smaller chunks of 5000 sequences or less. 

2.) Protein BLAST to identify protein homologs from the SwissProt protein database 
    using an evalue cutoff of 1e-6.  The BLAST results are returned in a tabular 
    format. 

The BASH script run after the Nextflow pipeline contains two processes.

1.) A simple 'cat' command to combine the BLAST output files into a single file for 
    the next step.

2.) Python script called 'formatBlastResults.py' that determines the number of protein 
    alignment matches per input query sequence. The results are returned as a CSV file.

The Nextflow results are returned in a directory that is created in the location the 
pipeline is initiated from.  The parent directory is called 'Project03_results'.  There 
are two sub-directories; 'splitSeq' and 'blastOutput' that correspond to the above 
processes, respectively.


To run this pipeline on the Kamiak HPC at WSU:

Before running script, make sure these python3 packages are installed using these 
commands:

  module load python3
  python3 -m pip install --user numpy biopython pandas


Load the following modules in order to run Nextflow with these commands:

  module use /data/ficklin/moduleFiles
  module add java nextflow


The Nextflow pipeline has been designed to run using the SLURM scheduler. The pipeline 
script is called 'Project03.nf' and correponding configuration file is called 
'nextflow.config'. The path to the 'splitSeq.py' Python script is specified in 
'Project03.nf'.

To run the Nextflow pipeline, you will need to specify the location of the input peptide 
FASTA file as an '--input' variable.  Here is the command to submit to the SLURM queue.

  sbatch nextflow run Project03.nf --file /data/hort503_01_s18/example-data/all.pep

The "--file" option can be changed to use any protein FASTA file.

Once the Nexflow pipline has completed, run the 'ReformatBlast.sh' script from 
the same directory used for the Nextflow pipeline (that way script can see the 
'Project_03-results' directory).  The path to the Python script 
'formatBlastResults.py' is already specified in the BASH script.

  ./ReformatBlast.sh

Two files will be generated.  'mergedBlastResults', which has all the BLAST output 
combined into a single file, and the final output file called 'sortedBlastResults.txt'.





