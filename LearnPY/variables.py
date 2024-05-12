# Variables in python

name="John"
print(name)
name="sam"
print(name)

x = 4
x = "4"

x=str(5)
print(x)
print(type(x))

casesensetive = "Hello"
Casesenesetive = "World"

print(casesensetive, Casesenesetive)
print(type(casesensetive, Casesenesetive))


# global variable

xy = "awesome"

def myfunc():
    # local variable
    yx = "fantastic"
    print("Python is " + xy)
    

print(xy)

# Change a global variable from inside a function

k = "awesome"

def myfunc():
    global k
    k = "fantastic2"
    print("Python is " + k)

print(k)
myfunc()
print(k)
