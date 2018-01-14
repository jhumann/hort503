name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# unit conversion attempts
height_cm = height * 2.54
weight_kg = weight * 0.45359237
weight_kg_rounded = round(weight * 0.45359237)
print(f"Zed's weight in kilograms would be {weight_kg}.")
print(f"Zed's height in centimeters would be {height_cm}.")
print(f"The weight in kilograms, with the round function would be {weight_kg_rounded}.")
