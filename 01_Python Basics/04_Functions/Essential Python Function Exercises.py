"""
# Description of the Task
This practice task involves creating several functions and a lambda function in Python to cover different concepts such as docstrings, multiple arguments, default arguments, lambda functions, positional and keyword arguments, returning multiple values, using one function within another, and higher-order functions.
Function with Docstring 
Function with Multiple Arguments
Function with Default Argument 
Lambda Function 
Function with Positional and Keyword Arguments 
Function Using Another Function 
Higher-Order Function 

# Instructions
Write a function greet that takes a name as an argument and prints a greeting message. Include a docstring that describes what the function does.
Write a function add_numbers that takes two arguments and returns their sum. Include a docstring that describes what the function does.
Write a function introduce that takes two arguments: name and age, with age having a default value of 18. The function should print a message introducing the person.
Write a lambda function that takes two arguments and returns their product. Assign this lambda function to a variable multiply and use it to multiply two numbers.
Write a function describe_pet that takes a pet's name (positional argument) and an optional keyword argument animal_type with a default value of 'dog'. The function should print a message describing the pet.
Write a function rectangle_properties that takes the length and width of a rectangle and returns its area and perimeter.
Write a function circle_area that takes the radius of a circle and returns its area. Then write another function cylinder_volume that uses circle_area to calculate the volume of a cylinder given its radius and height.
Write a function apply_function that takes another function and a value as arguments, and returns the result of applying the given function to the value. Test it with a lambda function.

# Learning Objective
Understand and implement functions with docstrings.
Learn how to handle multiple arguments in functions.
Use default arguments in functions.
Create and use lambda functions.
Differentiate between positional and keyword arguments.
Return multiple values from a function.
Implement a function that uses another function.
Understand and use higher-order functions.


## ----------- Sample Usage

# ----------- Function with Docstring : greet Function
# Example usage:
greet("Alice")
# Expected output:
# Hello, Alice!

# ----------- Function with Multiple Arguments: add_numbers Function
# Example usage:
result = add_numbers(3, 4)
print(result)
# Expected output:
# 7

# ----------- Function with Default Argument: introduce Function
# Example usage:
introduce("Bob")
# Expected output:
# My name is Bob and I am 18 years old.

# ----------- Lambda Function:  Multiplication
# Example usage:
result = multiply(3, 5)
print(result)
# Expected output:
# 15

# ----------- Function with Positional and Keyword Arguments: describe_pet Function
# Example usage:
describe_pet("Buddy")
# Expected output:
# I have a dog named Buddy.

# ----------- Function Returning Multiple Values: rectangle_properties Function
# Example usage:
area, perimeter = rectangle_properties(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")
# Expected output:
# Area: 15, Perimeter: 16

# ----------- Function Using Another Function: circle_area and cylinder_volume Functions
# Example usage:
volume = cylinder_volume(3, 5)
print(f"Volume: {volume}")
# Expected output:
# Volume: 141.37185

# ----------- Higher-Order Function: apply_function Function
# Example usage:
result = apply_function(lambda x: x * x, 4)
print(result)
# Expected output:
# 16

"""