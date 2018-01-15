from sys import argv
from os.path import exists

# specifies script, input file and output file names
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# Reduced command to one line
indata = open(from_file).read()

# opens file in write mode
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# closes out file
out_file.close()
