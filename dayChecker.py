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
## ughhhhh it thinks everything is pizza. TBFL
FavFood = input("What's your favorite food? I think mine might be pizza! ")
if FavFood == "Pizza":
    print("Oh wow we have the same favorite food, Pizza! :0")
elif FavFood == "Sandwiches":
    print("I like sandwiches too! Unless they get soggy, ew.")
elif FavFood == "Sushi":
    print("Mmmmmm sushii. Sushi's reeeeaally good too")
else:
    print("Hmm, I haven't tried that! It sounds like it could be good though!")

##UserAge = input("How old are you? I'm preetty young, I mean, I was just made! ")
##if UserAge == "1" or "2" or "3" or "4" or "5":
   ##print("Oh! You're REALLY young! You spell really well! Keep it up!")
##elif UserAge == "6" or "7" or "8" or "9" or "10":
    ##print("You're getting older! Congrats!")
##else:
    ##print("You're oldddd")

