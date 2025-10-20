#  str is class. str is immutable. str is iterable. str is hashable. str is a sequence.
# how to create a str object--
s1="hello"
s2='Hello'
s3="""Hello"""
s4='''Hello'''
s5=str(125)

# INDEXING
S="mysirg"
print(S[0])
print(S[-1])

# Accessing Str elements--
"""
1. s[index]  get the element by index
2. print(s)  return the whole string
3. for i in s:
    print(i)    print all elements one by one

4. important <-- Slicing operator--> 
 architecture>> strobject[beg(inclusive) : end(exclusive) : step]
 ex-- s1= "mysirg"
 print(s1[0:5:1]) out--> 'mysir'
 
 ex-- print(s1[5:1:-1]) out--> 'gris'
 
"""

# BUIILT IN METHODS--
s="mysirg"
print(len(s)) # return the length of string
print(max(s)) # return the biggest element in string
print(min(s)) # return the smallest element in string
print(sorted(s)) # it return the list of sorted element of string

# Concatination and Repetition Operator 
s1="abc"
s2="de"
s=s1+s2
print(s) # out- "abcde"

print(s1*3) # out-- "abcabcabc"


# Comparision Operator
# s1>s2 --> True if s1 comes after after in dictonary order
#  example-- s1="mysirg"  s2="saurabh"  print(s1>s2) -- False 
#  In case of one capital and one small letter small letter is big
#  example s1="mysirg"  s2="Saurabh" print(s1>s2) -- True


# Str Object Methods


s1="mysirg education services"
# 1. index() -- s1.index("i") -- 3
# 2. count() -- s1.count("i") -- 3
# 3. startswith() -- s1.startswith("my") -- True
# 4. endswith() -- s1.endswith("s") -- True
# 5. isdigit() -- s1.isdigit() -- False it checks wheather the string is digit
# 6. islower() -- s1.islower() -- True  it checks weather the string is in lower case or not
# 7. isupper() -- s1.isupper() -- Flase it checks weathere the string is in upper case
# 8. lower() -- s1.lower() -- convert the string into lower letters
# 9. upper() -- s1.upper() -- convert the string into upper case
# 10. replace() -- s1.replace("i"(old value),"I"(new value at the place of old value), s1.count("i")(for all the i))
# 11. format() --

a,b=10,20
s="sum of {} and {} is {}"
print(s.format(a,b,a+b))
# --out sum of 10 and 20 is 30

# if we give index in curly breaces{}

s="sum of {2} and {1} is {0}"
print(s.format(a,b,a+b))
# out-- sum of 30 and 20 is 10

# 12. split() # it gives a list of strings
s1="mysirg education services private limited"
print(s1.split("we have here by which we want to split lets assume space right now"))
# out-- ['mysirg','education','services','private','limited']

#  user input based
l=[int(x) for x in input("enter integers seprated by comma").split(",")] 
print(l)
# lets suppose user gave 44,55,66,77,88,22
# out-- [44,55,66,77,88,22]

# 13. join()--
"hume jisse join krana ho wo yaha de denge".join(s1)
s="mysirg education services"
l=s.split(" ")
print(l)
print("-".join(l))
# out-- ['mysirg', 'education', 'services']
#  mysirg-education-services
