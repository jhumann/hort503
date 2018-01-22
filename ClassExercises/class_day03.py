from sys import argv

# specify script, imput file and output file
script, in_file, out_file = argv

print(f"This script will copy {in_file} to {out_file}")

indata = open(in_file).read()

outdata = open(out_file, 'w')
outdata.write(indata)

print("Files copied.")
print(f"The input file is {len(indata)} bytes long.")

outdata.close()
