"""A python script that processes tabular BLAST output.

..module:: Project03
  :platform: Unix
  :synopsis: This script receives as input BLAST results in the tabular format.
  When using BLAST, this is outfmt=6.  The output is a CSV file that contains 2
  columns.  Column 1 is the Protein Name (query from BLAST) and Column 2 is the
  total number of alignment matches for that protein.

..moduleauthor:: Jodi Humann
"""

from sys import argv
script, tab_file = argv

import numpy as np
import pandas as pd

# Import file and name columns
print("Importing BLAST results")
blast = pd.read_table(tab_file, names=['QueryAccession', 'SubjectAccession',
    'PercentIdentity', 'AlignmentLength', 'NumberMismatch','NumberGaps',
    'StartQuery', 'StopQuery', 'StartSubject', 'EndSubject', 'Evalue',
    'Bitscore'])

# Make new df with just first 2 columns
print("Filtering results")
filteredBlast = blast[['QueryAccession', 'SubjectAccession']]

# Group by SubjectAccession and rename columns
groupedBlast = filteredBlast.groupby('QueryAccession')['SubjectAccession'].count()
groupedBlast2 = groupedBlast.reset_index()
groupedBlast2.columns = ['ProteinName', 'TotalMatchNumber']

# Sort protein list so protein with has highest number of hits at top (descending order)
sortedGroupedBlast = groupedBlast2.sort_values('TotalMatchNumber', ascending=False)

# Output file of results
print("Generating final file")
sortedGroupedBlast.to_csv("sortedBlastResults.txt", sep='\t', index=False)
