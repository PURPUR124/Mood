#!/usr/local/bin/python3

yn = input("Do you want a dad joke? (y)es or (n)o : ")
#if "y" in yn:
if yn.casefold() == "Y":
    ans = input("Why did the pilot install a horn on his plane?     ")
    if "why" in ans:
        print("For AIR TRAFFIC XD")
    else:
        print("(you're supposed to say why)")
        ans2 = input("Why did the pilot install a horn on his plane?     ")
        if "why" in ans2:
            print("For AIR TRAFFIC XD")
if "N" in yn:
    print("You're lame yaknow that?")

print("")
print("")
print("")
print("")
print("")
