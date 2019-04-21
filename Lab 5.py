#Aimen Ahmed
#CIS 1052
#Lab 5
#13 February 2019


#Number of Vowels

inputString = str(input("Please type a sentence or a word: "))

vowelcount = 0

inputString =inputString.lower()

vowelcount+=inputString.count("a")
vowelcount+=inputString.count("e")
vowelcount+=inputString.count("i")
vowelcount+=inputString.count("o")
vowelcount+=inputString.count("u")

print("You have %d vowels in your sentence or phrase."%(vowelcount))

print()
print()
print()
print()
print()

#Number of Even Numbers

def is_even(number):
    return number % 2 == 0 #if it's remainder = 0, it's even

def even_count(numbers_list):
    count = 0

    for number in numbers_list:
        if is_even(number): count += 1 #increment the counts; count +=1 > count = count + 1

    return count

raw_numbers = input("Enter a number to check the number of even digits in it: ") #all input comes in as a string
#numbers_list = [int(i) for i in raw_numbers.split(',')]
numbers_list = [int(i) for i in str(raw_numbers)]
count = even_count(numbers_list) #list of numbers into even_count function
print(count)
print()
print()
print()
print()
print()


#Three Digit Armstrong Numbers

def threedigarm():
    digits=int(input("To determine if the number is an Armstrong number, enter a 3 digit integer here: ")) #User digit input
    armstrong(digits)

def armstrong(d):
    sum = 0 #This would be the sum of the cubes of the digits, by starting with 0
    remainder = d 
    for x in range(0, 3): #Numbers are counted
        LastDig = remainder % 10 #% means division by modulus 10, to get the last digit
        remainder = remainder//10 #Integer dicision
        sum = sum + (LastDig**3) #Addition of the digit cubed to the sum
    # first check if number if 3 digits by checking if rem == 0
    if remainder != 0:
        print(d, "is not a three digit number.")
    #Armstrong number by comparison of sum
    elif d == sum:
        print(d, "as a number, is by definition a three digit Armstrong number.")
    else:
        print(d, "as a number is not an Armstrong number.")


threedigarm()

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()


#Riddler

def ridlr():
    for x in range(1000,10000): #The loop from the first 4 digit number (1000) to the last (9999)
        if Rid(x):
            print(x, "must be the address")

def Rid(d): #D is digits

    # split up the number by its digits
    remainder = d 
    #Ones/ remainder
    ones = remainder % 10
    remainder = remainder//10
    #Tens/ remainder
    tens = remainder % 10
    remainder = remainder//10
    #Hundreds/ remainder
    hundreds = remainder % 10
    remainder = remainder//10
    #Thousnds/ remainder
    thousands = remainder % 10

    if ones==tens: #cannot be addresses, deem as false statements
        return False
    elif ones==hundreds:
        return False 
    elif ones==thousands:
        return False
    # compares to tens
    elif tens==hundreds:
        return False
    elif tens==thousands:
        return False 
    elif hundreds==thousands:
        return False 

    if thousands != 3*tens:
        return False #1000s place

    if (d % 2 == 0): #Must be odd, false by definition
        return False

    #Sum digits = 27
    sum = thousands + hundreds + tens + ones
    if (sum != 27):
        return False

    return True
print()
print()
print()

print("For the riddler puzzle...")
ridlr()
