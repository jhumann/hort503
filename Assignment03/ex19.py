# defines function and that 2 arguments need input.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# function arguments are listed directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# variables are defined
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# inputs variables defined above into function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# uses mathmatical equations as input arguments for function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


# combines the variables defined above with math as input into function
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
