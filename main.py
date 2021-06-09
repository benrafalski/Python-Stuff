import math
import random
import os
import shutil
from abc import *
def howItPrint():
    print("hello world") # how to print

#-----variables-----
def variables():
    name = "Ben Rafalski" # can use single or double quotes for a string in python
    age = 20
    height = 250.5
    alive = True # booleans start with a capital letter
    print("hello " + name + " who is: " + str(age) + " years old and " + str(250.5) + "cm tall, is ben alive? " + str(alive))

#-----multiple assignment, assign multiple variables in one line-----
#name, age, alive = "ben", 20, True
#print("name: " + name + ", age: " + str(age) + ", isAlive?: " + str(alive))

#-----string methods-----
#name = "ben"
#print(len(name)) # string length
#print(name.find("b")) # returns the index of the character selected
#print(name.capitalize()) # capitalizes the first letter
#print(name.upper()) #turns string all uppercase
#print(name.lower()) # turns string all lowercase
#print(name.isdigit()) # returns true if it is a number
#print(name.isalpha()) # returns true if the letters in the string are alphabetical
#print(name.count("e")) # returns the count of selected characters
#print(name.replace("e", "a")) # replaces first argument with the second one
#print(name*3) # prints a string multiple times

#-----Type Casting-----
#x, y, z = 1, 2.2, "3" # int, float, string
#print(int(y)) # drops the decimal
#print(float(z)) # adds a .0 to the end
#print(str(x)*3)

#-----user input-----
#name = input("what is your name?: ") # always returns a string, must cast if you need to do math operations
#age = float(input("what is your age?: "))
#age += 1
#print("your name is: " + name + ", next year you will be: " + str(age))

#-----math functions, must use "import math" to start-----
#pi = 3.14
#x, y, z = 1, 2, 3
#print(round(pi)) # rounds the number
#print(math.ceil(pi)) # rounds the number up
#print(math.floor(pi)) # rounds the number down
#print(abs(-pi)) # returns the absolute value of the number
#print(pow(pi, 2)) # takes the first argument to the power of the second argument
#print(math.sqrt(pi)) # returns the square root of the number
#print(max(x,y,z)) # returns the max number from a set of numbers
#print(min(x,y,z)) # returns the min number from a set of numbers

#-----string slicing, creating a substring from a string-----
#name = "Ben Rafalski"
#first_name = name[0:3:1] # indexing[start(inclusive):stop(exclusive):step]
#last_name = name[4:12:1]
#reverse_name = name[::-1] # returns the string in reverse, index [0:end:-1]
#print(first_name + last_name)

#-----If statements-----
#age = int(input("how old are you?: "))
#if age >= 65:
#    print("you are a senior")
#elif age >= 18:
#    print("you are an adult")
#else:
#    print("you are a child")

#-----logical operators (and, or, not)-----
#temp = float(input("what is the tempurature outside?: "))
#if not(temp <= 0 and temp >= 30):
#    print("the tempuratue is good today")
#elif temp < 0 or temp > 30:
#    print("the tempurature is bad today")

#-----while loops-----
#name = ""
#while len(name) == 0:
#    name = input("enter your name: ")
#print("hello " + name)

#-----for loops-----
#for i in range(1,11,1): #executed 10 times 'range(inclusive, exclusive, step)'
#    print(i)

#-----nested loops-----
#rows = int(input("how many rows?: "))
#columns = int(input("how many columns?: "))
#symbol = input("enter a symbol to use: ")
#for i in range(rows):
#    for j in range(columns):
#        print(symbol, end = "") # prevents a newline
#    print() # newline

#-----loop control statements, break (terminate loop), continue (skip to next iteration), pass (does nothing)-----
#while True:
#    name = input("enter your name: ")
#    if name != "":
#        break
#phone_number = "123-456-7890"
#for i in phone_number:
#    if i == "-":
#        continue
#    print(i, end = "")
#for i in range(1,21):
#    if i == 13:
#        pass # does nothing, place holder for the word 'nothing'
#    else:
#        print(i)

#-----lists, like arrays-----
#food = ["pizza", "cookies", "hamburger", "hot dog"]
#food.append("ice cream") # adds the element to the end of the list
#food.remove("hot dog") # removes the selected element from the list
#food.pop() # removes the last element from the list
#food.insert(0,"cake") # inserts the second argument as an element into the index of the first argument in the list
#food.sort() # sorts the list alphabetically
#food.clear() # clears all items from the list

#-----2D lists, list of lists-----
#drinks = ["coffee", "soda", "tea"]
#dinner = ["pizza", "hamburger", "hotdog"]
#dessert = ["pie", "ice cream", "cake"]
#food = [drinks, dinner, dessert]
#for i in range(3):
#    for j in range(3):
#        print(food[i][j], end="")
#        if(j != 3):
#            print(", ", end="")
#    print()

#-----tuples, collections which are ordered and unchangeable, useful for related data-----
#student = ("ben", 21, "male")
#student.count("ben") # returns how many times a value appears in a tuple
#student.index("male") # returns the index of the selected element in the tuple

#-----sets, collection that is unordered and unindexed, has no dublicates-----
#utensils = {"fork", "spoon", "knife"}
#dishes = {"bowl", "plate", "cup", "knife"}
#utensils.add("napkin") # adds a specified element to the set
#utensils.remove("fork") # removes a specified element from the set
#utensils.clear() # clears all elements from a set
#utensils.update(dishes) # adds the elements of one set to another
#dinner_table = utensils.union(dishes) # takes the union of 2 sets
#for x in dinner_table:
#    print(x)
#utensils.difference(dishes) # what does utensils have that dishes does not?

#-----dictionaries = changeable, unordered collection of key:value pairs-----
#capitols = {'USA':'Washington DC', 'India':'New Dehli', 'China':'Beijing', 'Russia':'Moscow'}
#print(capitols['Russia']) # use the key instead of the index of the element
#print(capitols.get('Germany')) # safer way of accessing the elements
#print(capitols.keys()) # prints all the keys
#print(capitols.values()) # prints only the values
#print(capitols.items()) # prints the keys and the values together
#capitols.update({'Germany':'Berlin'}) # adds/changes an element in the dictionary
#capitols.pop('USA') # removes the key value pair from the dictionary
#capitols.clear() # clears the dictionary

#-----index operator [], used in strings, lists, and tuples-----
#name = "ben rafalski"
#first_name = name[:3].upper() # [start:end]
#last_name = name[4:].upper() # [start:end]
#last_character = name[-1] # access element in reverse
#print(first_name+last_name)

#-----functions-----
#def func(name): #use the def keyword
#    print("this is " + name + "'s first function")
#input = input("what is your name?: ")
#func(input)
#-----function that returns something-----
#def multiply(factor, multiplier):
#    multiplicand = factor * multiplier
#    return multiplicand
#number_1 = int(input("enter a number: "))
#number_2 = int(input("enter another number: "))
#multiplying = multiply(number_1, number_2)
#print(multiplying)

#-----keyword arguments, preceded by an identifier when passing into a func-----
#def hello(first, middle, last):
#    print("hello "+first+" "+middle+" "+last)
#hello(last = "rafalski", first = "benjamin", middle = "charles")

#-----*args paramenter, packs all arguments into a tuple-----
def argsAndKwargsParameters():
    def add(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
    print(add(5,5,5,5,5,5,5))
    #-----**kwargs, packs all arguments into a dictionary-----
    def hello(**kwargs):
        print("hello", end = " ")
        for key,value in kwargs.items():
            print(value, end=" ")
    hello(first="ben", middle = "charles", last = "rafalski")

#-----format method, helps display output-----
def formatMethod():
    animal = "cow"
    item = "moon"
    pi = 3.1415
    print("the {0:^10} jumped over the {1:^10}".format(animal, item)) # uses placeholders {}
    print("the number pi is {:.2f}".format(pi))

#-----random module, use 'import random'-----
def randomModule():
    x = random.randint(1,6)
    y = random.random()
    myList = ["rock", "paper", "scissors"]
    z = random.choice(myList)
    print(x, y, z)
    cards = [1,2,3,4,5,6,7,8,9,"J", "Q", "K", "A"]
    random.shuffle(cards)
    print(cards)

#-----exception handling-----
def exceptionHandling():
    try:
        numerator = int(input("enter a number to divide: "))
        denominator = int(input("enter a number to divide by: "))
        result = numerator / denominator
    except ZeroDivisionError:
        print("you cannot divide by zero")
    except ValueError:
        print("enter only numbers please")
    except Exception: # catches all exceptions
        print("something went wrong")
    else:
        print(result)
    finally: # executes everytime the try/except statement is executed
        print("this will always execute")

#-----file detection, use 'import os'-----
def detectFile():
    path = "C:\\Users\\benrafalski\\Documents\\CSE365\\Assignment3\\README.txt"
    if os.path.exists(path):
        print("that location exists")
        if os.path.isfile(path):
            print("that is a file")
        elif os.path.isdir(path):
            print("that is a folder")
    else:
        print("that location does not exist")

#-----reading a file-----
def readFile():
    try:
        with open('test.txt') as file:
            print(file.read()) # closes file automatically after opening
    except FileNotFoundError:
        print("that file was not found")

#-----writing a file-----
def writeFile():
    text = "this is my written text\nThis is a newline"
    with open('test.txt', 'w') as file: # open in write mode
        file.write(text) # ovewrites previous file, use 'a' instead of 'w' for appending instead

#-----copying a file, use 'import shutil'-----
def copyFile():
    shutil.copyfile('test.txt', 'copy.txt') # src,dest

#-----moving a file, use 'import os'
def moveFile():
    source = "test.txt"
    destination = "C:\\Users\\benrafalski\\Downloads\\test.txt"
    try:
        if os.path.exists(destination):
            print("this file is already there")
        else:
            os.replace(source, destination)
            print(source+ " was moved")
    except FileNotFoundError:
        print(source + " was not found")

#-----deleting a file, use 'import os'-----
def deleteFile():
    try:
        os.remove("copy.txt")
    except FileNotFoundError:
        print("that file was not found")

#-----classes-----
def createClass():
    class Car:
        # class variable
        wheels = 4
        # self is the same as 'this' keyword, __init__ is the constructor
        def __init__(self, make, model, year, color):
            # instance variables
            self.make = make
            self.model = model
            self.year = year
            self.color = color
        def drive(self):
            print("this car is driving")
        def stop(self):
            print("this car is stopped")

    new_car = Car("toyota", "tacoma", 2002, "silver")
    print(new_car.make, new_car.model, new_car.year, new_car.color, new_car.wheels)
    new_car.drive()
    new_car.stop()

#-----Inheritance-----
def inheritance():
    # parent class
    class Organism:
        alive = True
    # child class of organism
    class Animal(Organism):
        def eat(self):
            print("this animal is eating")
        def sleep(self):
            print("this animal is sleeping")
    # child classes of animal
    class Rabbit(Animal):
        def hop(self):
            print("this rabbit is hopping")
    class Fish(Animal):
        def swim(self):
            print("this fish is swimming")
    class Hawk(Animal):
        def fly(self):
            print("this hawk is flying")

    rabbit, fish, hawk = Rabbit(), Fish(), Hawk()
    print(rabbit.alive, fish.alive, hawk.alive)
    fish.eat()
    hawk.sleep()
    rabbit.hop()
    fish.swim()
    hawk.fly()

#-----multiple inheritance-----
def multipleInheritance():
    class Prey:
        def flee(self):
            print("this animal is fleeing")
    class Predator:
        def hunt(self):
            print("this animal is hunting")
    class Rabbit(Prey):
        pass
    class Hawk(Predator):
        pass
    class Fish(Prey, Predator):
        pass
    rabbit, hawk, fish = Rabbit(), Hawk(), Fish()
    rabbit.flee()
    hawk.hunt()
    fish.flee()
    fish.hunt()

#-----method chaining-----
def methodChaining():
    class Car:
        def turn_on(self):
            print("you start the engine")
            return self # must have return self on the methods you would like to chain together
        def drive(self):
            print("you drive the car")
            return self
        def brake(self):
            print("you step on the brakes")
            return self
        def turn_off(self):
            print("you turn off the engine")
            return self
    car = Car()
    car.turn_on().drive()

#-----super function-----
def superFunction():
    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width
    class Square(Rectangle):
        def __init__(self, length, width):
            super().__init__(length,width)
    class Cube(Rectangle):
        def __init__(self, length, width, height):
            super().__init__(length,width)
            self.heigth = height

#-----abstract classes, uses 'from abc import *'-----
def abstractClasses():
    class Vehicle:
        # this is the abstract method, making this an abstract class
        # this abstarct method must be overridden
        @abstractmethod
        def go(self):
            pass
    class Car(Vehicle):
        def go(self):
            print("you drive the car")
    class Motorcycle(Vehicle):
        def go(self):
            print("you ride the motorcycle")

