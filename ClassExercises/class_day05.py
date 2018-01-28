from sys import argv
import math
script, input_file, output_file = argv

def main():
    print("Step 1: Split 2 columns")
    split_values = split_strings(input_file)

    print("Step 2: transform expression value")
    values = log2_transform(split_values)

    # send values to output_file
    with open(output_file, 'w') as file:
        for k, v in values.items():
            file.write(k + '\t' + str(v) + '\n')

    print("All done!")


def split_strings(input):
    split_values = {}
    in_file = open(input, 'r')

    # strips line break and sends file to dictionary. Values are a float number
    for line in in_file.readlines():
        line = line.rstrip("\n")
        line = line.split(sep = "\t")
        split_values[line[0]] = float(line[1])

    return split_values


def log2_transform(values):

    # zeros cannot be log2 transformed, so if value=0 it is skipped
    for k, v in values.items():
        if v <= 0:
            continue
        elif v >= 0 or v != 0:
            values[k] = math.log2(v)

    return values


main()
