import sys,time,os

from click import option
#Ah, Lord, Lord, nobody's fault but mine
run = True
menu = True
play = False
rules = False

HP = 10
WILL = 6
pos = 0




def titlecard():
    print()
    print()
    
    print("<=======================-~oOxOo~-=======================>")
    print("I                                                       I")
    print("I               ~The tome of untold tales~              I")
    print("I                    -=[ by S0B0 ]=-                    I")
    print("I                                                       I")
    print("<=======================-~oOxOo~-=======================>")
    
    print()
    print()



def rulepage():
    print("   <=----------------------[ RULES ]-----------------------=>")
    print("   |  If an option has a number near it, type that number.  |")
    print("   |  If an option has no number near it,type the word in   |")
    print("   |   the square brackets []                               |")
    print("   |                                                        |")
    print("   |   do not press any keys while the typewriter animation |")
    print("   |   is playing                                           |")
    print("   |                                                        |")
    print("   |                                                        |")
    print("   |                                                        |")
    print("   |                                                        |")
    print("   |                                                        |")
    print("   |                                                        |")
    print("   |                                                        |")
    print("   <=----------------------[ RULES ]-----------------------=>             ")
    
 
 
 
def typewriter(message,s1,s2):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(s1)
        else:
            time.sleep(s2)

def clear():
    os.system("cls")


def drawline():
    print(" <=============-~oOxOo~-=============>")
    

def save():
    list = [name,str(HP),str(WILL),str(pos)]
    f = open("load.txt","w")
    for item in list:
        f.write(item + "\n")
    f.close()
 
def riddles():
     print("RIDDLES")
 
 
def rabbit(met_owl):
    typewriter("\n\
   \        \n\
    \ /\    \n\
    ( )     \n\
  .( o ).   \n\
     \n ",0.03,0.2)
    typewriter("    \n(Rabbit) :\n\
    -O I welcome thee upon thy temple for which faith must be the key.\n\
Answer minth riddles and I shall grant you entrance. \n [riddles] \n [talk]",0.03,0.2)
    op = input("\n>: ")
    if op == "riddles":
        riddles()
    elif op == "ask" and met_owl == False:
        typewriter(f"\n({name}): - Who are you? \n")
        typewriter("(Rabbit): - My name is of no importance. Know this : \n\
I am but the guardian of this temple",0.03,0.2)
        print("[riddles]")
        riddles()
    elif op == "ask" and met_owl == True:
        typewriter(f"\n({name}): - I don't trust you. You have no heart. \n",0.03,0.2)
        input("\n|enter|")
        
    else:
        print("\nINVALID INPUT")  
        input("\n|enter|")  
    
 
def prologue():
    met_owl = False
    clear()
    typewriter("it's 1990 and you sit in your bedroom \n\
playing a text adventure game on your computer.\n\
The rain drops on your window reflect the pale shade of the full moon.\n\
you feel at ease...\n\
As you begin your journey...",0.03,0.2)
    input("\n|enter|")
    clear()
    typewriter("...",0.03,0.2)
    typewriter("You walk the path of the pilgrim,in search of truth.\n\
The unforgiving sun is ever watching,your feet are heavy and your lips dry.\n\
You approach a lonely tree in this vast desert . It's shade is tempting. \n\
What do you do? ",0.03,0.2)
    print("\n[reach tree]\n[ignore tree]")
    dir = input(">: ")
    
    if dir == "reach tree":
        clear()
        typewriter("\nAs you approach the tree it's shade embraces you\n\
and a sudden breeze lifts the weight of your travel.\n\
As you sit down,you begin to drift in and out of conciousness.\n\
This tree seems special.",0.03,0.2)
        input("\n|enter|")
        typewriter("\nYour mind falls into a deep slumber...\n\
you start to dream of lush lands,the sky is clear here and the sound\n\
of a shy river can be heard.",0.03,0.2)
        input("\n|enter|")
        typewriter("\nYou see a great owl approaching...\n\
You feel protected,this entity feels familiar.\n[greet owl] \n[remain silent]",0.03,0.2)
        dec = input("\n>: ")
        if dec == "greet owl" or dec == "remain silent":
            typewriter("\nTraveler,a warning : beware the one who speaks in riddles\n\
for it has no H E A R T...",0.03,0.2)
            met_owl = True
            input("\n|enter|")
            typewriter("\nBefore you can say anything the great owl flies over you and fades\n\
in the distance. This interaction was weird.You suddenly wake up. You feel refreshed",0.03,0.2)
            input("\n|enter|")
            clear()
            typewriter("You resume your journey. \n\
The sun is slowly setting and it's piercing rays are less heavier.\n\
Your eyes begin to reflect the first blinks of the stars.\n\
Upon a rocky structure there lies a temple.",0.03,0.2)
            input("\n|enter|")
            typewriter("...As you approach the temple you see a rabbit guarding the entrance.\n [talk]",0.03,0.2)
            op = input("\n>: ")
            if op == "talk":
                rabbit(met_owl)
        else:
            print("invalid input! try again!")
            input("\n|enter|")
           
    elif dir == "ignore tree":
        clear()
        typewriter("You are devouted to the road. \n\
The sun is blazing the land,it's rays feel heavy.\n\
Despite the harsh environment you keep going.\n\
Upon a rocky structure there lies a temple,weirdly your heart skips a beat.",0.03,0.2)
        input("\n|enter|")
        typewriter("...As you approach the temple you see a rabbit guarding the entrance.\n [talk]",0.03,0.2)
        op = input("\n>: ")
        if op == "talk":
            rabbit(met_owl)
    else:
        
        print("INVALID INPUT! TRY AGAIN!")
        prologue()
     
 
 
 
 
    
while run:
    while menu:
        clear()
        titlecard()
        print("[1] NEW GAME")
        print("[2] LOAD GAME")
        print("[3] RULES")
        print("[0] QUIT GAME")
        
        if rules:
            clear()
            drawline()
            rulepage()
            drawline()
            rules = False
            choice = ""
            input("|enter| back ")
        else:
            choice = input(">: ")
        
        if choice == "1":
            clear()
            print(" WHAT IS YOUR NAME? ")
            name = input(">: ")
            menu = False
            play = True
        elif choice == "2":
           try:
                f = open("load.txt","r")
                load_list = f.readlines()
                if len(load_list) == 4:
                    name = load_list[0][:-1]
                    HP = load_list[1][:-1]
                    WILL = load_list[2][:-1]
                    pos = load_list[3][:-1]
                    clear()
                    drawline()
                    print("LOAD SUCCESSFUL. PLEASE PRESS ENTER TO CONTINUE \n")
                    #print(f"Welcome back, {name}\nyour stats are below : \n HP: {HP} \n will: {WILL}")
                    drawline()
                    input("|enter| continue ")
                    menu = False
                    play = True
                else:
                    print(" CORRUPT SAVE FILE! ")
                    input("|enter| ")
           except OSError:
               print(" NO LOADABLE FILE AVAILABLE! START A NEW GAME PLEASE! ")
               input("|enter| ")
            
        elif choice == "3":
            rules = True
        elif choice == "0":
            quit()
            
     
    
    while play:
        save()
        clear()
        drawline()
        print(f"Welcome to these lands,{name}")
        print("[1] BEGIN JOURNEY")
        print("[0] SAVE AND QUIT TO MENU")
        drawline()
        option = input(">: ")
        
        if option == "0":
            play = False
            menu = True
            save()
        elif option == "1":
            prologue()



