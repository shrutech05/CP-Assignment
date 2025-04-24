#1 Complex Number Operations
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

# Example Usage:
a = ComplexNumber(3, 4)
b = ComplexNumber(1, 2)
result = a.add(b)
print("Addition:", result)



#2 Matrix Operations
class Matrix:
    def __init__(self, data):
        self.data = data

    def add(self, other):
        for i in range(3):
            for j in range(3):
                self.data[i][j] += other.data[i][j]
        return self

    def display(self):
        for row in self.data:
            print(row)
# Example Usage:
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix1.add(matrix2).display()

#3 Surface Area and Volume of a Solid
class Solid:
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * 3.14 * self.radius ** 2

    def volume(self):
        return (4/3) * 3.14 * self.radius ** 3
# Example Usage:
solid = Solid(5)
print("Surface Area:", solid.surface_area())
print("Volume:", solid.volume())


#4 Perimeter and Area of a Regular Shape
class Shape:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius ** 2
# Example Usage:
circle = Shape(3)
print("Perimeter:", circle.perimeter())
print("Area:", circle.area())

#5  Time Arithmetic Operations
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add(self, other):
        total_minutes = self.minutes + other.minutes
        hours = self.hours + other.hours + total_minutes // 60
        minutes = total_minutes % 60
        return Time(hours, minutes)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"
# Example Usage:
time1 = Time(10, 45)
time2 = Time(3, 30)
result = time1.add(time2)
print("Added Time:", result)

#6 Date Comparison
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year
# Example Usage:
date1 = Date(1, 4, 2025)
date2 = Date(1, 4, 2025)
print("Dates are equal:", date1 == date2)

#7 Weather Class
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters
# Example Usage:
weather = Weather(["temperature", "humidity"])
print("temperature" in weather)  # True

#8 String Operations
class String:
    def __init__(self, text):
        self.text = text

    def concat(self, other):
        return String(self.text + other.text)

    def toLower(self):
        return self.text.lower()

    def toUpper(self):
        return self.text.upper()
# Example Usage:
s1 = String("Hello")
s2 = String(" World")
result = s1.concat(s2)
print("Concatenated String:", result.text)
print("Lowercase:", s1.toLower())
print("Uppercase:", s2.toUpper())

