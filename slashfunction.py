n = int (input("Enter a number for slash-based ASCII art printed at size n: "))

'''
for i in range (n): #num rows
    for j in range (n*4-2):
        if i == 0:
                print("!")
        else:
            str = ""
            numexc = n *4-2-4
            numfor = (n*4-2-numexc)/ 2
            if(j < numexc):
                str += "/"
            elif (j > numexc and j < numfor):
                str  += "!"
            elif (j<= numfor):
                str += "/"
            print(str, end = "")
range(0,10,1)
'''

for i in range(n):
    # \
    for j in range (i*2):
        print("\\", end= "")
    # !
    for j in range((n-i)*4 - 2):
        print("!", end="")
    # /
    for j in range (i*2):
        print("/",end= "")


    print()
