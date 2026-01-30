print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the Treasure Island\n"
      "Your mission is to find the treasure.\n"
      "You've stumbled upon this dark cave after taking a wrong turn during your hike and now You're at a crossroads.")
start_or_end=input("Do you want to Go in for this adventure or Do you want to turn back? "
                   "Type 'Go' to start or 'Turn' to exit\n").lower()

if start_or_end=="turn":
    print("You went back on your trail, never to look back again. Thanks for playing")
elif start_or_end=="go":
    direction=input("You're now at a crossroad. Do you want to go left or right?\n").lower()
    if direction=="left":
        lake=input("You've arrived near a lake. Do you want to swim across or wait for a boat?\n").lower()
        if lake=="swim":
            print("You tried to swim across the lake but it was croc infested. \nGame over")
        elif lake=="wait":
            print("A tall mysterious bearded man carrying a wand arrived a boat and you hitched a ride safely\n")
            print("He left you on a small island with nothing but a shining rock as a source of light.\n\n"
                  "Because of the dark you cant tell if the rock if far from you or right next to you.\n")
            island = input("You remembered you have a torch with you."
                           "Do you want to light the torch or go towards the shiny rock. "
                           "Type 'torch' or 'rock' to move ahead\n").lower()
            if island=="torch":
                print("You light up the entire area and find a Big Treasure Chest. \nYou Win")
                print("Thankyou for playing")
            elif island=="rock":
                print("You couldn't look where you were going and fell in a pit.\n You lose.")
                print("Game Over")

    elif direction=="right":
        print("You took a right and reached a dead end where a huge bear found you.\nGame Over")