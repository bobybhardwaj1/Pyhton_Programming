# dict is class
# dict element are pairs of key value
# dict is mutable
# dict is a not a sequence
# dict is iterable
# indexing is not applicable to dict object
# dict cannot have duplicate keys (not values)

#   HOW TO CREATE DICT OBJECT
d={1:"Rahul", 2:"payal", 3:"arjun",4:"prachi"}
print(d)
d={} # this is an empty dict
d=dict() # empty dict
d1=dict(r="rahul",p="payal")
print(d1)


#   HOW TO ACCSESS ELEMENT IN DICT
# by print
d={1:"Rahul", 2:"payal", 3:"arjun",4:"prachi"}
print(d[1])

#  with for loop
for i in d:
    print(i,d[i])
    
#   EDIT DICT ELEMENT
# there may be two case  " dictobject[key]=D "in this key exist or doesn't exist so:
#  1. if exist:== then it change the value of the key to D.
#  2. if doesn't exist:== then it add new key in the dict with value D

d[1]="Ravi"
print(d)
d[5]="Shayam"
print(d)


#   METHODS
# 1.  items() -- colletion dict elements
print(d.items())

# 2.  values() -- collection of only values of the dict keys
print(d.values())

# 3.  keys() -- collection of only keys of dict
print(d.keys())

#    SAME 5 BUILT IN METHODS THAT WE USE PREVIOUSLY WORKS ON ONLY KEYS.

#   COMAPRISON OPERATOR : ONLY TWO WORK HERE ==(IF BOTH DICT ITEMS ARE EQUAL) OTHERWISE, !=(NOT EQUAL)


#   DICT OBJECT METHODS
# 1.  pop(key)  --it delete the item from the dict and return the value of the key
print(d.pop(5))
print(d)

# 2.  popitem()  -- it delete item randomly and return the whole item in tuple
print(d.popitem())
print(d)

# 3.  clear() -- it return the emptyb dict
print(d.clear())

#   DICT COMPREHENSION
#  d{key expression : data expression for i in seq}
d={a:a**2 for a in range(1,8,1)}
print(d)