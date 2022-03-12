

Oper_1 = int(input("Enter (1)to Add (2) to Substract (3)to Multiply or (4)to Divide: "))

if Oper_1 == 1:
    print ("Your choice is Addition")
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    total_1 = num_1 + num_2
    print (f"{num_1} + {num_2} = {total_1}")

elif Oper_1 == 2:
    print ("Your choice is Substraction")
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter a second number: "))
    total_1 = num_1 - num_2
    print (f"{num_1} - {num_2} = {total_1}")

elif Oper_1 == 3:
    print ("Your choice is Multiplication")
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    total_1 = num_1 * num_2
    print (f"{num_1} * {num_2} = {total_1}")

elif Oper_1 == 4:
    print ("Your choice is Division")
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    total_1 = num_1 / num_2
    print (f"{num_1} / {num_2} = {total_1}")

else:
    print ("Insert a number between 1 and 4")



