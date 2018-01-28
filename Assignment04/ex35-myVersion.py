from sys import exit

# room accessed from bear_room
def gold_room():
    print("This room is full of gold.  How much do you take?")

# prompts user to enter number (integer)
    choice = int(input("> "))

# if number is less than 50, if statement.  If 50 or over, else statement
    if choice < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

# left room, directed from start function to here
def bear_room():
    print("""
    There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?

    'take honey' or 'taunt bear'?""")
    bear_moved = False

    while True:
        choice = input("> ")

        # else is an endless loop, does not go to dead function
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("""
    The bear has moved from the door.
    You can go through it now.

    'open door' or stay and 'tickle bear'?""")
            bear_moved = True
        elif choice == "tickle bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            dead("I got no idea what that means. You don't deserve to play anymore.")

# right room, directed from start function
def cthulhu_room():
    print("""
    Here you see the great evil Cthulhu.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or eat your head?

    'flee' or 'head' or 'His choice'?""")

    choice = input("> ")

    # flee sends user back to start, head terminates game, other answer sends back to room
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# dead function that terminates program...when user screws up
def dead(why):
    print(why, "Good job!")
    exit(0)

# main function that starts game
def start():
    print("""
    You are in a dark room.
    There is a door to your right and left.
    Which one do you take?

    'left' or 'right' or 'none'?""")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
