#Creating Python Lists: Literals, Concatenation, and More
empty_list  = []
even = [2, 4, 5, 6]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits =  sorted("432985617")
print(digits)

digits =  list("432985617")
print(digits)

# more_numbers = list(numbers)
# more_numbers =  numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
#checking if number n more_numbers are the same
print(numbers is more_numbers)
print(numbers == more_numbers)
