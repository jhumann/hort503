from sys import argv

# tells what arguments need input on command line
script, filename = argv

# creates variable that opens a file
txt = open(filename)

# Prints the file name
print(f"Here's your file {filename}:")
#prints the contents of the file specified in 'txt'
print(txt.read())

# prompts user to enter file name again
print("Type the filename again:")
file_again = input("> ")

# creates variable from user input name at prompt that opens the file (again)
txt_again = open(file_again)

# prints file contents again
print(txt_again.read())
