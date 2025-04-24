#1 Odd & Even Lists: Replace, Flatten, Sort
import random

odd_list = [random.randint(1, 99) | 1 for _ in range(5)]
even_list = [random.randint(1, 99) & ~1 for _ in range(4)]
print("Original Odd List:", odd_list)
print("Original Even List:", even_list)

odd_list[2] = even_list
print("After Replacement (Nested):", odd_list)

flat_list = []
for item in odd_list:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)
print("Flattened List:", flat_list)

flat_list.sort()
print("Sorted List:", flat_list)

#2 Find Positions of All Occurrences
lst = [random.randint(1, 10) for _ in range(20)]
print("List:", lst)

num = int(input("Enter number to find: "))
positions = [i for i, val in enumerate(lst) if val == num]
print(f"Positions of {num}:", positions if positions else "Not found")

#3 Remove Duplicates from Random List
nums = [random.randint(1, 30) for _ in range(50)]
print("Original List with Duplicates:", nums)
unique_nums = list(set(nums))
print("List after removing duplicates:", unique_nums)

#4 Separate +ve and -ve Numbers
numbers = [random.randint(-50, 50) for _ in range(30)]
positive = [n for n in numbers if n >= 0]
negative = [n for n in numbers if n < 0]
print("Original List:", numbers)
print("Positive Numbers:", positive)
print("Negative Numbers:", negative)

#5 Convert List of Strings to Uppercase
words = ["apple", "banana", "grape", "kiwi", "melon"]
upper_words = [word.upper() for word in words]
print("Original List:", words)
print("Uppercase List:", upper_words)

#6 Fahrenheit to Celsius Conversion
fahrenheit_list = [32, 68, 77, 100, 212]
celsius_list = [round((f - 32) * 5 / 9, 2) for f in fahrenheit_list]
print("Fahrenheit:", fahrenheit_list)
print("Celsius:", celsius_list)

#7 Stack Implementation (Menu-Driven)
stack = []
while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        value = input("Enter value to push: ")
        stack.append(value)
    elif choice == '2':
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty")
    elif choice == '3':
        print("Stack:", stack)
    elif choice == '4':
        break
    else:
        print("Invalid choice")

#8 Queue Implementation (Menu-Driven)
queue = []
while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        value = input("Enter value to enqueue: ")
        queue.append(value)
    elif choice == '2':
        if queue:
            print("Dequeued:", queue.pop(0))
        else:
            print("Queue is empty")
    elif choice == '3':
        print("Queue:", queue)
    elif choice == '4':
        break
    else:
        print("Invalid choice")

#9 List Comprehension: Elements in L1 but not in L2
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [x for x in list1 if x not in list2]
print("List1:", list1)
print("List2:", list2)
print("Elements in List1 not in List2:", list3)
