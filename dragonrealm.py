#This is a Dragon Realm Game
import random
import time

print("Game credit: Nikhil Gupta\n")
time.sleep(1)
def intro():
    print("You are in a land full of dragons.")
    time.sleep(1)
    print("In front of you,\nyou see two caves. In one cave, the dragon is friendly\n")
    time.sleep(1)
    print("and will share his treasure with you. The other dragon")
    time.sleep(1)
    print("is greedy and hungry, and will eat you on sight.")
def common():
    print("You approach the cave...")
    time.sleep(1)
    print("It is dark and spooky...")
    time.sleep(1)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(1)

ch="yes"
while ch=="yes":
    intro()
    print("which cave you would like to go\n1 (Press 1)\n2 (Press 2)")
    cave=''
    while cave!='1'and cave!='2':
        cave=input()
    cave=int(cave)
    num=random.randint(1,2)
    common()
    if num==cave:
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")
    print("Play Again! \n (type) yes \n(type) no")
    ch=input()
time.sleep(3)
#i=input()
