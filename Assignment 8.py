# 1. Convert Words in a List to Uppercase and Store Them in a Set
words_list = ['apple', 'banana', 'cherry', 'date']
uppercase_set = {word.upper() for word in words_list}
print("1. Set with words in uppercase:", uppercase_set)


# 2. Create a Set with Random Numbers, Count Numbers Less Than 30, and Delete Numbers Greater Than 35
import random
random_numbers = {random.randint(15, 45) for _ in range(10)}

print("2. Random Numbers Set:", random_numbers)

less_than_30 = sum(1 for num in random_numbers if num < 30)
print("Count of numbers less than 30:", less_than_30)

random_numbers = {num for num in random_numbers if num <= 35}

print("Set after deleting numbers greater than 35:", random_numbers)


# 3. Add, Modify, and Delete Names in a Set
# Create an empty set
names_set = set()

# Add five new names to the set
names_set.update(['John', 'Alice', 'Bob', 'Charlie', 'Diana'])

# Modify one existing name (change 'Bob' to 'Robert')
names_set.discard('Bob') # Remove 'Bob' if it exists
names_set.add('Robert')

# Delete two names from the set
names_set.discard('Alice') # Remove 'Alice'
names_set.discard('Charlie') # Remove 'Charlie'

print("3. Final Names Set:", names_set)


# 4. Separate Names Starting with 'A' and 'B' into Two Sets
# Set with names starting with A or B
names_set = {'Alice', 'Bob', 'Andrew', 'Bella', 'Charlie', 'David'}

# Separate names into two sets: one starting with 'A' and the other with 'B'
names_A = {name for name in names_set if name.startswith('A')}
names_B = {name for name in names_set if name.startswith('B')}

print("4. Names starting with A:", names_A)
print("4. Names starting with B:", names_B)
