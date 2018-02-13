"""A Python script that performs simple read trimming of a FASTQ file.

.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.

.. moduleauthor:: Jodi Humann (with help from Tyler Biggs)

"""
from sys import argv
script, input_fq, output_fq, min_qual_score, min_read_len = argv

#
# function that retrieves single sequence and return it as list
#
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

# set out_list as a list
    out_list = list()

# strip the first 4 lines from file, remove /n, add to out_list
    for i in range(4):
        out_list.append(fq.readline().rstrip())

# return read from out_list
    return out_list

#
# function that trims 5' end by quality and filters out short sequences
#
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
    seq = list(read[1])
    divider = read[2]
    qual_score = list(read[3])

# convert ASCII values to numbers and calulate qual score
    qual_score_ord = [ord(i) for i in qual_score]
    qual_score_num = [(i - 33) for i in qual_score_ord]

# trim seq and qual_score by min_q
    for qual_numb in qual_score_num:
        if qual_numb < min_q:
            del seq[0]
            del qual_score[0]
        elif qual_numb >= min_q:
            break

# only return sequences min_size and longer
    if len(seq) < min_size:
        return False

# convert trimmed seq and qual_score to strings and return 4 item list for each read
    clean_read_F = [name, ''.join(seq), divider, ''.join(qual_score)]
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

# define the inputs from the argv
    fq = input_fq
    filtered_fq = output_fq
    min_q = int(min_qual_score)
    min_size = int(min_read_len)

# open and calculate number of reads for input file
    print(f"Opening {fq} for reading...")
    in_f = open(fq, 'r').read()
    input_count = in_f.count('@cluster')

# start processing reads
    print(f"Opening {filtered_fq} for writing...")

# specify the number of times the process needs to repeat
    start = 0
    end = input_count
    step = 1

# retrieve a sequence, trim it and add to filtered_list if it passes inspection
    with open(fq, 'r') as f:
        filtered_list = list()

        while start <= end:
            single_read = get_read(f)
            clean_read_F = trim_read_front(single_read, min_q, min_size)

            if not clean_read_F:
                start += step
                continue

            filtered_list.append(clean_read_F)
            start += step

# write trimmed reads to file with /n between lines
    with open(filtered_fq, 'w+') as f:
        for x in filtered_list:
            f.write('\n'.join(x))
            f.write('\n')

# print stats for output file
    print(f"{input_count} reads were found")

# calculate stats for output file
    out_f = open(filtered_fq, 'r').read()
    output_count = out_f.count('@cluster')

# calculate how many reads were removed and how many kept
    removed = input_count - output_count
    print(f"{removed} reads were removed")
    print(f"{output_count} reads were trimmed and kept")
    print("Done.")

#
# begin the program by calling the main function.
#
main(argv)
