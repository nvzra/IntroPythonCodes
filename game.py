myage=22
guess=input("guess my age")
if int(guess) == myage:
    print("good guess")
if int(guess) >= 30:
    print("too old")
if int(guess) < 18:
    print("too young")
