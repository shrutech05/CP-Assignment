# 1. Add two numbers
a, b = 86, 54
print("Add:", a + b)

# 2. Subtract two numbers
print("Subtract:", a - b)

# 3. Multiply two numbers
print("Multiply:", a * b)

# 4. Divide two numbers
print("Divide:", a / b)

# 5. All operations
print("Add:", a + b)
print("Multiply:", a * b)
print("Subtract:", a - b)
print("Divide:", a / b)

# 6. Convert hours into minutes
hours = 5
print("Minutes:", hours * 60)

# 7. Convert minutes into hours
minutes = 270
print("Hours:", minutes / 60)

# 8. Convert dollars into Rs (1$ = 48 Rs)
dollars = 56
print("Rs:", dollars * 48)

# 9. Convert Rs into dollars (1$ = 48 Rs)
rupees = 432
print("Dollars:", rupees / 48)

# 10. Convert dollars into pounds (1$ = 48 Rs, 1 pound = 70 Rs)
print("Pounds:", (dollars * 48) / 70)

# 11. Convert grams into kg
grams = 1000
print("Kg:", grams / 1000)

# 12. Convert kg into grams
kg = 8
print("Grams:", kg * 1000)

# 13. Convert bytes into KB, MB and GB
bytes_val = 1048576  # 1MB
print("KB:", bytes_val / 1024)
print("MB:", bytes_val / (1024**2))
print("GB:", bytes_val / (1024**3))

# 14. Convert Celsius into Fahrenheit
celsius = 60
fahrenheit = (9/5 * celsius) + 32
print("Fahrenheit:", fahrenheit)

# 15. Convert Fahrenheit into Celsius
f = 77
c = 5/9 * (f - 32)
print("Celsius:", c)

# 16. Calculate interest (I = PRN/100)
P, R, N = 1000, 10, 6
I = P * R * N / 100
print("Interest:", I)

# 17. Area and perimeter of square (A = L^2, P = 4L)
L = 7
print("Square Area:", L ** 2)
print("Square Perimeter:", 4 * L)

# 18. Area and perimeter of rectangle (A = L*B, P = 2(L+B))
L, B = 2, 3
print("Rectangle Area:", L * B)
print("Rectangle Perimeter:", 2 * (L + B))

# 19. Area of circle (A = 22/7 * R * R)
R = 7
print("Circle Area:", 22/7 * R * R)

# 20. Area of triangle (A = H * L / 2)
H, L = 6, 18
print("Triangle Area:", H * L / 2)

# 21. Calculate net salary
gross_salary = 70000
allowance = gross_salary * 0.10
deduction = gross_salary * 0.03
net_salary = gross_salary + allowance - deduction
print("Net Salary:", net_salary)

# 22. Net sales = gross sales – 10% discount
gross_sales = 600000
discount = gross_sales * 0.10
net_sales = gross_sales - discount
print("Net Sales:", net_sales)

# 23. Average and total of three subjects
s1, s2, s3 = 80, 70, 95
total = s1 + s2 + s3
average = total / 3
print("Total Marks:", total)
print("Average Marks:", average)

# 24. Swap two values
x, y = 27, 23
x, y = y, x
print("Swapped values: x =", x, "y =", y)
