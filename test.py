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
                    WorkForCafe = input("Oh you want to work for the cafe? (Y)es or (N)o: ")
	                if WorkForCafe == ('Y') or ('y'):
                        toast=bread
                    print("Here's our menu again incase you forgot")
                elif (choice == "3"):
                    os.system('clear')
                    print("chose 3")
