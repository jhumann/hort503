from sys import argv

# imported arguments
script, input_file = argv

# function to read and print file to screen
def print_all(f):
    print(f.read())

# function to reset to beginning of file, position 0 byte
def rewind(f):
    f.seek(0)

# function to print the line from the file, with the line number before it
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = '')

# assigns variable to opened input file from entered arguments
current_file = open(input_file)

# prints text with new line after
print("First let's print the whole file:\n")

# uses print_all function above to print contents of file to screen
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# uses rewind functon to move to very beginning of file
rewind(current_file)

print("Let's print three lines:")

# specifies current_line number and then uses print_a_line function to print line number and string of line content
current_line = 1
print_a_line(current_line, current_file)

# same as above, but line number is now 2 (line 1 + 1)
current_line += 1
print_a_line(current_line, current_file)

# same as above, but line number is now 3 (line 2 + 1)
current_line += 1
print_a_line(current_line, current_file)
