# defines function and that 2 arguments need input.
def plants_and_animals(plant_count, animal_count):
    print(f"The park has {plant_count} different examples of flora.")
    print(f"The zoo has {animal_count} different examples of fauna.")
    print("Let's study some biology!\n")


# function arguments are listed directly
print("We can just give the function numbers directly:")
plants_and_animals(20, 30)


# variables are defined and used as input into function below
print("OR, we can use variables from our script:")
flora = 10
fauna = 50

plants_and_animals(flora, fauna)


# uses mathmatical equations as input arguments for function
print("We can even do math inside too:")
plants_and_animals(10 + 20, 5 + 6)


# combines the variables defined above with math as input into function
print("And we can combine the two, variables and math:")
plants_and_animals(flora + 70, fauna + 100)


# have user input numbers
print("We can have the user input the variable numbers.")
print("Enter the number of flora: ")
flora = input()
print("Enter the number of fauna: ")
fauna = input()
plants_and_animals(flora, fauna)
