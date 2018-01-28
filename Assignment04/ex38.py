ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list.  Let's fix that.")

# converts string into list, list of more items to add
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

# checks length of stuff and adds items from more_stuff until 10 is reached
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) # prints item in position 1
print(stuff[-1]) # prints last item
print(stuff.pop()) # pops off last item on list
print(' '.join(stuff)) # prints list as one string, minus corn
print('#'.join(stuff[3:5])) # prints items 3 and 4 with # in middle
