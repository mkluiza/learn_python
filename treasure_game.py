# Treasure Island Game

print("Welcome to Treasure Island. Your mission is to find the treasure.")
first_step = input(
    "You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")
if first_step == "left":
    second_step = input(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    if second_step == "wait":
        third_step = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if third_step == "yellow":
            print("You found the treasure! You Win!")
        elif third_step == "red":
            print("It's a room full of fire. Game Over.")
        elif third_step == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fall into a hole. Game Over.")


