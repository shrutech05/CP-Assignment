#1 Print all alphabets in upper case and in lower case
print("Uppercase Letters:")
for i in range(65, 91):
    print(chr(i), end=" ")
print("\nLowercase Letters:")
for i in range(97, 123):
    print(chr(i), end=" ")

#2 Print multiplication table of a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#3 Count number of alphabets and digits in a string
string = input("Enter a string: ")
alphabets = digits = 0
for ch in string:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
print("Alphabets:", alphabets)
print("Digits:", digits)

#4 Check number properties (prime, perfect, armstrong, palindrome, automorphic)
num = int(input("Enter a number: "))

# Prime
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break

# Perfect
sum_factors = sum(i for i in range(1, num) if num % i == 0)
is_perfect = sum_factors == num

# Armstrong
n = num
order = len(str(n))
armstrong = sum(int(d)**order for d in str(n)) == n

# Palindrome
is_palindrome = str(num) == str(num)[::-1]

# Automorphic
square = num ** 2
is_automorphic = str(square).endswith(str(num))

print("Prime:", is_prime)
print("Perfect:", is_perfect)
print("Armstrong:", armstrong)
print("Palindrome:", is_palindrome)
print("Automorphic:", is_automorphic)

#5 Generate all Pythagorean Triplets with side length <= 30
for a in range(1, 31):
    for b in range(a, 31):
        c = (a**2 + b**2) ** 0.5
        if c.is_integer() and c <= 30:
            print(f"{a}, {b}, {int(c)}")

#6 Print 24 hours of day with suffixes
for hour in range(0, 24):
    if hour == 0:
        print("12 AM - Midnight")
    elif hour == 12:
        print("12 PM - Noon")
    elif hour < 12:
        print(f"{hour} AM")
    else:
        print(f"{hour - 12} PM")

#7 Print nCr and nPr
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = int(input("Enter n: "))
r = int(input("Enter r: "))

ncr = factorial(n) // (factorial(r) * factorial(n - r))
npr = factorial(n) // factorial(n - r)

print("nCr =", ncr)
print("nPr =", npr)

#8 Print factorial of a given number
num = int(input("Enter a number: "))
fact = 1
for i in range(2, num + 1):
    fact *= i
print("Factorial:", fact)

#9 Print N natural numbers in reverse
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(i, end=" ")

#10 Generate N numbers of Fibonacci series
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#11 Calculate sin(x) using Taylor series (x in degrees)
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def sin_x(x_deg, terms=10):
    x = x_deg * 3.14159 / 180  # Convert to radians
    result = 0
    for i in range(terms):
        sign = (-1) ** i
        term = (x ** (2*i + 1)) / factorial(2*i + 1)
        result += sign * term
    return result

x = float(input("Enter angle in degrees: "))
print("sin(x):", sin_x(x))
