# script from study drill
# adding input to script with argv
from sys import argv
script, eyes, hair, handedness, color = argv
second_color = input("What is my second favorite color? ")

print("This script is:", script)
print("My eye color is:", eyes)
print("My hair color is:", hair)
print("My dominant hand is:", handedness)
print("My favorite color is:", color)
print(f"My second favorite color is {second_color}")
