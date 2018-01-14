print("I will now count my chickens:")

# For Hens, (30/6) calculated first then added to 25 to get 30
print("Hens", 25 + 30/ 6)
# For Roosters, (25*3)=75mod4=18x4=72, with a remainder of 3, 100-3=97
print("Rooster", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

# 4mod2=0, 1/4=.25 so the equation is 1+0-0.25+6=6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

# returns true or false in relation to less-than symbol
print(3 + 2 < 5 - 7)

# After the text prints, math calculated and printed
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print ("How about some more.")

# Text prints and then true/false prints
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
