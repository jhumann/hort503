#!/bin/bash
#SBATCH --partition=hort503-01-s18
#SBATCH --account=hort503-01-s18
#SBATCH --job-name=TAIR10-IPR
#SBATCH --output=TAIR10-IPR.out
#SBATCH --error=TAIR10-IPR.err
#SBATCH --time=0-00:01:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
module add python3/3.6.5
python3 TAIR10-script.py
