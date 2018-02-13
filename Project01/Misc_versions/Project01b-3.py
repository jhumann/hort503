"""A Python script that performs simple read trimming of a FASTQ file.

.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.

.. moduleauthor:: Jodi Humann

"""
from sys import argv
script, input_fq, output_fq, min_qual_score, min_read_len = argv

def get_read(fq):
    """Extract a single read from a FASTQ file.

    Reads in a FASTQ file are stored in 4 lines that contain the
    sequence_id, nucleotide sequence, a second id, and a series of
    characters represeting quality scores.

    :param fq: A file handle for the FASTQ file
    :type fq: An io.TextIOBase object (created using the open() function).

    :return: a list containing 4 strings: the sequence ID, nucleotide sequence,
        second ID, and the quality score sequence. If there are no more
        sequences in the FASTQ file then this function returns False.
    :rtype: a list with four elements
    """

    with open(fq, 'r') as f:
        fq_list = [line.strip() for line in f]
        for line in fq_list:
            if ('@cluster' in line):
                single_rd = [fq_list.pop(0), fq_list.pop(0), fq_list.pop(0), fq_list.pop(0)]
                #print(single_read)
                return single_rd
            else:
                False

        #print(single_read)
        #return single_read

def trim_read_front(read, min_q, min_size):
    """Trims the low quality nucleotides from the front of a reads' sequences.

    This function examines the quality score of each nucleotide sequence
    starting from the first position of the sequence. When it encouters a
    high quality score it stops trimming and returns an updated read.

    :param read: A list containing for elements in this order: the sequence ID,
        the nucleotide sequence string, a secondary identifier string, and a
        quality score string.
    :type read: a list

    :param min_q:  The minimum quality score that a nucleotide must have to
        not be trimmed (e.g. 30).
    :type min_q:  integer

    :param min_size:  The minimum size that the sequence must have after
        trimming to keep the read (e.g. 30).
    :type min_size: integer

    :return: a list just like the the get_read() function returns but with the
       low-quality reads (and corresponding quality scores) trimmed off the
       front of the string. If the remaining trimmed read is smaller than the
       desired minimum read length then this function returns False.
    :rtype: a list with four elements
    """
# separate out items from input read list
    name = read[0]
    seq = read[1]
    #seq_len = len(seq)
    #print(seq_len)
    divider = read[2]
    qual_score = read[3]
    qual_len = len(qual_score)
# convert ASCII values to numbers and calulate qual score
    qual_score_ord = [ord(i) for i in qual_score]

    #print(qual_len)
    qual_score_num = [(i - 33) for i in qual_score_ord]
    #print(qual_score_num)
    i = qual_score_num[0]

# how do I get these to work with the if statements????
    min_qual = int(min_q)
    min_len = int(min_size)

# for qual_score_num, trim of low quality bases from beginning
    if qual_score_num[i] < 30:
        qual_score_num.remove(i)
    elif qual_score_num[i] >= 30:
        False

# determine how many bases were trimmed and trim seq and qual_score strings
    #print(qual_score_num)
    trim_len = len(qual_score_num)
    #print(trim_len)
    bases_rm = qual_len - trim_len
    #print(bases_rm)
    trim_seq = seq[bases_rm:]
    #print(trim_seq)
    trim_qual = qual_score[bases_rm:]
    #print(trim_qual)

# return trimmed read if length is greater than min_size
    if trim_len >= 30:
        clean_read_F = [name, trim_seq, divider, trim_qual]
        #print(clean_read_F)

    return clean_read_F

#
# The main function for the script.
#
def main(argv):
    """The main function of this script.

    After trimming is completed, the fucntion prints out three status lines. The
    first indicates the total number of reads that were found. The second
    indicates how many reads were removed for being too short after trimming and
    the third indicates how many reas were trimmed and kept.

    The script will create a new FASTQ file of just the trimmed reads and name
    it according to the argument provided by the user when running the script.

    :param argv:  The incoming arguments to this script as
       provided by the sys.argv variable.  There must be four total arguments
       provided to the script must be in the following order

       - The filename for the input FASTQ file
       - The filename for the new output FASTQ file that this script creates
       - An integer for the minimum quality score. Anything below this at the
         beginning of each read's nucleotide sequence is trimmed off.
       - An integer indicating how large a read's nucleotide sequence must
         be after trimming in order to keep it.
    """
    fq = input_fq
    filtered_fq = output_fq
    min_q = int()
    min_size = int()


    print(f"Opening {fq} for reading...")
# calculate stats for old and new file
    in_f = open(fq, 'r').read()
    input_count = in_f.count('@cluster')
    print(f"Opening {filtered_fq} for writing...")

    start = 0
    end = input_count
    step = 1
    while start <= end:
    #for x in range(0, end):
        single_read = get_read(fq)
        clean_read_F = trim_read_front(single_read, min_q, min_size)
        final_read = '\n'.join(clean_read_F)
        #print(final_read)
        # write trimmed reads to file
        with open(filtered_fq, 'a+') as file:
            file.write(final_read + '\n')
        start += step

# calculate stats for old and new file
    print(f"{input_count} reads were found")

    out_f = open(filtered_fq, 'r').read()
    output_count = out_f.count('@cluster')
    removed = input_count - output_count
    print(f"{removed} reads were removed")
    print(f"{output_count} reads were trimmed and kept")
    print("Done.")


# Begin the program by calling the main function.
main(argv)
