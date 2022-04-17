
name = input("What is your name traveler? "+ "\n" +"Name : ")
print("Welcome,",  name , "!" + "\n")
print("#####################################################" + "\n")

answer = input("You walk the path of the pilgrim,in search of truth."+ "\n" + "The unforgiving sun is ever watching,your feet are heavy and your lips dry."+ "\n" + "You approach a lonely tree in this vast desert . It's shade is tempting. What do you do? ")

if (answer == "stay" or answer =="relax" or answer =="break" or answer =="take a break" or answer =="stop"):
    answer == input(
        "\n"+"As you approach the tree it's shade embraces you"+ "\n" + " and a sudden breeze lifts the weight of your travel.As you sit you begin to drift in and out of conciousness. This tree seems special.What do you do? ")
   
    if (answer == "look" or answer =="look around" or answer =="explore" or answer =="take a break" or answer =="stop"):
        answer == input(
            "\n"+"Suddenly water bursts out of the tree trunk, creating a small pond on the dry soil. It seems to be crystal clear.What do you do? ")
    
    elif (answer == "get up" or answer =="leave" or answer =="go away" or answer =="stop resting"):    
        answer == input(
            "\n"+"You are now well rested. During your short sleep you dreamt of a golden owl ")
   


elif (answer == "leave" or answer =="go away" or answer =="keep going" or answer =="move" or answer =="keep moving" or answer =="run"):
      answer == input(
          "\n"+"You are devouted to the road. Passing by the tree you notice an odd structure ahead. The piercing rays of the sun now feel even heavier.")

else : 
    print("\n" + "Not a viable option! Try again.")     