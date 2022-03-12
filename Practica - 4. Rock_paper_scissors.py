import random

def psr_game():

    print ("========================")
    print ("  WELCOME TO THE GAME")
    print ("=========================")
    print ("Paper - Scissors - Rock")
    print ("=========================")

    user_choice = input("Enter (pa) for paper \n or enter (sc) for scissors \n or enter (ro) for rock").lower()

    if user_choice == "pa":
        print ("User choice: PAPER")
    elif user_choice == "sc":
        print ("User choice: SCISSORS")
    elif user_choice == "ro":
        print ("User choice: ROCK")


    computer_choice = random.choice(["pa", "sc", "ro"])

    if computer_choice == "pa":
        print ("PC choice: PAPER")
    elif computer_choice == "sc":
        print ("PC choice: SCISSORS")
    elif computer_choice == "ro":
        print ("PC choice: ROCK")


    if user_choice == computer_choice:
        print ("====")
        print ("DRAW")
        print ("====")
    elif user_choice == "pa" and computer_choice == "ro":
        print ("====")
        print ("USER'S VICTORY")
        print ("====")
    elif user_choice == "sc" and computer_choice == "pa":
        print ("====")
        print ("USER'S VICTORY")
        print ("====")
    elif user_choice == "ro" and computer_choice == "sc":
        print ("====")
        print ("USER'S VICTORY")
        print ("====")
    else:
        print ("====")
        print ("THE COMPUTER WINS")
        print ("====")


psr_game()