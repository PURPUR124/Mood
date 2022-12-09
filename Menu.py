#!/usr/local/bin/python3



print("Hello!")
print("Welcome to the Wonderful Python Cafe!")
choice = ""
while True:
    print("Our current Menu is:")
    print("1) If Else Eclair")
    print("2) Elif Latte")
    print("3) While Loop Tea")
    print("4) Apple.py")
    print("5) Leave the Cafe")

    choice = input("Enter your menu selection: ")
    choice = choice.strip()
    if (choice == "1"):
        print ("Thank you for visiting the Wonderful Python Cafe, please enjoy your Else If Eclair!")
    elif (choice == "2"):
        print ("Thank you for visiting the Wonderful Python Cafe, please enjoy your Elif Latte!")
    elif (choice == "3"):
        print ("Thank you for visiting the Wonderful Python Cafe, please enjoy your While Loop Tea!")
    elif (choice == "4"):
        print ("Thank you for visiting the Wonderful Python Cafe, please enjoy your Apple.py!")
    elif (choice == "5"):
        print ("Left the Cafe")
        break
    elif (choice == "6"):
        WorkForCafe = input("Oh you want to work for the cafe? (Y)es or (N)o: ")
        if WorkForCafe == "Y":
                break
        if WorkForCafe == "N":
            print("Ok!")

    else:
        print ("That's not on our menu, sorry!")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    choice2 = ""
while WorkForCafe == "Y":
        print("Thanks for coming in today!")
        print("You have a couple of tasks you can do today:")
        print("1.) Wash Dishes")
        print("2.) Prep Food")
        print("3.) Prep Drinks")
        print("4.) Sweep")
        print("5.) Mop")
        print("6.) Leave the Cafe")
        choice2 = input("What would you like to do? ")

        if choice2 == "6":
            print("Left the Cafe")
            break
        elif choice2 == "1":
            print("You washed dishes, and they SPARKLE")
        elif choice2 == "2":
            print("You prepped food, and it tastes AMAZING according to our customers")
        elif choice2 == "3":
            print("You prepped drinks, and they taste INCREDIBLE according to our customers")
        elif choice2 == "4":
            print("You swept, and now the floor isn't dusty!")
        elif choice2 == "5":
            print("You mopped, and now the floor isn't sticky!")
        else:
            print("That's not an option on the task list, sorry!")

