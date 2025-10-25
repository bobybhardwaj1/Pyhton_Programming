# Lambda is a Keyword
# Lambda expression are strictly  restricted to a single expression
# lambda input : expression

#  ex--
lambda a,b: a+b
# now we can give values of a and b in two ways
k=(lambda a,b: a+b)(3,4)
print(k)

# or

k=(lambda a,b: a+b)
print(k(3,4))

# Recursion using Lambda
# caculate factorial

f= lambda n:  1 if n==0 or n==1 else n*f(n-1)
print(f(5))