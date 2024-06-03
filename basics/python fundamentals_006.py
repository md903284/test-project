# file handling 

# "r": read only
# "w" : write only
# "a" : appending data at the end of file
# "wt" : write text
# "wb" : write binary
# "rb" : read binary
# "rt" : read text

f=open("name.txt")
f.read()
f.close()

f=open("name.txt","w")
f.write("my age is")
f.close()


with open("name.txt") as f :
    print(f.read())
f.closed

with open("name.txt","w") as f :
    f.write("this is manoj")

with open ("new.txt","w") as f:
    f.write("my name is manoj")

# write in existing file

with open ("new.txt","w") as f:
    f.write("my name is manoj \n")
    f.write("my age is ")

with open("new.txt","r") as f:
    data = f.read()
    print(data)


with open("name.txt","a") as f :
    f.write("this is manoj")

with open("charminar.jpg","rb") as f:
    data = f.read()
    print(data)

    with open ("new.jpg", "wb") as d:
        d.write(data)


#Error & Exception Handling

# syntax error
# Name error
# type error
# file not found
# indentation error
# zero division error


print(dir(__builtins__))

 # Try & except

a=5
b=0
# put the suspect code in try block
try:
    print(a/b)
except:
    print("hello world")


a=5
b=2
# put the suspect code in try block
try:
    print(a/b)
except:
    print("hello world")

 # except
a=5
b=2
# put the suspect code in try block
try:
    print(2+"2")
except:
    print("hello world")

# finally

a=5
b=5
# put the suspect code in try block
try:
    print("open file")
    print(a/b)
except Exception as e :
    print("hello world",e)

finally:
    print("close file")


