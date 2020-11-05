import random
import time
from constants import PLAYER, EMPTY_SPACE, EXIT, PUZZLE

# Room Variable - The map of which the players moves about
room = [
    'xxxxxxxxxxxxxxxxx',
    'x....x........xex',
    'x.xx...xx.xxx.x.x',
    'x..x.xx.xpx.xxx.x',
    'x.x.....x.......x',
    'xxxxxxxxxxxxxxxxx'
]


# Word Puzzle function - Starts a password guessing minigame when called
def word_puzzle():
    passwords_list = [
        "blue", "applesauce", "nickel", "bababooey", "cheesecake"
    ]
    correct_password = random.choice(passwords_list)
    print("A wall with a computer terminal blocks your path.")
    time.sleep(2)
    print("You find a note with words scribbled all over it.")
    time.sleep(2)
    for each_password in passwords_list:
        if each_password == correct_password:
            print(each_password.upper())
        else:
            print(each_password)
    time.sleep(2)
    print("The computer terminal flashes on the screen...")
    guess = input("Please input password to continue: ")
    while guess != correct_password:
        print("ERROR: INCORRECT PASSWORD")
        print(f"Looks like, {guess} was not the password!")
        guess = input("Try again: ")

    print(
        "The computer screen flashes for a second, then the wall blocking your path slowly sinks into the ground."
    )
    time.sleep(2)


# Move function - The main movement function for the character
def move(current_row, current_col, direction):
    new_row = current_row
    new_col = current_col

    if direction == "up" and room[new_row - 1][new_col] != "x":
        new_row -= 1
    elif direction == "down" and room[new_row + 1][new_col] != "x":
        new_row += 1
    elif direction == "right" and room[new_row][new_col + 1] != "x":
        new_col += 1
    elif direction == "left" and room[new_row][new_col - 1] != "x":
        new_col -= 1
    elif direction not in ("up", "down", "left", "right"):
        print("Please submit either up, down, left, or right.")
    else:
        print("You ran into a wall! Try going somewhere else.")
    return [new_row, new_col]


# Print Map Function - Prints the map with a view limited to 1 space around the current location
def print_map(room, current_row, current_col):
    for row_index, each_row in enumerate(room):
        print_row = []
        if row_index not in (0, (len(room) - 1)):
            if (row_index == current_row) or (
                    row_index == current_row + 1) or (
                        row_index == current_row - 1):
                for col_index, each_col in enumerate(list(each_row)):
                    if row_index == current_row and col_index == current_col:
                        print_row.append(PLAYER)
                    elif col_index == current_col or (
                            col_index == current_col + 1) or (
                                col_index == current_col - 1):
                        print_row.append(each_col)
                    else:
                        print_row.append(EMPTY_SPACE)
            else:
                for col_index, each_col in enumerate(list(each_row)):
                    print_row.append(EMPTY_SPACE)
            print("".join(print_row))
        else:
            print(each_row)


# Initial location of character
current_row = 4
current_col = 1

print("You wake up with a dizzying pain in your head.")
time.sleep(2)
print("You have such a headache, you can't even remember your name!")
time.sleep(2)
print("What was it, Bob? No, Roberto! No, couldn't be.")
time.sleep(2)
player_name = input("Wait I remember! It was... \nInput name here: ")

if (player_name.lower()) == "bob":
    print("It was Bob afterall!")
elif (player_name.lower() == "roberto"):
    print("Ahhh wait, it was Roberto aha.")
else:
    print(f"Ahhhh yes, {player_name}. What a fine name it is.")

time.sleep(2)
print("Now, what are you doing here anyhow?")
time.sleep(2)
print("You find a note...\n")
print(f"Welcome to my Labyrinth {player_name},")
print("I have spent a long time watching you.")
print("I have deemed you are the perfect person to solve it.")
print("Now, set forth and ESCAPE MY LABYRINTH.\n")
time.sleep(4)
print("What a strange letter you think to yourself.")
time.sleep(2)
print("You set forth to escape that weirdo's silly maze.\n")

while room[current_row][current_col] != EXIT:
    print()
    print_map(room, current_row, current_col)
    print()
    direction = input("What direction would you like to move? ")
    current_row, current_col = move(current_row, current_col, direction)
    if room[current_row][current_col] == PUZZLE:
        print()
        word_puzzle()

print("You feel the warm sun bathe your body in light.")
time.sleep(2)
print("You expect to hear the Labyrinth Weirdo scream out to you.")
time.sleep(2)
print("Silence...")
time.sleep(2)
print("They must be shouting to themself somewhere hidden away.")
time.sleep(2)
print("Oh well, you are free and that's all that matters.")
time.sleep(2)
print(
    "You walk through the wheat fields, following the power lines to the nearest road."
)
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(f"Game Over. Thank you for playing {player_name}!")
