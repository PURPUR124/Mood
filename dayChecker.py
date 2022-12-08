#!/usr/local/bin/python3

## get user input
Name = input("What's your name? ")

## print some things
print("Nice to meet you, " + Name + "!")

## get _more_ input
HowIsDoingToday = input("How are you doing today " + Name + "?? Good or Bad? ")
if HowIsDoingToday == "Bad":
    print("Oh I'm so sorry to hear that, " + Name + "! I hope it gets better!")
elif HowIsDoingToday == "Good":
    print("That's great! I hope it stays that way " + Name + "!")



