def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

# specify variables and input numbers for functions, numbers are print by functions
age = add(30, 11)
height = subtract(78, 12)
weight = multiply(95, 2)
iq = divide(100, 1)

# prints out results of functions as listed variables
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, divide(weight, subtract(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
