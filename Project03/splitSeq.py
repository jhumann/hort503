"""A Python script that spits large fasta files into files contianing 5000 
sequences or less to decrease run time in downstream analysis tools.

.. module:: Project03
   :platform: Unix
   :synopsis: This script receives as input a fasta file.  The output files 
   are multiple fasta files.
   :dependent python packages: numpy, biopython
   
.. moduleauthor:: Jodi Humann and mostly Dr. Google
"""
from sys import argv
script, input_fasta = argv

from Bio import SeqIO

def batch_iterator(iterator, batch_size):
    entry = True  # Make sure we loop once

    while entry:
        batch = []

        while len(batch) < batch_size:
            try:
                entry = next(iterator)
            except StopIteration:
                entry = False

            if not entry:
                # End of file
                break

            batch.append(entry)

        if batch:
            yield batch

record_iter = SeqIO.parse(input_fasta, 'fasta')

# Splits fasta file into smaller files containing 5000 sequences or less
for i, batch in enumerate(batch_iterator(record_iter, 5000), start=1):
    filename = 'group_{}.fasta'.format(i)
    count = SeqIO.write(batch, filename, 'fasta')
    print('Wrote {} records to {}'.format(count, filename))