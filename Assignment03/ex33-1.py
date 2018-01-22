i = 0
numbers = []

print("Input a end number for range: ")
top_number = int(input())

print("Input the increment: ")
increment = int(input())

while i < top_number:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + increment
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
