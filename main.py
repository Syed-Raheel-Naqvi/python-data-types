# String
name = "Raheel"
print(f"My name is {name} and i am a developer") # f-string
print(type(name))

# Multi-line string, use triple quotes to write multi-line string
paragraph = """My name is Raheel, 
I am a Developer,
currently learning Python"""
print(paragraph)


# Integer
a = 30  # Integer is a whole number, it can be positive or negative
b = 15
print(a + b) # Addition
print(a * b) # Multiplication
print(a / b) # Division
print(a - b) # Subtraction
print(a % b) # Modulus
print(type(a)) #type() function is used to get the data type of the variable

# Float
c = 10.5   # Float is a number with decimal point, it can be positive or negative
d = 15.5
print(c + d)

# Boolean
is_hungry = True # Boolean is a data type that can only have two values, True or False
not_hungry = False

if(is_hungry):
    print("Let's order the pizza")
else:
    print("Let's go to sleep")


# List
shopping_items : list[str] = ["Cake", "Eggs", "Juice", "Chips", "Bread", "Oil"]

print(type(shopping_items))
print(shopping_items)
print(len(shopping_items))  # "len" length means total items in list
print(shopping_items[0:4])  # Slice the list
shopping_items.append("Butter")  # Adding the item in list
shopping_items.remove("Bread")   # Remove item from the list
shopping_items.pop(0)  # Remove item from the list
shopping_items.insert(3,"Cherry")  # Insert item in list
print(shopping_items)


# Tuple
tup = (2,7,4,8,3,9,3)  # Tuple is immutable collection of values, never change the values once assigned.

print(type(tup)) 
print(len(tup)) # Length of the tuple
print(tup[2]) 
print(tup[1:4]) # Slice the tuple
print(tup.index(4)) # Index of the element
print(tup.count(3)) # Count the element


# Dictionary
info = {     # Dictionary is a collection of key value pairs,it is mutable.
    "key" : "value",
    "name" : "Raheel",
    "learning" : "Python",
    "is_adult" : True,
    "marks" : 75.2   
}

print(type(info))
print(info["name"])
print(info["marks"]) 
print(info.get("learning"))
info["name"] = "Syed Raheel" # Update the value
info["is_student"] = True    # Add new key value pair
print(info) 
print(info.keys()) # Get all the keys


# Set 
collection = {1,2,4,2,2,4,9,3,5,1,6,7}  # Set unordered collection of unique values

print(collection) # ignore the duplicate values, only unique values will be printed.
print(len(collection)) # Length ignore the duplicate values. 


# Frozen set 
frozen = frozenset([1,2,3,4,5,6,7,8,9])  # Frozen set is immutable set
print(frozen)


# Functions
def greet(name): # Function is a block of code which only runs when it is called
    print(f"Hello {name}") 

greet("Raheel")


# None
a = None
print(type(a)) # NoneType means no value is assigned to the variable.


# Comparison Operators
age = int(input("What is your age? "))
                         # Comparison operators are used to compare two values  
if (age < 18) :          # if else statement
  print("You are a minor")
elif (age == 18) :
  print("You are young person")
elif (age >= 80) :
  print("You are an old person")
else:
  print("You are an adult")

