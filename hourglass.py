def hg():
    print("|\"\"\"\"\"\"\"\"\"\"\"|")
    for line in range(1,5):
        print(" "*line, end="")
        #for x in range (line):
           #   print(" ", end="")
        print("\\", end ="")
        print(":"*(8-2*(line-1)), end="")
        print("/", end ="")
        print()
    print("     ||")
    for line in range(1,5):
        print(" "*(4-line+1), end="")
        #for x in range (line):
           #   print(" ", end="")
        print("/", end ="")
        for _ in range(line*2):
            print(":", end="")
        print("\\", end ="")
        print()
    print("|\"\"\"\"\"\"\"\"\"\"\"|")

hg()
