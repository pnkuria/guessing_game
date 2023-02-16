# This program creates a guessing game
from random import randint
user_name = input("Enter username")
print("Hello" + user_name + "!")

number = randint(10,50)
counter = 0
while counter < 5:
    user_number = eval(input("Enter random number:"))
    




