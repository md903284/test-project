"""
# Description of the Task
Write a Python program that:
Takes two string inputs from the user: a main string and a substring.
Checks if the substring is present in the main string.
Prints the starting index of the substring if found, or a message indicating it is not found.

# Instructions
Prompt the user to enter the main string.
Prompt the user to enter the substring.
Use Python string methods to determine if the substring is present in the main string.
If the substring is found, print the starting index of the first occurrence of the substring.
If the substring is not found, print an appropriate message.

# Learning Objective
The objective of this task is to practice working with Python strings, 
particularly string searching methods like find() or index(). 
This task helps in understanding how to manipulate and search within strings.

# Sample Usage
Enter the main string: Hello, welcome to the world of Python!
Enter the substring: welcome
Output: The substring 'welcome' is found at index 7.
"""

# Prompt the user to enter the main string
main_string = input("Enter the main string: ")
# Prompt the user to enter the substring
substring = input("Enter the substring: ")
# Check if the substring is in the main string
index = main_string.find(substring)
# Print the result
if index != -1:
    print(f"The substring '{substring}' is found at index {index}.")
else:
    print(f"The substring '{substring}' is not found in the main string.")