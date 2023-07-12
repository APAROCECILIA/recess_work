'''dictionary; these allow to store data values in key value pairs
thbey dont allow duplicates
they are ordered and changeable
in the order;
key: value
'''
carsDict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1966,
    "year": 2000  # this overwrites the above key "year"
}
print(carsDict)
# using a key name to access a value

print(carsDict["brand"])
print(type(carsDict))
print(len(carsDict))

# the dict()constructor through the dict() method
mydict = dict(
    name=" Soldier",
    age=50,
    country="Nigeria"
)
print(mydict)
print(type(mydict["name"]))

# EXERCISE
# a programme to check for mental health
# of the student

myDict = {
    "happy": "great to hear that!",
    "confused": "please setle down and write down what is confusing",
    "tired": "take a nap",
    "restless": "go to the gym"
}

emotion = input("what are your feelings now?: ")

if emotion in myDict:
    value = myDict[emotion]
    print(value)
else:
    print("sorry, I could not interprete your emotion.")


# if's ,for and while loop
a = 1
b = 2
if a < b:
    print(" something")

fruits = ["mangoes", "apples"]
for f in fruits:
    print(f)

# exercise(the use of control statements)
number = int(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")


# break and continue statements
i = 2
while i < 4:
    print(i)
    i += 1
    break
    print(" I am done with while loop")

for alpha in range(1, 5):
    if alpha == 4:
        break  # halt at 4
    print(alpha)

print(" I halted at 4")

# continue
for celia in range(0, 4):
    if alpha == 3:
        continue  # skip 3
    print(celia)
    break
    print("I have continued")  # this is to help track my code

# exception handling
try:
    myNumbers = [1, 2, 3, 4]
    print(myNumbers[5])
except:
    print("not in range")
finally:
    print("try another index")


# END OF MORNING SESSION
 # DICTINARIES
 # example
student = {
    "name": "cecilia",
    "age": 40,
    "program": "BSSE",
    "gpa": 3.8
}
# Accessing dictionary values
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Program:", student["program"])
print("Student GPA:", student["gpa"])

# Modifying dictionary values
student["gpa"] = 3.9
print("Updated GPA:", student["gpa"])

# Adding a new key-value pair
student["year"] = "YR3"
print("Student Year:", student["year"])

# EXERCISE
# Get all values in the dictionary
values_list = list(student.values())
print("values in the dictionary are:", values_list)

# Check if a key exists
if "age" in student:
    print("The 'age' key exists in the dictionary.")

if "year" in student:
    print("The 'year' key exists in the dictionary.")
else:
    print("The 'year' key does not exist in the dictionary.")

# Update items using the update() method
student.update({"program": "BCSC", "gpa": 4.0})
print(student)

# Removing a key-value pair
del student["program"]
print("Updated Dictionary:", student)


# Loop through the dictionary
for key, value in student.items():
    print(key, ":", value)


# DATA TYPES
a = 2  # int
b = 4.555  # float
c = 6j  # complex

# type conversion (EXERCISE)
# int to float
x = float(a)
print(type(x))

# float to complex
z = complex(b)
print(type(z))

# complex to float
# r = float(c)   it gives an error


# STRINGS
# declare a string
name = "aparo"
print(name)

# single line string
x = "me"

'''exercise
use the len() method for length
use a for loop
an example in slicing in strings
'''
print(len(x))

for y in x:
    print(y)

# Slicing example in strings

text = "Hello, World!"

# Slicing a string
slice1 = text[0:5]  # Slice from index 0 to 4 (exclusive)
slice2 = text[7:]   # Slice from index 7 to the end
slice3 = text[:5]   # Slice from the beginning to index 4 (exclusive)
slice4 = text[::2]  # Slice with a step size of 2

# Print the slices
print("Slice 1:", slice1)
print("Slice 2:", slice2)
print("Slice 3:", slice3)
print("Slice 4:", slice4)

# multiline strings
quote = '''i am going to church
this Sunday'''

# as arrays
Lname = "cecilia"
for x in Lname:
    print(x)

# exercise
# how to modify a string
a = "afternoon"
# print(a.upper())
# print(a.lower())

# remove whitespace
b = "after noon"
print(b.strip())

# string concatenation
fruit1 = "apple"
fruit2 = "mango"
print(fruit1 + fruit2)

# formating strings
name = "John"
age = 25
profession = "Engineer"

# Using positional arguments
message = "My name is {}. I'm {} years old and I work as an {}.".format(
    name, age, profession)
print(message)

# Using indexed arguments
message = "My name is {0}. I'm {1} years old and I work as an {2}.".format(
    name, age, profession)
print(message)

# Using named arguments
message = "My name is {name}. I'm {age} years old and I work as an {profession}.".format(
    name=name, age=age, profession=profession)
print(message)

# Using f-strings (Python 3.6+)
message = f"My name is {name}. I'm {age} years old and I work as an {profession}."
print(message)


# booleans evaluate to true or false
# use conditions to show boolean values
e = 40

if (e < 30):
    print("false")
else:
    print("true")
