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
larger (43,5)

# challenge

def even (li):
    #iterate on the list li
    for i in li :
        # check for even elements
        if i % 2 == 0:
            print (i, end=" ")
lst = [1,2,3,4,5,6]
even (lst)


 # Challenge: Return List with Unique Numbers
    
lst = [1,2,3,1,2,4]

def unique (li):
     new = []
     #iterate on the list li
     for i in li:
         if i not in new :
             new.append(i)
     return new
unique(lst)


# Arguments vs Parameters in Functions


def func (Name) :
    print ("my name is",Name)
func("manoj")


# Positional Arguments

def intro (name,hobby):
    print("my name is", name)
    print ("my hobby is", hobby)
intro ("manoj","play")

# Default Arguments

def intro (name,hobby= "gaming"):
    print("my name is", name)
    print ("my hobby is", hobby)
intro ("manoj")


with open("new.tex", "w") as f :
    f.write ("new file created")








def intro (name,hobby= "gaming", age = 24):
    print("my name is", name)
    print ("my hobby is", hobby)
intro ("manoj")



