#This is a Number guessing game
print("Made by Nikhil")
import random
import time
print("Hello! What's your name")
nm=input()
number=random.randint(1,20)
print("Hey! "+nm+", I am thinking a number between 1 and 20")

print("You are given 5 chances!")
for chance in range(5):
    time.sleep(1)
    print("Take a Guess:) ")
    choise=int(input())
    if choise<number:
        print("Your Guess is too low!  :(")
    elif choise>number:
        print("Your Guess is too high!  :(")
    elif choise==number:
        print("Yeah! Great you have got it! :)")
        break
time.sleep(3)

