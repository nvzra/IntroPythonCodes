date = input("Please enter a date (mm/dd/yyyy)\n")
# mm/dd/yyyy
# 0123456789

month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:])

# Months with 30 days
if month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days month")
    if day < 1 or day > 30:
        print("Invalid date")
    else:
        print("Valid date")

# Months with 31 days
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days month")
    if day < 1 or day > 31:
        print("Invalid date")
    else:
        print("Valid date")

# Month of February
if month == 2:
    print("February of Doom")
    if day >= 1 and day < 29:
        print("Valid date")
    elif day == 29:
        print("To-do: Check for leap year")
        if year % 4 == 0:
            print("Possibly a leap year")
            if year % 400 == 0:
                print("This is a leap year")
            elif year % 100 == 0:
                print("This cannot be a leap year because of an invalid date")
            else:
                print("This is a leap year")
    else:
        print("Invalid date")

if month < 1 or month > 12:
    print("Invalid month. Retry, please.")
