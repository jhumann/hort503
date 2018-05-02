#!/bin/bash
cat Project03_results/blastOutput/*.txt >> mergedBlastResults
python3 /data/hort503_01_s18/jhumann/Project03/formatBlastResults.py mergedBlastResults

