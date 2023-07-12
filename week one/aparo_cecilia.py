# python script example
print('cecilia')

# variables

name = 'APARO CECILIA'
age = 31
my_age = '31'
print(name, age)
print(name + my_age)

'''
PEP8 Script guidelines

1. indention is a must
2. use CASES to declare variables , names 
an functions
camelCase
snake_case
PascalCase

datatypes;
Strings, integers, floats, booleans

sequence types include;
lists use []
tuple use ()
range use loops and iterrations

mapping types
dict enclosed wth{} 
example {
    name: 'aparo'
    age: 31
}
or{ name: 'aparo', age: 31}

Item Dict{guava, cocoa, coconut}

set Types {guava, cocoa, coconut} unordered collection  type, unique 
None Types: None represents absence of a value 
name: none
'''
gender_type = True
print(gender_type)
# END OF MORNING SESSION

# LISTS - stores many items using a single variable
# allows duplicate values or items

names = ['Aparo', 'cecilia', 'heavens', 'Aparo']
my_numbers = [1, 2, 6, 8, 9, 3, 4, 12, 3, 4, 4]
print(names)

# lengh
print(len(my_numbers))

# type
print(type(my_numbers))

# access
print(names[2])
# access heavens
print(names[-2])

# accessing a range
print(names[:3])
print(names[:3])

# add item
names.append("soldier")
print(names)

names.insert(0, "kyle")
print(names)

# remove
names.pop(3)
names.remove("cecilia")

'''TUPLES  
Store many items in one variable
ordered and non_changeable
a data type in python
use parenthesis
allows duplicate values
example'''

weapons = ("rifle", "shortgun", "pistol", "M2_machine_gun", "rifle")
print(weapons)
print(type(weapons))

# length
print(len(weapons))

# different data types
weapon = ("rifle", 23, 2.1, True)
print(weapon)

# access items in tuples
weapons = ("rifle", "shortgun", "pistol", "M2_machine_gun", "rifle")
print(weapons[3])
print(weapons[-1])
print(weapons[:3])

# adding items in tuples; first change to  a list ,add then return to a tuple
weapons = ("rifle", "shortgun", "pistol", "M2_machine_gun", "rifle")

weap = list(weapons)
weap.append("m4_carbine")
weapons = tuple(weap)

print(weapons)
'''
another way to add new item
w = "M240machine_gun"
new_weapons = weapons+ (w)
print (new_weapons)

'''

# add tuples with the same data types
countries = ("Nigeria", "Niger", "Ghana")
countriez = ("Tanzania", "Ethiopia",)

countries += countriez
new_countries = countries + countriez
print(countries)

# for loop - it prints things one at a time and hence the vertical format

my_weapons = ("rifle", "shortgun", "pistol", "M2_machine_gun", "rifle")
for x in my_weapons:
    print(x)

'''
sets
store multiple items in one variable
unchangeable values but can add and remove values from it
'''
nyamaSet = {"beef", "mutton", "pork", "Chevon", "chicken"}
print(nyamaSet)

# length
print(len(nyamaSet))

# type
print(type(nyamaSet))

# accessing element
print(nyamaSet[0])
print(nyamaSet[3])

# remove
nyamaSet.remove("Chevon")
nyamaSet.pop(2)
print(nyamaSet)

# add using insert and append
nyamaSet.insert(1, "molokoni")
nyamaSet.append("duckmeat")
print(nyamaSet)

# add two sets together

nyama = {"beef", "mutton", "pork", "Chevon", "chicken"}
vegs = {"skuma", "nakati", "gobe", "spinach", }

nyama += vegs

newNyama = nyama
print(newNyama)
