#1 Count Boys and Girls
people = [("rahul", "don"), "rohit", "rishi", ("dhoni", "Ryan")]
boys = girls = 0

for person in people:
    if isinstance(person, tuple):
        boys += len(person)
    else:
        girls += 1

print("Number of boys:", boys)
print("Number of girls:", girls)

#2 Split Tuple List into Separate Lists
students = [(1, "zara", 18), (2, "sam", 19), (3, "aakash", 17)]

roll_nos = [s[0] for s in students]
names = [s[1] for s in students]
ages = [s[2] for s in students]

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)


#3 Days Between Two Dates (tuples)
from datetime import date

date1 = (24, 4, 2025)
date2 = (1, 5, 2025)

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

delta = abs((d2 - d1).days)
print("Number of days between the two dates:", delta)


#4 Sort Food Items by Price (Descending)
food_prices = [("Burger", 120), ("Pizza", 250), ("Fries", 90), ("Sandwich", 150)]
sorted_items = sorted(food_prices, key=lambda x: x[1], reverse=True)

print("Food items sorted by price (high to low):")
for item in sorted_items:
    print(item)


#5 Remove Empty Tuples
python
Copy
Edit
tuple_list = [(), (1, 2), (), (3,), (), (4, 5)]
filtered = [t for t in tuple_list if t]

print("After removing empty tuples:", filtered)


#6 Modify an Element of a Tuple
t = (1, 2, 3)
t_list = list(t)
t_list[1] = 99
t = tuple(t_list)

print("Modified tuple:", t)


#7 Delete an Element of a Tuple
t = (10, 20, 30, 40)
t_list = list(t)
del t_list[2]
t = tuple(t_list)

print("Tuple after deletion:", t)
