print('''*******************************************************************************
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
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

first = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

if first == "right":
    print("Good Choice.")
    second = input('You\'ve come to a lake. There is an island in the middle of the lake.' 
          'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if second == "swim":
        print("Lucky You, you are swimming and alive.")
        third = input("Three boats are showing up, one red, one green and one blue. "
                      "Which one do you choice?\n").lower()
        if third == "blue":
            print("Yes, you took the right boat, now go and get your treasure on the island.")
            print("Congratulations you won.")
        else:
            print("You swam straight into the pirates gap. Game Over.")
    else:
        print("A hungry lion caught you. Game Over.")
else:
    print("You fell into a hole. Game Over.")
