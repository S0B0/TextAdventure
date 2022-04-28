#   
#   I am strong just like a steed
#   When I fall I do not bleed
#   Yet I die from those in ...?
#   

import sys,time,os
from tkinter import N
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)




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

def characterCreation():
    typewriter("Choose a name: ",)
    name = input("\n>:")
    return name

#FIRST MENU
def firstMenu():
    typewriter(Fore.YELLOW + "Make a numeric selection:  ",0.03,0.2)
    print("[1] Start")
    print("[2] ???")
    print("[3] ???")
    print("[0] EXIT")

def interactRabbit():
     typewriter("    \n(Rabbit) :\n\
    -O I welcome thee upon thy temple for which faith must be the key.\n\
Answer minth riddles and I shall grant you entrance. \n [riddles] \n [leave] \n",0.03,0.2)
     firstInteract = input("\n>:")
     if firstInteract == "riddles":
        riddles()
     elif firstInteract == "who are you":
         typewriter("I am the guardian of thy temple.",0.03,0.2)
     elif firstInteract == "leave":
         typewriter("You chose to leave the path. Rot reached your chest and neck. You collapse... The pilgrimage ends... ",0.03,0.2)  
         finalDecision = input("\n>:") 
     else:
         typewriter("INVALID INPUT. TRY AGAIN\n",0.03,0.2)
         interactRabbit()
# RABBIT RIDDLES FUNCTION ~ USED ON THE LEAVE PATH
def riddles():
   
    typewriter(" \n                                 'Spends all  life in but a cage\n\
				 Brings us joys yet it can rage\n\
				 Behold thee,the restless sage!'\n \n                                 What am I? \n>: ",0.03,0.2)
    firstRiddleAnswer = input()
    if firstRiddleAnswer == "heart" or firstRiddleAnswer == "Heart" or firstRiddleAnswer == "HEART":
        typewriter("    (Rabbit) : \n\
    -You are quite bold yet still I won't start to fold\n",0.03,0.2)
    
    else :
        typewriter("INVALID INPUT.TRY AGAIN\n",0.03,0.2)
        riddles()

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
        typewriter("\n            ====== ## PROLOGUE ## ======\n",0.03,0.2)
        prologue()

# PROLOGUE FUNCTION USED IN THE START GAME 
def prologue():
    typewriter("You walk the path of the pilgrim,in search of truth.\n\
The unforgiving sun is ever watching,your feet are heavy and your lips dry.\n\
You approach a lonely tree in this vast desert . It's shade is tempting. \n\
What do you do?" + Fore.RED +"\n [rest] \n [leave]\n>: ",0.03,0.2)

    firstPath = input() 
    if firstPath == "rest" or firstPath == "relax" or firstPath == "sit" or firstPath == "stay":
        restPath()
    elif firstPath == "leave" or firstPath == "go away" or firstPath == "keep moving":
        leavePath()
    else:
        print("INVALID INPUT.Try again\n")
        prologue()
        

# REST PATH FUNCTION ~ USED IN THE PROLOGUE ~ 
def restPath():
    typewriter("As you approach the tree it's shade embraces you\n\
and a sudden breeze lifts the weight of your travel.\n\
As you sit down,you begin to drift in and out of conciousness.\n\
This tree seems special.What do you do? \n [focus] \n [wake up] \n>: ",0.03,0.2)
    secondPath = input()
    if secondPath == "focus" or secondPath == "look" or secondPath == "observe":
        print("WATER PATH")
        #waterPath()
    elif secondPath == "leave" or secondPath == "get up" or secondPath == "wake up":
        print("LEAVE PATH")
        #leavePath()
    else:
        print("INVALID INPUT.Try again\n")
        restPath()

def leavePath():
    typewriter("You are devouted to the road. \n\
The sun is slowly setting and it's piercing rays are less heavier.\n\
Your eyes begin to reflect the first blinks of the stars.\n\
Upon a rocky structure there lies a temple.\n\
A rabbit guards its door.",0.03,0.2)
    typewriter("\n\
   \        \n\
    \ /\    \n\
    ( )     \n\
  .( o ).   \n\
    "+ Fore.YELLOW + " \n [talk] \n ",0.03,0.2)
    interact = input("\n>:")
    if interact == "talk":
        typewriter("You greet the rabbit...",0.03,0.2)
        interactRabbit()
    else:
        typewriter("INVALID INPUT.TRY AGAIN",0.03,0.2)
        leavePath()




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
       startGame()
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





