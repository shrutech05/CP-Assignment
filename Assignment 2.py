import math

# 1. Largest and smallest of two
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest:", a, "Smallest:", b)
elif b > a:
    print("Largest:", b, "Smallest:", a)
else:
    print("Both are equal.")

# 2. Largest and smallest of three
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
largest = x
smallest = x
if y > largest:
    largest = y
if z > largest:
    largest = z
if y < smallest:
    smallest = y
if z < smallest:
    smallest = z
print("Largest:", largest, "Smallest:", smallest)

# 3. Odd or even
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4. Divisible by 10
n = int(input("Enter a number: "))
if n % 10 == 0:
    print("Divisible by 10")
else:
    print("Not divisible by 10")

# 5. Age check
age = int(input("Enter age: "))
if age < 18:
    print("Minor")
else:
    print("Major")

# 6. Number of digits
num = int(input("Enter a number: "))
count = 0
temp = abs(num)
while temp > 0:
    count += 1
    temp = temp // 10
if num == 0:
    count = 1
print("Number of digits:", count)

# 7. Leap year
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 8. Triangle validity
a1 = int(input("Enter angle 1: "))
a2 = int(input("Enter angle 2: "))
a3 = int(input("Enter angle 3: "))
if a1 + a2 + a3 == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

# 9. Absolute value
n = int(input("Enter a number: "))
if n < 0:
    print("Absolute value:", -n)
else:
    print("Absolute value:", n)

# 10. Rectangle area vs perimeter
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
area = l * b
peri = 2 * (l + b)
if area > peri:
    print("Area is greater than Perimeter")
else:
    print("Perimeter is greater than or equal to Area")

# 11. Check collinear points
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))
if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("Points are collinear")
else:
    print("Points are not collinear")

# 12. Point and circle
cx = int(input("Enter circle center x: "))
cy = int(input("Enter circle center y: "))
radius = float(input("Enter radius: "))
px = int(input("Enter point x: "))
py = int(input("Enter point y: "))
distance = math.sqrt((px - cx)**2 + (py - cy)**2)
if distance < radius:
    print("Point is inside the circle")
elif distance == radius:
    print("Point is on the circle")
else:
    print("Point is outside the circle")

# 13. Number to word (0-19)
n = int(input("Enter a number (0 to 19): "))
words = ["zero", "one", "two", "three", "four", "five", "six", "seven",
         "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
if 0 <= n <= 19:
    print("In words:", words[n])
else:
    print("Out of range")

# 14. Student marks and result
m1 = input("Enter marks for subject 1 (or 'Absent'): ")
m2 = input("Enter marks for subject 2 (or 'Absent'): ")
m3 = input("Enter marks for subject 3 (or 'Absent'): ")

def convert_marks(m):
    if m.lower() == "absent":
        return -1
    return int(m)

mark1 = convert_marks(m1)
mark2 = convert_marks(m2)
mark3 = convert_marks(m3)

marks = [mark1, mark2, mark3]
total = 0
count = 0
grades = []

for m in marks:
    if m == -1:
        grades.append("NA")
    else:
        total += m
        count += 1
        if m <= 39:
            grades.append("F")
        elif m <= 44:
            grades.append("P")
        elif m <= 49:
            grades.append("C")
        elif m <= 54:
            grades.append("B")
        elif m <= 59:
            grades.append("B+")
        elif m <= 69:
            grades.append("A")
        elif m <= 79:
            grades.append("A+")
        elif m <= 100:
            grades.append("O")
        else:
            grades.append("Invalid")

if -1 in marks:
    print("One or more subjects marked 'Absent'")
else:
    average = total / 3
    if mark1 <= 39 or mark2 <= 39 or mark3 <= 39:
        result = "Fail"
    else:
        result = "Pass"
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grades:", grades)
    print("Result:", result)
