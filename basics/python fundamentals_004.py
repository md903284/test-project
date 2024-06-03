# Defining a function

def greet ():
    # this body of the function
    print('HOW ARE YOU')
greet()

# Docstring

def greet ():
    """
    This function greets everyone when it is called
    """
    print('HOW ARE YOU')
greet()

# parameters
def greet (name):
    print('HOW ARE YOU', name)
greet("rahul")


def add (a,b):
    c = a + b
    print (c)
    print (a, b)
add (2,5)


def add (a,b):
    c = a + b
    print (c)
add (2,5)


# Return vs print
def add (a,b):
    c = a + b
    print (c)

add (3,7)
add = add (3,7)
type(print(10))


def add (a,b):
    c = a + b
    return c

b = add (3,7)
print (b,type(b))


# code after return statement doesn't get executed

def func () :
    print ("before return")
    return "rahul"
    print ("after return")
func ()


# returning multiple values

def intro (name, age, hobby):
    return name,age,hobby
c,d,e = intro ("manoj", 24, "travel")
print (c,d,e)

c = intro ("manoj", 24, "travel")
print (c,type(c))


# scope of variable

# a can be used anywhere in the program

a = 5
def func ():
    print(a)
func()
print(a)


a = 5

def func ():
    # x is a local variable to this function
    x = 3
    print(x)
func ()
print(a)
#print(x)

a = 5
def func ():
    a = 20
    print(a)
func()
print(a)



a = 5
def func ():
    global a
    a = 20
    print(a)
print(a)
func()
print(a)



# lambda function

def add (a,b) :
    return a+b

add (3,4)
(lambda a,b : a+b)(3,4)

def larger (a,b):
    if a>b:
        return a
    else :
        return b
larger (4,5)