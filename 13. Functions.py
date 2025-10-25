#  Function is a block of code which only runs when it is called
#  function has a name for identification

#   FUNCTION DEFINITION
"""
def functionName(args): HERE def IS A KEYWORD
    "code"
    "code"
"""
    
#   FUNCTION CALLING VS FUNCTION DEFINITION

# This is function definition
def f1():
    a=int(input("Enter your Number"))
    b=a**2
    print("Squre of",a,"is",b)    
    
# this is function calling. once function is called it can be call any number of times.
f1()
f1()
f1()


#       WAYS TO DEFINE FUNCTION
#  There are 4 ways to define a function.
#  1. takes nothing. returns nothing
#  2. takes something. returns nothing
#  3. takes nothing. returns something
#  4. takes something. returns something

# 1. TAKES NOTHING RETURNS NOTHING
def add():         # we take nothing in the args
    print("enter two numbers")
    a=int(input())      # these variables which in defined within function is called local variables
    b=int(input())
    c=a+b
    print("sum is",c)
add()
x=10  # these variables called outside function is called global variables



# 2. TAKES SOMETHING, RETURNS NOTHING(in this we takes args but return nothing)
def add(a,b):
    c=a+b
    print("sum is",c)
add(5,6)




# 3. TAKES NOTHIING, RETURNS SOMETHING( IN THESE WE DONT TAKE ANY ARGS BUT RETURN SOMETHING)
def add():
    a=int(input("enter your first number"))
    b=int(input("enter your second number"))
    c=a+b
    return c
s=add()
print(s)



# 4. TAKES SOMETHING, RETURNS SOMETHING
def add(a,b):
    c=a+b
    return c
s=add(4,5)
print(s)


