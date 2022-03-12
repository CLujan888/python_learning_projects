#Mad Libs simulator

food_1 = input("Enter a type of food: ")
name_1 = input("Enter the student name: ")
verb_1 = input("Enter a verb: ")
noun_1 = input("Enter a noun: ")
verb_2 = input("Enter another verb in the past sentence: ")
verb_3 = input("Enter a third verb in the past sentence: ")
verb_4 = input("Enter the last verb in the past sentence: ")

mad_lib = f"It was {food_1} day at school, and {name_1} was super excited for {verb_1}. But when she went outside to eat, a {noun_1} stole her {food_1}! {name_1} chased the {noun_1} all over school. She {verb_2}, {verb_3}, and {verb_4} through the playground. Then she tripped on her shoelace and the {noun_1} escaped! Luckily, {name_1}'s friends were willing to share their {food_1} with her."

print(mad_lib)