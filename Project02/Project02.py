"""A Python script that extracts SNP variant information from a pileup
file format.  SNPs are selected if the reference base has 10 or more mapped
reads.  Bases from the reads must also have a quality score greater than 30
and there must be at least 3 copies of each variant.

.. module:: Project02
   :platform: Unix
   :synopsis: This script receives as input a pileup file and the base name of
   the output files.  The output files are a tab-delimited file with the SNP
   variant information and a graph of SNP frequency across
   the chromosome.

.. moduleauthor:: Jodi Humann

"""
from sys import argv
script, pileup_file, output_file_prefix = argv

import numpy as np
import pandas as pd
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Import file and name columns
print("Importing pileup file")
pileup = pd.read_table(pileup_file,
    names=['SeqName', 'Pos', 'Base', 'ReadNumber', 'ReadBase', 'QualScore'])

# Filter to keep bases with 10 or more mapped reads
print("Removing bases with less than 10 mapped reads")
G10reads = pileup[pileup['ReadNumber'] > 9]

# remove $ and ^. from ReadBase
print("Removing bases with reads that contain deletion/insertion/skip")
clean_regex = re.compile(r"(\$)|(\^.)", flags=0)
CleanReadBase = G10reads.ReadBase.str.replace(clean_regex, '')
readFilter = pd.concat([G10reads, CleanReadBase], axis=1)
readFilter.columns = ['SeqName', 'Pos', 'Base', '#Reads','ReadBase',
    'QualScore', 'CleanReadBase']

# Filter to remove all reads with insertion/deletion/skip
CleanReads = readFilter[np.invert(
    readFilter.CleanReadBase.str.contains(r'\*|\+|\-|\>|\<'))]

# Convert ASCII characters and calculate the quality score
print("Filtering bases by quality score greater or equal to 30")
QualScoreSplit = CleanReads.QualScore.apply(lambda x: list(x))
def convertQual(x):
    qual_score_ord = [ord(i) for i in x]
    qual_score_num = [(i - 33) for i in qual_score_ord]
    return qual_score_num
QualScoreNum = QualScoreSplit.apply(convertQual)

# Filter bases from CleanReadBase and QualScore that have quality score < 30
BaseSplit = CleanReads.CleanReadBase.apply(lambda x: list(x))
CleanQual = pd.concat([BaseSplit, QualScoreNum], axis=1)

def sortBase(x, y):
    QualScore = [x]
    CleanQualScore = []
    CleanReadBase = [y]
    SortedBase = []

    for i in range(0, len(x)):
        if x[i] >= 30:
            CleanQualScore.append(x[i])
            SortedBase.append(y[i])
        elif x[i] < 30:
            continue
    return pd.Series([CleanQualScore, SortedBase])

CleanQual2 = CleanQual.apply(lambda x: sortBase(x['QualScore'],
    x['CleanReadBase']), axis=1)
CleanQual2.columns = ['CleanQualScore', 'CleanReadBase']
CleanQual3 = CleanQual2.CleanReadBase.apply(lambda x: ''.join(x))

# Add filtered bases to dataframe
CleanReads2 = pd.concat([CleanReads, CleanQual3], axis=1)
CleanReads2.columns = ['SeqName', 'Pos', 'Base', '#Reads','ReadBase',
    'QualScore', 'CleanReadBase', 'CleanReadBaseSort']

# count variants and total bases and add as series
print("Counting SNP variants")
match_count = CleanReads2.CleanReadBaseSort.str.count(r'\.|,')
Aa_count = CleanReads2.CleanReadBaseSort.str.count(r'A|a')
Tt_count = CleanReads2.CleanReadBaseSort.str.count(r'T|t')
Cc_count = CleanReads2.CleanReadBaseSort.str.count(r'C|c')
Gg_count = CleanReads2.CleanReadBaseSort.str.count(r'G|g')
CleanReads3 = pd.concat([CleanReads2, match_count, Aa_count, Tt_count,
    Cc_count, Gg_count], axis=1)
CleanReads3.columns = ['SeqName', 'Pos', 'Base', '#Reads','ReadBase',
    'QualScore', 'CleanReadBase', 'CleanReadBaseSort', 'matchCount',
    'A', 'T', 'C', 'G']

# remove series I don't need anymore and melt and sort table
print("Generating table with SNP calls, keeping SNPs with 3 or more copies")
finalTable = CleanReads3[['SeqName', 'Pos', 'Base', '#Reads', 'A', 'T',
    'C', 'G']]
finalTableMelt = pd.melt(finalTable, id_vars=['SeqName', 'Pos', 'Base',
    '#Reads'], value_vars=['A', 'T', 'C', 'G'], value_name='SNPcount')
finalTableMelt2 = finalTableMelt.sort_values(['Pos'])
finalTableMeltSort = finalTableMelt2[finalTableMelt2['SNPcount'] >= 3]

# calculate frequency of variant and add as series
print("Calculating SNP variant frequency")
Freq = finalTableMeltSort.SNPcount.divide(finalTableMeltSort['#Reads'])
withFreq = pd.concat([finalTableMeltSort, Freq], axis=1)
withFreq.columns = ['SeqName', 'Pos', 'Base', '#Reads','variable',
    'SNPcount', 'Freq']

# remove all series I don't need in final table
print("Generating final table and creating file")
ReallyFinalTable = withFreq[['SeqName', 'Pos', 'Base', 'variable', 'Freq']]
ReallyFinalTable.columns = ['SeqName', 'Position', 'Base', 'Variant',
    'Frequency']

# Generate tab-delimited output file
TableFilename = (f"{output_file_prefix}.txt")
ReallyFinalTable.to_csv(TableFilename, sep='\t', index=False)

# Generate graph and output to file
print("Generating final graph")
GraphFilename = (f"{output_file_prefix}.png")
graph = ReallyFinalTable.plot(x= 'Position', y= 'Frequency', kind='bar',
    figsize= (20,7), title='SNP Variant Frequency', legend=False, rot=90)

spacing = 100
visible = graph.xaxis.get_ticklabels()[::spacing]
for label in graph.xaxis.get_ticklabels():
    if label not in visible:
        label.set_visible(False)

plt.savefig(GraphFilename, dpi=300)
