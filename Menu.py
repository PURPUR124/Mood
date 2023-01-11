#!/usr/local/bin/python3
import os
# PLEASE DO NOT STEAL MY GAME, IT'S NOT FINISHED AND I'M VERY PROUD OF IT

while True:
    print("1.) Walk down the street")
    print("2.) Check what buisnesses there are along the street")
    WhatToDo = input("What would you like to do? ")
    if WhatToDo == "1":
        print("You walk down the street a bit, but when you look around nothing has changed, almost like you haven't moved at all...")
        os.system('sleep 5')
        os.system('clear')
    if WhatToDo == "2":
        os.system('clear')
        print("You see 4 buisnesses, and 3 homes. The buisnesses are named A, B, and C")
        EnterBuisness = input("What buisness would you like to enter? A, B, or C? ")
        if EnterBuisness == "A":
            
            food = ["Apple.py","If Else Eclair"]
            drinks = ["While Loop Tea (Hot)","Elif Latte","While Loop Tea (Cold)"]
            mop = ["You mopped, and the floor's still a little sticky","You mopped, and the floor's still really sticky","You mopped, and the floor's not sticky at all anymore"]
            sweep = ["You swept, and the floor's still a little dusty","You swept, and the floor's still really dusty","You swept,and the floor's not dusty at all anymore"]

            print("Hello!")
            print("Welcome to the Wonderful Python Cafe!")
            choice = ""
        while True:
                print("Our current Menu is:")
                print("1) If Else Eclair")
                print("2) Elif Latte")
                print("3) While Loop Tea (Hot or Cold)")
                print("4) Apple.py")
                print("5) Leave the Cafe")

                choice = input("Enter your menu selection: ")
                if (choice == "1"):
                    # Clearing the screen using the imported 'os' library
                    os.system('clear')
                    print ("Thank you for visiting the Wonderful Python Cafe, please enjoy your Else If Eclair!")
                    os.system('sleep 2')
                    print("Here's our menu again incase you forgot")
                elif (choice == "2"):
                    os.system('clear')
                    print ("Thank you for visiting the Wonderful Python Cafe, please enjoy your Elif Latte!")
                    os.system('sleep 2')
                    print("Here's our menu again incase you forgot")
                elif (choice == "3"):
                    os.system('clear')
                    print ("Thank you for visiting the Wonderful Python Cafe, please enjoy your While Loop Tea!")
                    os.system('sleep 2')
                    print("Here's our menu again incase you forgot")
                elif (choice == "4"):
                    os.system('clear')
                    print ("Thank you for visiting the Wonderful Python Cafe, please enjoy your Apple.py!")
                    os.system('sleep 2')
                    print("Here's our menu again incase you forgot")
                elif (choice == "5"):
                    os.system('clear')
                    print("You left, and are now on the sidewalk of a small bustling town.")
                    break
                elif (choice == "6"):
                    os.system('clear')
                    WorkForCafe = input("Oh you want to work for the cafe? (Y)es or (N)o: ")
	                    if WorkForCafe == ('Y') or ('y'):
	                        while True:
	                            os.system('clear')
	                            #print("Thanks for coming in today!")
	
	
	                            print("You have a couple of tasks you can do today:")
	                            print("1.) Wash Dishes")
	                            print("2.) Prep Food")
	                            print("3.) Prep Drinks")
	                            print("4.) Sweep")
	                            print("5.) Mop")
	                            print("6.) Stop Working for the Wonderful Python Cafe")
	                            choice2 = input("What would you like to do? ")
	
	                            if choice2 == "1":
	                                os.system('clear')
	                                print("You washed dishes, and they SPARKLE")
	                            elif choice2 == "2":
	                                os.system('clear')
	                                print("You prepped food, and it tastes AMAZING according to our customers")
	                            elif choice2 == "3":
	                                os.system('clear')
	                                print("You prepped drinks, and they taste INCREDIBLE according to our customers")
	                            elif choice2 == "4":
	                                os.system('clear')
	                                print("You swept, and now the floor isn't dusty!")
	                            elif choice2 == "5":
	                                os.system('clear')
	                                print("You mopped, and now the floor isn't sticky!")
	                            elif choice2 == "6":
	                                os.system('clear')
	                                print("You stopped working for us!")
	                                break
	                            else:
	                                os.system('clear')
	
	                                print("That's not on our task list, sorry!")
        #elif EnterBuisness == "B":
            #print("blah blah")
        #elif EnterBuisness == "C":
            #print("blah blah blah")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
