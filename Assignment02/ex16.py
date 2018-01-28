from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do not want that, hit RETURN.")

# input waits for "return" from user
input("?")

# opens file in write mode
print("opening the file...")
target = open(filename, 'w')

# empties file
print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

# three lines we will add to file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# writes each of above lines to file with line break in between
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# closes files
print("And finally, we close it.")
target.close()