# Function calling itself is called Recursion

""" 
def f1():
    print("Hi")
    f1()    # Recursive case
    print("Bye")
 
"""
# we have not create a situation where recursion can end

# BASE CASE :-- Base Case is a condition from where recursion ends and backtrack

def f1(n):
    if n==1:
        return 1
    s=n+f1(n-1)
    return s
f1(4)

"""in this code base case is :if n==1:
                                return 1"""
                                
""" HOW TO APPROACH RECURSION

1, DEFINE THE BASE CASE
2, CALL THE FUNCTION ITSELF
"""

# ex-- sum of squre of n natural number
def SumSqure(n):
    if n==1:
        return 1
    return n**2+SumSqure(n-1)
x=SumSqure(3)
print(x)