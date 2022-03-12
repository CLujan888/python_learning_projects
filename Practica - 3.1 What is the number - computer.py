import random


def theComputer_Guess_Number(x):
    
    print ("====================")
    print ("WELCOME TO THE GAME")
    print ("===================")
    print ("You will generate a number, and the computer will guess that")
    print ("===================")

    h_limit = x
    l_limit = 1

    option = " "

    while option != "c":
        if h_limit != l_limit:
            pc_attemp = random.randint (l_limit, h_limit)
        else:
            pc_attemp = h_limit   #can be h_limit or l_limit
        

        option = input (f"The computer thinks the number is: {pc_attemp}.\n Enter(a) if the number is lower \n or (b) if the number is higher \n or  (c) if the number is the same: ").lower()

        if option == "a":
            h_limit = pc_attemp - 1

        elif option == "b":
            l_limit = pc_attemp + 1
    
    print (f"Yes! {pc_attemp} is the number, the computer guessed the number correctly")
    

#Call the function
theComputer_Guess_Number(100)



