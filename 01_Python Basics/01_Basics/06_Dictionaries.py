"""
# Description of the Task: 
Create a Python program that demonstrates the use of dictionaries. Dictionaries are a fundamental data structure in Python used to store key-value pairs.

# Instructions:
Create a dictionary to store information about a person. Include keys such as "name", "age", "city", "country", etc.
Print the dictionary.
Update the dictionary to include additional information.
Print the updated dictionary.
Access and print specific values from the dictionary using their keys.

# Learning Objective:
Understanding dictionaries and their syntax in Python.
Practicing dictionary manipulation including adding, updating, and accessing key-value pairs.
"""

information = {
            "name": "manoj",
            "age": 24,
            "city": "hyderabad",
            "country": "india"
            }


print(information)


# Updating the dictionary to include additional information.

information["name"]={"manojdomala"}
information["city"]={"hyderabad,charminar"}
print(information["name"])
print(information["city"])

 # Accessing the specific values from the dictionary using their keys.

print(information["age"])
print(information["city"])



