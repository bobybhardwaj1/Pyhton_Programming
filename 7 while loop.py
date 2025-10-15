# while structure
"""
    while condition:
        code
        code
"""

# example-- print 5 times hello

i=1
while i<=5:
    print("hello")
    i+=1
    
# example-- print n natural number
n=int(input("enter your number"))
i=1
while i<=n:
    print(i)
    i+=1
    
#  sum of n natural number
n=int(input("Enter your number "))
s=0
i=1
while i<=n:
    s=s+i
    i+=1
print("sum of n natural number is ",s)

# prime or not
n=int(input("Enter your number"))
i=0
while i<n:
    if n%i==0:
        print("Not Prime")
        break # break is used to terminate the execution of loop
    i+=1
else:
    print("Prime")
