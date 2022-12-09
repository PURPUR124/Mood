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

