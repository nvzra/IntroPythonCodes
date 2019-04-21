#Aimen Ahmed
#02062019
#CIS 1051
#99 Bottles of Beer

def beers(n):
    for n in range(n, 0, -1):
        print(str(n) + ' bottles of beer on the wall '+ str(n) + ' bottles of beer')
        print('Take one down, pass it around, ' + str(n-1) + 'bottles of beer on the wall')



#Sum of Square Integers
def  sumsq(n):
    sum = 0
    for x in range (1,n+1):
        sum = sum +(x**2)
    print("The sum of the squares of the first ", n, " positive integers is:  ", sum)


def multtable(n):
    for line in range (1,n+1):
        for pl in range (1,n+1):
            print(line * pl, end = "\t")
        print()

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

     

n = int(input("Enter number of beers: ")) 
beers(n)
print()
print()
print()

i= int (input("Enter a number to calculate the squared sum of the integer: "))
sumsq(i)
print()
print()
print()

n= int(input("Enter an integer to display multiplication table: "))
multtable(n)

print()
print()
hg()

n = int (input("Enter a number for slash-based ASCII art printed at size n: "))
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
