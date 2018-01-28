from sys import exit

def start():
    print("""
    You are the famous archeologist, Indiana Jones.
    You just have stumbled upon the entrance to a
    hidden tomb deep in the jungle.
    Maybe you will find a treasure...and some adventure!
    You enter the tomb and there are three hallways.

    Do you go 'left' or 'right' or 'straight'?""")

    choice = input("> ")

    if choice == "left":
        test_1()
    elif choice == "right":
        test_3()
    elif choice == "straight":
        test_2()
    else:
        dead("I guess you chickened out and left the tomb.")


def test_1():
    print("""
    You come upon a room full of snakes.
    Yeah, yeah...you hate snakes.
    There is a very, very large cobra staring at you and he says:

    "I will let you pass if you win my game. I am thinking of a
    number. If you guess a larger number, you are dead. Guess
    my number or lower, and I will let you pass."

    What is your guess?""")

    choice = int(input("> "))

    if choice < 7:
        print("""
    You are a worthy adversary, you may pass.""")
        test_4()
    else:
        dead("Wrong! The cobra strikes you in the neck.")


def test_2():
    print("""
    You enter a room that has a wall full of different glyphs.
    You count 5 spear symbols, 9 snake symbols, 4 idol
    symbols, and 10 crazy monkey symbols. You also see
    something that resembles an abacus by a locked door.

    Next to each row on the abacus, is something that looks
    like a math problem. Enter your answers and see if you
    can get that door open.

    Next to row 1, is monkeys divided by spears.""")

    choice = int(input("> "))

    if choice == 2:
        print("""
    Row 2 is idols times spears.""")
        choice = int(input("> "))
        if choice == 20:
            print("""
    Row 3 is monkeys minus snakes.""")
            choice = int(input("> "))
            if choice == 1:
                print("""
    Door opens, you continue.""")
                test_4()
            else:
                dead("Your math skills suck!  You are killed by a poison dart.")
        else:
            dead("Your math skills suck!  You are killed by a poison dart.")
    else:
        dead("Your math skills suck!  You are killed by a poison dart.")

def test_3():
    print("""
    You enter a room that is long and narrow. You notice holes on
    the walls and suspicious looking stones on the floor.  Looks
    like the good old poison dart gimick.

    There are two doorways on the other end.  You see a path to
    the left doorway, but it will be a 'slow and steady' trip.
    The path to the right doorway will require you to be a
    'speed demon'.

    Which one do you choose?""")

    choice = input("> ")

    if choice == "slow and steady":
        print("""
    You gingerly make your way to the first doorway.
    It took forever, but you made it unscathed.""")
        test_2()
    elif choice == "speed demon":
        print("""
    You run for your life to the second doorway and only get a few nicks.
    The poison on the darts must not be too toxic.""")
        idol_room()
    else:
        dead("You get hit with multiple darts and feel the poison kicking in...death awaits.")


def test_4():
    print("""
    You enter a room filled with monkeys. They are all facing a
    very large gorilla who appears to be in charge.  A couple
    monkeys guide you through the crowd to stand in front of
    the gorilla. He says:

    "Welcome to our home.  You must be somewhat smart and
    agile to make it to this part of the tomb.  I suppose you
    are looking for some treasure.  You are either very close,
    or still very far away.  If you win my game of riddles,
    treasure might come unto you."

    Answer 'true' or 'false' to my riddle:
    Do two wrongs make a right?  In Boolean terms...
    """)

    choice = input("> ")

    if choice == "true":
        start()
    elif choice == "false":
        idol_room()
    else:
        dead("You had a 50:50 chance, what's wrong with you?")


def idol_room():
    print("""
    You have finally made it to the idol room.  There it sits up
    on a pedestal, bathed in a single ray of sunlight. You grab
    the idol, waiting for the chaos to start.  There doesn't
    appear to be any traps...something is hinky.  Suddenly, the
    door you entered through closes and three new passage ways open.

    Do you take the path on the 'left', 'center', or 'right'? """)

    choice = input("> ")

    if choice == "left":
        dead("You are grabbed by monkeys and forced to eat monkey brains!")
    elif choice == "center":
        print("""
    You run like mad, constantly looking over your shoulder.
    Then you see it, glorious daylight!  You made it out!""")
        exit(0)
    elif choice == "right":
        dead("You hear a rumbling behind you. You are squashed by a huge boulder.")
    else:
        dead("You are indecisive and stay put, slow death awaits.")


def dead(why):
    print(why, "You should have stuck with teaching, Professor Jones.")
    exit(0)


start()
