#!/usr/local/bin/python3

Name = input("What's your name? ")
print("Nice to meet you, " + Name + "!")
HowIsDoingToday = input("How are you doing today " + Name + "?? Good or Bad? ")
if "bad" in HowIsDoingToday:
    print("Oh I'm so sorry to hear that, " + Name + "! I hope it gets better!")
elif "good" in HowIsDoingToday:
    print("That's great! I hope it stays that way " + Name + "!")
else: 
    print("I'm not sure what you meant by that, but ok?")
FavFood = input("What's your favorite food? I think mine might be pizza! ")
if "pizza" in FavFood:
    print("Oh wow we have the same favorite food, Pizza! :0")
elif "sandwiches" in FavFood:
    print("I like sandwiches too! Unless they get soggy, ew.")
elif "sushi" in FavFood:
    print("Mmmmmm sushii. Sushi's reeeeaally good too")
else:
    print("Hmm, I haven't tried that! It sounds like it could be good though!")
print("I've been doing some random stuff lately, namely gaming.")
WhatBeenDoingLately = input("How about you? ")
if WhatBeenDoingLately == "Nothing really":
    print("Oh that's too bad, maybe you can do something fun sometime soon?")
else:
    print("Oooh!")
Age = input("How old are you? I'm pretty new in some aspects- I'm still being made actually! ")

if int(Age) <= 7:
    print("Oh you're young! You spell really well, keep it up!")
elif int(Age) > 7 and int(Age) <  15:
    print("Almost old enough to drive XD")
elif int(Age) > 15 and int(Age) < 30:
    print("Noice, old enough to drive!")
elif int(Age) > 30:
    print("Hmm, decently old")

print("Well, I had fun talking to you! I hope you have a good rest of your day :)")

