#   
#   I am strong just like a steed
#   When I fall I do not bleed
#   Yet I die from those in ...?
#   

import sys,time,os

#  Note : typewriter class is WIP
def typewriter(message,s1,s2):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(s1)
        else:
            time.sleep(s2)
#os.system("cls") 

#FIRST MENU
def firstMenu():
    print("Make a numeric selection:  ")
    print("[1] Start")
    print("[2] ???")
    print("[3] ???")
    print("[0] EXIT")

# RABBIT RIDDLES FUNCTION ~ USED ON THE LEAVE PATH
def riddles():
    typewriter("            (Rabbit) :\n\
				-O I welcome thee upon thy temple for which fate must be the key.\n\
				Answer minth riddles and I shall grant you entrance.\n",0.03,0.2)
    typewriter(" \n                                 'Spends all  life in but a cage\n\
				 Brings us joys yet it can rage\n\
				 Behold thee,the restless sage!'\n \n                                 What am I? \n>: ",0.03,0.2)
    firstRiddleAnswer = input()
    if firstRiddleAnswer == "heart" or firstRiddleAnswer == "Heart" or firstRiddleAnswer == "HEART":
        typewriter("        (Rabbit) : \n\
				-Wise pilgrim you are quite bold yet still I won't start to fold\n",0.03,0.2)

# START GAME FUNCTION ~ USED IN THE MAIN
def startGame():
    typewriter("Would you like to start the game? (Y/N)\n>: ",0.03,0.2)
    start = input() 
    if start == "n" or start == "N"or start == "no" or start == "No" or start == "NO":
        uSure = input("are you sure? (Y/N)\n>: ")
        if uSure == "n" or uSure == "N"or uSure == "no" or uSure == "No" or uSure == "NO":
            print("\n             ## PROLOGUE ##\n",0.03,0.2)
            prologue()
        elif uSure == "y" or uSure == "Y"or uSure == "yes" or uSure == "Yes" or uSure == "YES":
            print("FAREWELL...")
    elif start =="y" or start == "Y" or start == "yes" or start == "Yes" or start == "YES":
        typewriter("\n             ## PROLOGUE ##\n",0.03,0.2)
        prologue()

# PROLOGUE FUNCTION USED IN THE START GAME 
def prologue():
    typewriter("              You walk the path of the pilgrim,in search of truth.\n\
            The unforgiving sun is ever watching,your feet are heavy and your lips dry.\n\
            You approach a lonely tree in this vast desert . It's shade is tempting. \n\
            What do you do? \n>: ",0.03,0.2)

    firstPath = input() 
    if firstPath == "rest" or firstPath == "relax" or firstPath == "sit" or firstPath == "stay":
        restPath()
    elif firstPath == "leave" or firstPath == "go away" or firstPath == "keep moving":
        leavePath()
    else:
        print("INVALID INPUT.Try again")
        prologue()
        

# REST PATH FUNCTION ~ USED IN THE PROLOGUE ~ 
def restPath():
    typewriter("            As you approach the tree it's shade embraces you\n\
            and a sudden breeze lifts the weight of your travel.\n\
            As you sit down,you begin to drift in and out of conciousness.\n\
            This tree seems special.What do you do? \n>: ",0.03,0.2)
    secondPath = input()
    if secondPath == "focus" or secondPath == "look" or secondPath == "observe":
        print("WATER PATH")
        #waterPath()
    elif secondPath == "leave" or secondPath == "get up" or secondPath == "wake up":
        print("LEAVE PATH")
        #leavePath()
    else:
        print("INVALID INPUT.Try again")

def leavePath():
    typewriter("            You are devouted to the road. \n\
		The sun is slowly setting and it's piercing rays are less heavier.\n\
		Your eyes begin to reflect the first blinks of the stars.\n\
		Upon a rocky structure there lies a temple.\n\
		A rabbit guards its door.\n",0.03,0.2)
    riddles()


## MAIN ##
print()
print()
print("    ~~###############################~~")
print("     ~#                             #~")
print("    ~~#         ~The road~          #~~")
print("     ~#                             #~")
print("    ~~###############################~~")
print()
print()


firstMenu()
option = int(input(">:"))

while option != 0:
    if option == 1:
       leavePath()
    elif option == 2:
        print("??")
    elif option == 3:
        print("??")
    else:
        print("Invalid Option")
   
    firstMenu()
    #typewriter("\nMake numeric selection\n>:",0.03,0.2)
    option = int(input(">:"))
        
print("Farewell...")





