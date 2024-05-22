Name = "manoj domala"
size = len(Name)
print (Name[-size])
print (size)

# String Slicing

name = " manoj kumar"
name [0:6]
size = len(name)
name[3:size]


# capitalize
name = "manoj"
print (name.capitalize())

# title

name= "manoj is name"
print(name.title())

# upper
name = "i'm doing good"
print (name.upper())

# lower

name = "I'M DOING GOOD"
print (name.lower())

# find

name = "I'M DOING GOOD"
print (name.find("O"))


# find

name ='manoj is my name'
print (name.find('is'))

# count

name = "is this good for us"
print (name.count("o"))

# index 
name = "is this good for us"
print (name.index ("f"))

# replace

name = "is this good for us"
print (name.replace("us","me"))

# split

name = "is this good for us"
lst=name.split()
print (lst)

# islower
name = "is this good for us"
lst=name.islower()
print (lst)

# isupper
name = "is this good for us"
lst=name.isupper()
print (lst)


# isnumeric
name = "is this good for us"
lst=name.isnumeric()
print (lst)

# isalpha
name = "is this good for us"
lst=name.isalpha()
print (lst)

# formatting

name = "manoj"
age = 25

print ("my name is {} and my age is {}" .format(name,age))


# Concatenation

first = 2
second = 15

print (first+second)



#list

l = list()
print (type(l))


l1 = [1,6,8,2]
print(type(l1))

l = [1,2,3,4,5,6,7,9]
print(len(l))


l = [1,2,3,4,5,6,7,9]
l[0:3]
print(len(l))


name= [200,300,700,500]
print(name.count(100))

# index 

name= [200,300,700,500]
print(name.index(500))

# pop

name= [200,300,700,500]
print(name.remove(200))


l = [1,2,3,4,5]
l.append("manu")
print (l)

l = [1,2,3,4,5, "manu"]
l1 = [6,7]
l.append(l1)
print (l)


# dictionary

d = {}
print (type(d))
print (d)


pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}
print (type(d))
print (pets)

#zip

name = ["dog", "rat", "cat"]
prices = [12,13,15]
pets = dict(zip(name, prices))
print (pets)


name = ["dog", "rat", "cat"]
prices = [12,13,15]
pets = dict(zip(name, prices))
print (len(pets))


pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}
print (pets["dog"])
print (pets["rat"])

# method
name = ["dog", "rat", "cat"]
prices = [12,13,15]
print (pets.get("dog"))
print (pets.get("cat"))

# Updating dictionary

pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}

pets ["dog"] = {"puppy": 50, "adult" : 100}
print (pets)


pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}

pets ["dog"] = {"puppy": 50, "adult" : 100}
pets ["rabbit"]= 80
print (pets)

# new dictionary

pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}
new= {"pig" : 2, "bird" : 5}
pets ["dog"] = {"puppy": 50, "adult" : 100}
pets ["rabbit"]= 80
pets.update(new)
print (pets)


# Deletion Operations in Dictionary

pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}

pets.pop("dog")
print (pets)

# pop item 


pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}

pets.popitem()
print (pets)
pets.popitem()
print (pets)
pets.popitem()
print (pets)


 #Iteration in Dictionary

pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}
for i in pets :
    print(i , pets[i], end=" ")

# More Dictionary Methods

pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}
pets.keys()
print (pets)

pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}
pets.values()
print (pets)



pets = {
    "dog" : 12,
    "cat" : 13,
    "rat" : 15
}
pets.items()
print (pets)