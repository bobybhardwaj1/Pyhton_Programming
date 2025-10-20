# tuple is a class
# tuple is iterable
#  tuple is immutable
# tuple element are indexed
#  tuple is a sequence
# tuple can store hetrogeneoous element

# creating tuple object
t=(1,2,3,4,5)
print(type(t))
t=()# empty tuple

t=(10) 
# this is not type 'tuple'. this is 'int' type.
print(type(t))

#  if we want to create tuple with singfle element then we use comma after the value.
t=(10,)
print(type(t))

#  if we put values without "()" then it is also considered as tuple
t=1,2,3,4,5
print(type(t))

# Accesing tuple element by 3 ways
# !st method : By indexing
t=(1,2,5,7)
print(t[0],t[1])

# With For loop
for i in t:
    print(t)
    
# with while loop
i=0
while i<len(t):
    print(t[i])
    i+=1
    


#      BUILT IN METHODS
     
# 1. min() --return the minimum element in tuple
print(min(t)) 
# 2. max() --return the maximum element in tuple
print(max(t))
# 3. len() --return the length of tuple
print(len(t))
# 4. sum() --return the sum of the element of the tuple
print(sum(t))
# 5. sorted() -- return the lsit of sorted tuple 
print(sorted(t))
# if we want reverse order list then pass the perametre reverse= True inside sorted
print(sorted(t, reverse=True))

#    CONCATINATION AND REPETITION OPERATOR
t1=10,20
t2=30,40,50
print(t1+t2) # concatenate two tuple
print(t1*3) # repeate the tuple 3 times


#     COMPARISON OPERATOR
#  For comapring check the first element of the tuples if they are same then second and so on.
t1=10,20
t2=30,40
print(t1<t2)

#     TUPLE OBJECT METHODS

t=(1,2,3,4,5)
# 1. index(element) --return the index of the element of the tuple
print(t.index(2))

# 2. count(element) -- return the count of element in tuple
print(t.count(3))

#     SLICING OPERATOR
t=(10,20,40,60,70,90)
#  t[beg(inclusive): end(exclusive): step]
print(t[0:4:1])


#      USER INPUT
#  t= tuple([int(e) for e in input.split(",")])