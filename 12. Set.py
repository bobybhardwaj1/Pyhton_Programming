# set is a class
# set is mutable
# set is not a sequence
# set is iterable
# indexing is not applicable to set object
# set cannot have duplicate value

#     HOW TO CREATE SET OBJECT
s={1,2,3,4}
s=set("we can put only iterable object here") # this is a empty set

#     ACCESSING SET ELEMENT
s={2,3,4,5}
for i in s:
    print(i)


#    BUILT IN METHODS
# 1. min()
# 2. max()
# 3. len()
# 4. sum()
# 5. sorted()

#   SET OBJECT METHODS
# add() -- add specified element in set
# update() -- add iterable element to the set
# discard() -- remove element from the set if we outside element then it does not give error
# remove() -- remove element
# intersection() -- return the set of comman elements from the sets
# union() --return the union of the sets
# clear() -- return the empty set
# issubset() -- check weather it is a subset or not
# issuperset() -- check weather it is a superset
# pop() -- detlete element in sequence


#     SET COMPREHENSION
# s={expression for i in object}
print({int(a) for a in input().split(",")})
