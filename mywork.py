
# inheritance
class house:
    def __init__(self, type, location, price):
        self.type = type
        self.location = location
        self.price = price

    def property(self):
        print("the property is at: " + self.location)
        
class land(house):  # has same properties and methods of the above
    pass


c1 = land("mailo", "gulu", "USD2000")
print(c1.type)
print(c1.price)
print(c1.location)

print(c1.property())

'''ARRAY it is like a list[]
methods like; append()
clear()copy()returns a copy of the list
count()insert()pop()remove()
reverse()sort()
'''
cars = ["ford", "volvo", "BMW"]
print(len(cars))

'''
USER INPUT
python 3.6 uses input() method
python 3.6 uses raw_input() method

this example takes in username
'''
username = input("Enter username: ")
print("username is: " + username)

