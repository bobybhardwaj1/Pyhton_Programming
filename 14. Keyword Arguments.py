"""
 Before studying keyword argument lets know default arguments 
 
  DEFAULT ARGUMENTS :-- Default Argumrnts indicate that the function argument will take that value
  if valur argument is passed during the funtion call. 
  The default argument is assigned by using the assignment operator (=).
"""

def f1(a,b):
    print("a=",a,"b=",b)
f1(2,3) # This is positional arguments bacoz according to postion a=2, b=3
f1(b=2,a=3) # this is keyword arguments in this a=3, b=2

# You cannot have positional arguments after keyword rguments

#  Example-- agar teen perameter ho hum do hi value de uss case m kya kre
def add(a,b,c):
    d=a+b+c
    print("sum is",d)
# now we are taking some examples 
add(2,3) 
# ab yaha ye error de dega isko handel krne k liye hum c ko default zero kr dete h
def add(a,b,c=0):
    d=a+b+c
    print("sum is",d)
# now we are taking some examples 
add(2,3) # ab ye error nhi dega
