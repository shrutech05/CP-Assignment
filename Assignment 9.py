# 1. Define Functions `fun()`, `disp()`, and `msg()`, Store Them in a List, and Call Them in a Loop

# Define three functions
def fun():
    print("This is fun() function.")

def disp():
    print("This is disp() function.")

def msg():
    print("This is msg() function.")

function_list = [fun, disp, msg]

for func in function_list:
    func()


# 2. Add Corresponding Elements of Two Lists Using `map` and `lambda`
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]

result = list(map(lambda x, y: x + y, list1, list2))

print("2. Result of adding corresponding elements:", result)


# 3. Generate 10 Random Numbers Between -15 and 15, and Obtain the Square of Each Number

import random
random_numbers = [random.randint(-15, 15) for _ in range(10)]
squared_numbers = list(map(lambda x: x ** 2, random_numbers))

print("3. Random Numbers:", random_numbers)
print("Squared Numbers:", squared_numbers)


# 4. Print Strings Which Are Palindromes
lst = ['madam', 'Python', "malayalam", 12321]

def is_palindrome(word):
    return str(word) == str(word)[::-1]

palindromes = list(filter(is_palindrome, lst))
print("4. Palindromes in the list:", palindromes)


# 5. Filter Names with More Than 8 Characters
faculty_members = ['John', 'Alice', 'Alexander', 'Michael', 'Jonathan', 'Anna']
long_names = list(filter(lambda name: len(name) > 8, faculty_members))

print("5. Names with more than 8 characters:", long_names)
