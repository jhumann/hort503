#!/bin/bash
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=runhmmer
#SBATCH --output=runhmmer.out
#SBATCH --error=runhmmer.err
#SBATCH --time=0-24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
/data/hort503_01_s18/jhumann/HMMER/runhmmer.sh $1 $2 $3
