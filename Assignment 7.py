# 1. Concatenate Three Dictionaries to Create a Fourth Dictionary
dict1 = {'A': 1, 'B': 2}
dict2 = {'C': 3, 'D': 4}
dict3 = {'E': 5, 'F': 6}

dict4 = {**dict1, **dict2, **dict3}

print("1. Fourth Dictionary:", dict4)

# 2. Check if a Dictionary is Empty or Not
# Function to check if a dictionary is empty
def is_empty(d):
    return len(d) == 0
my_dict = {}

if is_empty(my_dict):
    print("2. The dictionary is empty.")
else:
    print("2. The dictionary is not empty.")

# 3. Department-wise Min and Max Salary
dept_salaries = {
    'IT': [(101, 50000), (102, 60000), (103, 45000)],
    'HR': [(201, 55000), (202, 62000), (203, 49000)],
    'Finance': [(301, 70000), (302, 75000), (303, 69000)]
}

def dept_salary_stats(dept_salaries):
    for dept, employees in dept_salaries.items():
        salaries = [emp[1] for emp in employees]
        print(f"3. {dept} - Min Salary: {min(salaries)}, Max Salary: {max(salaries)}")

dept_salary_stats(dept_salaries)

# 4. Frequency of Each Character in a String
def char_frequency(string):
    freq_dict = {}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
            else:
                freq_dict[char] = 1
        return freq_dict

input_string = input("Enter a string for program 4: ")
frequency = char_frequency(input_string)

print("4. Character Frequency:", frequency)

# 5. Compute Total Bill Using Grocery Dictionaries
grocery_prices = {'apple': 2, 'banana': 1, 'orange': 3, 'milk': 1.5}

grocery_quantity = {'apple': 3, 'banana': 2, 'orange': 1, 'milk': 4}

def total_bill(prices, quantities):
    total = 0
    for item in prices:
        if item in quantities:
            total += prices[item] * quantities[item]
    return total

bill = total_bill(grocery_prices, grocery_quantity)

print("5. Total Bill: $", bill)
