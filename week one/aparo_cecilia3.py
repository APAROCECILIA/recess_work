# BOTH MORNING AND EVENING SESSIONS
'''
basic operators & expressions: input and output operators
Arithmetic operators
+addition
- subtraction
/ division
// divide return the quotient without the remainder
*  multiplication
% modulu
** exponential ; this is to raise a number

-comparison operator
== looks like and is equal to
!== or!= not equal to
> greater >= or equals to
< less  <= or equals to

logical operators
logical and 'and'
logical or 'or'
logical not 'not'

assignment operators
 assignment operator: =
 add: +
 add and assign: +=
 subtract and assign: -=
 exponential and assign **=
 multiply and assign *=
 modulu and assign %=
 divide and assign /=

membership operators
in
not in

identity operators
is: checks if they are alike
is not : checks if they are not alike


'''


# examples of arithmetic operators
x = 30 + 20
y = 40 - 60
z = 2*2
c = 4/2
r = 3 % 2
q = 4 ** 4
print(x, y, z, c, r, q)

# comparison operator: greater than
a = 5
b = 1
if a > b:
    print("success")
# greater or equal to
g = 3
h = 3

if g >= h:
    print("equal but not greater")

# less than
f = 0
d = 6

if f < d:
    print("true")

# less than or equal to
w = 7
p = 7
if w >= p:
    print("equal but not less")
# equal to
l = "cecil"
k = "cecil"
if l == k:
    print("true")

# logical operators

a = True
b = False

if (a and b):
    print("they ain't the same")  # true

else:
    print("they are the same")  # false

if (a or b):
    print("it doesnt care")  # true

else:
    print("any could be true or false")

# logical not
print(not a)

# compound assignment operator
v = 5
v += 5
print(v)

g = 6
g -= 4
print(g)

# membership assignment
weapons = ["rifle", "machine_gun", "short_gun"]
if "rifle" in weapons:
    print("true")
    print("short_gun" in weapons)


# bitwise operator: performs operation on individual bits
'''
bitwise AND : &
bitwise OR : |
bitwise XOR : ^
bitwise NOT : ~
bitwise leftshift : <<
bitwise rightshift : >>
example;
'''
liam = 40
hezo = 90

for_and = liam & hezo
for_or = liam | hezo
for_exclusive = liam ^ hezo
for_not = ~liam
for_leftshift = liam << 2
for_rightshift = hezo >> 2

print(for_leftshift)
print("iam done")
print(for_rightshift)


# EXAMPLE: A SIMPLE CALCULATOR
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"


print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    result = add(num1, num2)
    print("Result:", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("Result:", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("Result:", result)
elif choice == '4':
    result = divide(num1, num2)
    print("Result:", result)
else:
    print("Invalid choice")


# END OF MORNING SESSION


# AFTERNOON SESSION EXERCISES
# a list of five and access the second person
# Create a list with 5 items (names of people)
# and write a Python program to output the 2nd item:

people = ["John", "Alice", "Bob", "Emily", "Michael"]
print(people[1])

# Write a Python program to
# change the value of the first item to a new value:

people = ["John", "Alice", "Bob", "Emily", "Michael"]
people[0] = "cecilia"
print(people)

# Write a Python program to add a sixth item to the list:
people = ["John", "Alice", "Bob", "Emily", "Michael"]
people.append("Sarah")
print(people)

# Write a Python program to add "Bathel" as the 3rd item in your list:

people = ["John", "Alice", "Bob", "Emily", "Michael"]
people.insert(2, "Bathel")
print(people)

# Write a Python program to remove the 4th item from the list:

people = ["John", "Alice", "Bob", "Emily", "Michael"]
del people[3]
print(people)

# Use negative indexing to print the last item in your list:

people = ["John", "Alice", "Bob", "Emily", "Michael"]
print(people[-1])

# Create a new list with 7 items and
# use a range of indexes to
# print the 3rd, 4th, and 5th items:

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[2:5])

# Write a list of countries and make a copy of it:

countries = ["USA", "Canada", "UK", "Germany", "France"]
countries_copy = countries.copy()
print(countries_copy)

# Write a Python program to loop through the list of countries:

countries = ["USA", "Canada", "UK", "Germany", "France"]
for country in countries:
    print(country)

# Write a list of animal names and sort them in both descending and ascending order:
animals = ["Elephant", "Tiger", "Lion", "Giraffe", "Monkey"]
ascending_order = sorted(animals)
descending_order = sorted(animals, reverse=True)
print("Ascending order:", ascending_order)
print("Descending order:", descending_order)

# Using the list above,
# write a Python program to output
# only animal names with the letter 'a' in them:

animals = ["Elephant", "Tiger", "Lion", "Giraffe", "Monkey"]
a_animals = [animal for animal in animals if 'a' in animal.lower()]
print(a_animals)

# Write two lists,
# one containing your first names and the other your second names.
# Join the two lists:

first_names = ["John", "Alice", "Bob"]
second_names = ["Doe", "Smith", "Johnson"]
full_names = first_names + second_names
print(full_names)

# TUPLES
#  your favorite phone brand:

x = ("samsung", "iphone", "tecno", "redmi")
favorite = x[2]
print(favorite)

# access 2nd last item in your tuple:

x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]
print(second_last_item)

# update "iphone" to "itel":

x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)
x[1] = "itel"
x = tuple(x)
print(x)

#  add "Huawei" to your tuple:

x = ("samsung", "iphone", "tecno", "redmi")
x = x + ("Huawei",)
print(x)

#  loop through the tuple above:

x = ("samsung", "iphone", "tecno", "redmi")
for phone in x:
    print(phone)

#  remove/delete the first item in your tuple:

x = ("samsung", "iphone", "tecno", "redmi")
x = x[1:]
print(x)

# Using the tuple() constructor,
# create a tuple of the cities in Uganda:
cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu"])
print(cities)

# unpack your tuple:

x = ("samsung", "iphone", "tecno", "redmi")
phone1, phone2, phone3, phone4 = x
print(phone1, phone2, phone3, phone4)

# print the 2nd, 3rd, and 4th cities above:

cities = ("Kampala", "Entebbe", "Jinja", "Gulu")
print(cities[1:4])

# Write two tuples,
# one containing your first names and the other your second names.
# Join the two tuples:

first_names = ("cecilia", "heavens", "felicity")
second_names = ("aparo", "amaro")
full_names = first_names + second_names
print(full_names)

# Create a tuple of colors and multiply it by 3:

colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)

# Return the number of times 8 appears in this tuple:
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5):

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print(count_8)


# SETS
# Use the set() constructor to create a set of 3 of your favorite beverages:

favorite_beverages = set(["kashera", "coffee", "juice"])
print(favorite_beverages)

# Use the correct method to add 2 more items to the beverages set:

favorite_beverages = set(["kashera", "coffee", "juice"])
favorite_beverages.update(["water", "kitiribitta"])
print(favorite_beverages)

# Given the set below; mySet = {"oven", "kettle", "microwave", "refrigerator"},
# check if microwave is present
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

# Write a Python program to remove "kettle" from the set above:
mySet = {"oven", "kettle", "microwave", "refrigerator"}
mySet.remove("kettle")
print(mySet)

# Write a Python program to loop through the set above:
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)

# Write a set of 4 items and a list of two items.
# add elements in the list to elements in the set:

mySet = {"apple", "banana", "orange", "grape"}
myList = ["pineapple", "mango"]
mySet.update(myList)
print(mySet)

# Write two sets, one containing your ages and the other your first names.
# Join the two sets:

ages = {25, 30, 35}
first_names = {"John", "Alice", "Bob"}
combined_set = ages.union(first_names)
print(combined_set)


# STRINGS
# Declare two variables,
# an integer and a string, and use the correct method to
# concatenate the two variables:
number = 42
text = "Hello"
concatenated = str(number) + text
print(concatenated)

# Consider the example below;
# txt = " Hello, Uganda! ".
# Output the string without spaces at the beginning, in the middle, and at the end:

txt = "      Hello,       Uganda!       "
trimmed_txt = txt.strip()
print(trimmed_txt)

# Write a Python program to convert the value of txt to uppercase:

txt = "Hello, Uganda!"
uppercase_txt = txt.upper()
print(uppercase_txt)

# Write a Python program to replace the character 'U' with 'V' in the string above:
txt = "Hello, Uganda!"
modified_txt = txt.replace("U", "V")
print(modified_txt)

# Using the code below,
# return a range of characters in the 2nd, 3rd, and 4th positions:
# y = "I am proudly Ugandan"

y = "I am proudly Ugandan"
character_range = y[1:4]
print(character_range)

# The piece of code below will give an error when output:
# x = "All "Data Scientists" are cool!".
# Write a Python program to correct it:

x = 'All "Data Scientists" are cool!'
print(x)

# DICTIONARIES
#  print the value of the shoe size:
Shoes = {"brand": "Nick",
         "color": "black",
         "size": 40}
shoe_size = Shoes["size"]
print(shoe_size)

#  change the value "Nick" to "Adidas":

Shoes = {"brand": "Nick",
         "color": "black",
         "size": 40}
Shoes["brand"] = "Adidas"
print(Shoes)

# add a key/value pair "type": "sneakers" to the dictionary:
Shoes = {"brand": "Nick",
         "color": "black",
         "size": 40}
Shoes["type"] = "sneakers"
print(Shoes)
