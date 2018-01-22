people = 30
cars = 40
trucks = 15

# if cars are greater than people, print line
if cars > people:
    print("We should take the cars.")
# if first is false and cars are less than people, print line
elif cars < people:
    print("We should not take the cars.")
# if first 2 are false, print this
else:
    print("We can't decide.")

# if trucks greater than cars, print line
if trucks > cars:
    print("That's too many trucks.")
# if above false, and trucks are less than cars, print line
elif trucks < cars:
    print("Maybe we could take the trucks.")
# if both above are false, print line
else:
    print("We still can't decide.")

# if people are greater than trucks, print line
if people > trucks:
    print("Alright, let's just take the trucks.")
# if above is false, print line
else:
    print("Fine, let's stay home then.")
