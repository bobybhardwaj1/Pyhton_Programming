# Typecasting : the process of converting a variable from one data type to another
#    str(), int(), float(), bool()

name = "boby"
age=21
gpa= 7.2
print(type(name))
print(type(age))
print(type(gpa))

gpa=int(gpa)
age= float(age)
age=str(age)
name = bool(name)
age=bin(age) # convert into binary. but it will give answer in str type with prefix 0b
age=oct(age) # convert into octal. but it will give answer in str type with prefix 0o
age=hex(age) # convert into hexa decimal. but it will give answer in str type with prefix 0x



# Input() : A function that prompts the user to enter data
# Returns the entered data as a string

name= input("What is your name: ")
print(f"Hello {name}")

age=int(input("What is your age?: "))
age= age + 1
print(f"your age is {age}")
