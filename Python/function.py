#creating a function to calculate area of circle
# taking radius as input from the user
#importing math module for using pi in calculations 
import math
def area_of_circle(radius):
    return math.pi * (radius ** 2)      
print("Enter the value of radius:")
r=int(input())
print("The area of the circle is:",area_of_circle(10))

def greet(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message
print(greet("Geeks"))


def greet(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message
print(greet("Geeks"))


def print_values(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_values(1, 2, 3, name="Rose", age=24)

# nested  functions

def func_1(x):
    S = "Data Science with Python"
    def func_2():
        return (S,x)
    return func_2()

# Create a closure
closure = func_1(3.0)

print(closure)

# recursive
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)