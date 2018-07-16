################## IMPORTATN : OBJECT ORIENTED PROGRAMMING CONCEPT #######

# imperative programming (using statements, loops, and functions as subroutines),
# functional programming (using pure functions, higher-order functions, and recursion).

# Objects in python are created using classes.
# once class is created like other oops programming this can be used again and again

# classes are created using keyword "class"
# intend to include the functions

class Animal:
    # __init__ similar to constructor in java
    # self -> similar to this in java
    def __init__(self,animaltype,legs):
        #typeofAnimal & leg are attributes of the class.
        self.typeofAnimal=animaltype
        self.leg=legs

cat = Animal("cat",4)
dog = Animal("dog",4)

# What type of object is a method in class - Function

################## NOTES : more about class #############
# __init__ => This method is called when an instance of the class is created
# it also uses class name as function

# in the above example, __init__ takes 2 arguments and assign to the object attribute

# self => All the methods should have the self as first parameter
# although it isn't explicitly passed.
# self is more like a this in java
# python adds the self argument to the list when calling or invoking the function

# Within a method definition, self refers to the instance calling the method.
# instances of a class have attributes, which are data associated with them.

# self.attribute => is used to initialize the inital value of instance's attribute

# Refer the above example of class

# how to print the values of the attributes
print(cat.typeofAnimal)


######################## NOTES : using methods in class ####################
# Methods => Classes can have other methods other than __inti__
# This can be created usign def keyword

class Dog:
    def __init__(self,name,color): # note if the init is misspelled issues TypeError : object takes no parameter
        self.name=name
        self.color=color

    def bark(self):
        print("dog barks")


dog1 = Dog("Coda","brown")
print(dog1.name)
dog1.bark()

########################## NOTES : using class level attributes ###########

class Car:
    tires = 4
    def __init__(self,name,color):
        self.name=name
        self.color=color

toyota=Car("toyota","red")

print(toyota.name) # at instance level
print(toyota.tires) # accessing class level attribute from instance
print(Car.tires) # accessing class level attribute directly using class object

# NOTE: class attribute are shared along all instances of class

class Student:
    def __init__(self, name):
        self.name = name
 
    def sayHi(self):
         print("Hi from "+self.name)
  
s1 = Student("Tom")
s1.sayHi()

# NOTE: AttributeError
# Trying to access an attribute of an instance that isn't defined causes
# an AttributeError. This also applies when you call an undefined method.    

s2=Student("Ram")
# uncomment to test Attriute error
# print(s2.section)
# s2.hello()

################### IMPORTANT : INHERITANCE ##################################
# Inheritance -> a way to share functionlity between classes
# parent and child class

class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=name

class Cat(Animal): # inheritance
    def meow(slef):
        print("cat meowsss")

class Dog(Animal):
    def bark(self):
        print ("dogs barksss")

dog1 = Dog("Cram","black")
print(dog1.color)
dog1.bark()

############### NOTES : about inheritance ################
# subclass => class that is inheriting from another class
# superclass => class that is being inhertied
# methods can be overriden
##########################################################


class Birds:
    def __init__(self, name, color):
        self.name=name
        self.color = color

    def sing(self):
        print("bird sings")

class Parrot(Birds):
    def sing(self):
        print("parrot talked")

# Birds - super class; Parrot - subclass
parrot1 = Parrot("Grad","green")
parrot1.sing()

# another way of invoking 
Birds("CalculatorExample.py","brown").sing()

######################## NOTES : MULTI-LEVEL INHERITANCE ###############
# Inheritance can be indirect. Multiple inheritance.

# class A inherited in class B and class B inhertied in class C

class A:
    def method(self):
        print("A method")

class B(A):
    def bmethod(self):
        print("A supercalss inhertied in B")


class C(B):
    def cmethod(self):
        print("B superclass inhertied in C")

c = C()

c.method()
c.bmethod()
c.cmethod()

###################### NOTES #######################
# CIRCULAR INHERITANCE is not possible in python

### quiz

class A:
    def a(self):
        print(1)

class B(A):
    def a(self):
        print(2)

class C(B):
    def c(self):
        print(3)

c =C()
c.a()

# 2

################# IMPORTANT : SUPER method in inhertiance #############
# super function, used to call the method in the parent class

class SuperClass:
    def method1(self):
        print ("method1")

    def method2(self):
        print("method2")

class SubClass(SuperClass):
    def methodsub1(self):
        print("subclass methodsub1")
        #use super
        super().method1()
        super().method2()

SubClass().methodsub1()

######################### IMPORTANT : Magic methods ###################
# methods that starts and end with __ (double underscore) is special method
# it is used to create a seperate functionality

# it is used on such functionality for creating operator overloading.

# They are also know as DUNDERS.
# one such example is cusom classes that allow operator such as +, *

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)

first = Vector2D(5,7)
second = Vector2D(3,9)

result = first + second
print("{0} {1} ".format(result.x,result.y))

# The __add__ method allows for the definition of a custom behavior
# for the + operator in our class. 
# As you can see, it adds the corresponding attributes
# of the objects and returns a new object, containing the result.
# Once it's defined, we can add two objects of the class together.

class ProductPoints:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self,points):
        return ProductPoints(self.x*points.x,self.y*points.y)

point1 = ProductPoints(4,5)
point2 = ProductPoints(4,5)

res = point1 * point2
print ("{0} , {1}".format(res.x,res.y ))

############## NOTES : other magic methods #################
#__sub__ for -
#__mul__ for *
#__truediv__ for /
#__floordiv__ for //
#__mod__ for %
#__pow__ for **
#__and__ for &
#__xor__ for ^
#__or__ for |

# The x*y is translated to x.__mul__(y)
# NOTE: if x hasn't implemented __add__, x and y are different types
# then y.__radd___(x) is called.
# there are equivalent r method for all magic methods

class Strings:
    def __init__(self,txt):
        self.txt= txt
    def __truediv__(self,other):
        line = "=" * len(other.txt)
        return "\n".join([self.txt,line,other.txt])

spam = Strings("spam")
strs = Strings("Hello Python!")
print (spam/strs)

# Magic method for comparision - Operator overloading
#__lt__ for <
#__le__ for <=
#__eq__ for ==
#__ne__ for !=
#__gt__ for >
#__ge__ for >=

# if __ne__ is not implemented it returns to the opposite
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

#There are several magic methods for making classes act like containers.
#__len__ for len()
#__getitem__ for indexing
#__setitem__ for assigning to indexed values
#__delitem__ for deleting indexed values
#__iter__ for iteration over objects (e.g., in for loops)
#__contains__ for in
#__call__ for calling objects as functions
#__int__ converting object to int (built-in types)
#__str__ converting object to string (built-in types)

# below is an example of how length function and indexing function return random number 
import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
# its more like an interceptor

############################# IMPORTANT L LIFE CYCLE OF OBJECT ###########
# Object life cycle includes creation, manipulation and destruction.

# 1st stage of life cycle is defintion of the class.
# 2nd stage is calling __init__ the instantiation of an instance.
# 3rd stage, memory is allocated to store the instance
# optional stage before 3rd stage __new__ method of the class is called,
# this usally overriden only in special cases
# finally the object is ready for use

# manipulation, happens by interacting with the attributes of the object
# finally the object will be destroyed.

# When an object is destroyed, the memory allocated to it is freed up,
# and can be used for other purposes.

# Destruction of an object occurs when its reference count reaches zero.
# Reference count is the number of variables and other elements that refer to an object.

# If nothing is referring to it (it has a reference count of zero) nothing
# can interact with it, so it can be safely deleted.

# In some situations, two (or more) objects can be referred to by each
# other only, and therefore can be deleted as well. 
# The del statement reduces the reference count of an object by one,
# and this often leads to its deletion.
# The magic method for the del statement is __del__. 
# The process of deleting objects when they are no longer needed
# is called garbage collection.
# In summary, an object's reference count increases when it is assigned
# a new name or placed in a container (list, tuple, or dictionary).
# The object's reference count decreases when it's deleted with del,
# its reference is reassigned, or its reference goes out of scope.
# When an object's reference count reaches zero, Python automatically deletes it.




