def square(numbers):
  squared = []
  for number in numbers:
    squared.append(number**2)
  return(squared)

str_of_numbers = input("Enter a list of numbers or enter to quit: ")
print("input (string):", str_of_numbers)

numbers_as_strings = str_of_numbers.split(' ')  # now have a list of strings

numbers_list = []
for number_as_string in numbers_as_strings:
  numbers_list.append(int(number_as_string)) 


print("The sum of your numbers is: ", sum(numbers_list))        # uses built in `sum` function
print("The squares of your numbers are:", square(numbers_list)) 
