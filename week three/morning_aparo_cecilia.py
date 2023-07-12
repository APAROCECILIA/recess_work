'''
ADVANCED TOPICS IN PYTHON;

REGULAR EXPRESSIONS
GENERATORS AND ITERATORS
DECORATORS
CONTEXT MANAGERS
\d 	Returns a match where the string contains digits (numbers from 0-9) 	"\d"
\s	Returns a match where the string contains a white space character
\w 	Returns a match where the string contains any word characters 
(characters from a to Z, digits from 0-9, and the underscore _ character)
.: matches 
* 	Zero or more occurrences 	"he.*o" 
+ 	One or more occurrences 	"he.+o"	
? 	Zero or one occurrences 	"he.?o" 
[] 	A set of characters 	"[a-m]" 
[^ ]:matches any character not within the square brackets
^ :	Starts with 	"^hello"
$ :matches the end of the line

more examples;
\ 	Signals a special sequence (can also be used to escape special characters) 	"\d" 	
. 	Any character (except newline character) 	"he..o" 		
{} 	Exactly the specified number of occurrences 	"he.{2}o" 	
| 	Either or 	"falls|stays" 	
() 	Capture and group'''

# matching and searching
# regex re.match(), re.search(), re.findall()
# example1

import re

text = "my name is  a Cecilia and I am a software engineer"

# match first word
match = re.search(r"\b\w+\b", text)

if match:
    print("Match:", match.group())

# example 2


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


# Example usage
email1 = 'example@example.com'
email2 = 'invalid_email.com'

if validate_email(email1):
    print(f"{email1} is a valid email.")
else:
    print(f"{email1} is an invalid email.")

if validate_email(email2):
    print(f"{email2} is a valid email.")
else:
    print(f"{email2} is an invalid email.")


# generators and iterators
# generators, use the yield keyword instead of return
print("factorial example")


def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


# Example usage
n = 5
factorial_gen = factorial_generator(n)

for factorial in factorial_gen:
    print(factorial)


print("another example on generators")


def my_generator():
    data = [1, 2, 3]
    for item in data:
        yield item


gen = my_generator()
for item in gen:
    print(item)

    gen = (x for x in range(5))
    for item in gen:
        print(item)

'''
ITERATORS
an iterator is an object that contains 
countable number of values and it can be traversed through. Iterable objects include;
lists,tuples, sets, dictionaries, and you can obtain an itertor from them
you can also iterate through the characters of a string because a sting is also an iterator

it contains methods such as  __iter__() and __next__()
an example od a tuple;

'''
# another example;
print("an example on iterators")
weapons = ("rifle", "shortgun", "pistol", "M2_machine_gun", "rifle")
weaponsIter = iter(weapons)

print(next(weaponsIter))
print(next(weaponsIter))
print(next(weaponsIter))
print(next(weaponsIter))
print(next(weaponsIter))


str = "cat"

strIter = iter(str)
print(next(strIter))
print(next(strIter))
print(next(strIter))

# decorators, to allow modify a behaviour of the function
# without directly changing the source code,

print("an example on decorators")


def my_decorator(func):
    def inner():
        print("this is the decorator")
    return inner


def outer_decorator():
    print("this is the outer decorator ")


outer_decorator()
