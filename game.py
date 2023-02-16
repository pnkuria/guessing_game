# This program creates a guessing game
from random import randint
user_name = input("Enter username")
print("Hello" + user_name + "!")

random_number = randint(10,50)
counter = 0
while counter < 5:
    user_number = eval(input("Enter random number:"))
    counter += 1
    if user_number<random_number:
        print("Your guess is too low")
    elif user_number > random_number:
        print("Your guess is too high")
    elif user_number==random_number:
        print("You win!")
        break
     






