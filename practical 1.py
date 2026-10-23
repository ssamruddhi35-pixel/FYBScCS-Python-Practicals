Q1. Variable Creation and Naming Rules
name = "Rahul"
age = 18
marks = 85.5
city = "Mumbai"

print("Name:", name)
print("Age:", age)
print("Marks:", marks)
print("City:", city)

Q2. Dynamic Typing in Python
x = 10
print(x, type(x))

x = "Python"
print(x, type(x))

x = 10.5
print(x, type(x))

Q3. Constants Simulation
PI = 3.14
GRAVITY = 9.8
MAX_USERS = 100

print("PI:", PI)
print("Gravity:", GRAVITY)
print("Maximum Users:", MAX_USERS)

# Python does not strictly enforce constants.
# Capital letters indicate that values should not change.

Q4. Data Type Identification System
a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))
c = input("Enter a string: ")
d = input("Enter True or False: ")

d = d == "True"

print("Value:", a, "Type:", type(a))
print("Value:", b, "Type:", type(b))
print("Value:", c, "Type:", type(c))
print("Value:", d, "Type:", type(d))

print("\nValue\t\tType")
print(a, "\t\t", type(a))
print(b, "\t\t", type(b))
print(c, "\t\t", type(c))
print(d, "\t\t", type(d))


Q5. Type Conversion (Casting)
age = input("Enter your age: ")
marks = input("Enter your marks: ")

age = int(age)
marks = float(marks)

print("Age:", age)
print("Marks:", marks)
print("Age after 5 years:", age + 5)
print("Marks after adding 5:", marks + 5)


Q6. Implicit vs Explicit Type Conversion
a = 10
b = 5.5

print("Addition:", a + b)

# int + string gives an error
# print(a + "5")

# Explicit conversion
print("Corrected addition:", a + int("5"))

Q7. Memory Behaviour of Variables
a = 10
b = 10

print("ID of a:", id(a))
print("ID of b:", id(b))

a = 20

print("Value of a:", a)
print("Value of b:", b)

Q8. Swapping Variables Using Two Methods
Method 1: Using a third variable
a = 10
b = 20

temp = a
a = b
b = temp

print("After swapping:", a, b)
Method 2: Using tuple unpacking
a = 10
b = 20

a, b = b, a

print("After swapping:", a, b)

Q9. Data Type-Based Calculator
try:
    a = input("Enter first value: ")
    b = input("Enter second value: ")

    if a.replace(".", "", 1).isdigit() and b.replace(".", "", 1).isdigit():
        a = float(a)
        b = float(b)
        print("Addition:", a + b)
    else:
        print("Concatenation:", a + b)

except ValueError:
    print("Invalid input")

Q10. Boolean Logic and Data Types
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

adult = age > 18
passed = marks > 50

print("Adult:", adult)
print("Passed:", passed)

if passed:
    print("Student has passed")
else:
    print("Student has not passed")

Q11. Temperature Converter
c = float(input("Enter temperature in Celsius: "))

f = (c * 9 / 5) + 32

print("Temperature in Fahrenheit: {:.2f}".format(f))

































