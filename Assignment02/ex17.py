from sys import argv
from os.path import exists

# specifies script, input file and output file names
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# 'len' reports the size on the input file
print(f"The input file is {len(indata)} bytes long")

# 'exists' reports if file already exists with a True/False
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# opens file in write mode
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# closes both files
out_file.close()
in_file.close()
