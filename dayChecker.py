#!/usr/local/bin/python3

Name = input("What's your name? ")
print("Nice to meet you, " + Name + "!")
HowIsDoingToday = input("How are you doing today " + Name + "?? Good or Bad? ")
if HowIsDoingToday == "Bad":
    print("Oh I'm so sorry to hear that, " + Name + "! I hope it gets better!")
elif HowIsDoingToday == "Good":
    print("That's great! I hope it stays that way " + Name + "!")
else: 
    print("I'm not sure what you meant by that, but ok?")



