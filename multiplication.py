def multtable(n):
    for line in range (1,n+1):
        for pl in range (1,n+1):
            print(line * pl, end = "\t")
        print()
    

n= int(input("Enter an integer to display multiplication table: "))
multtable(n)
