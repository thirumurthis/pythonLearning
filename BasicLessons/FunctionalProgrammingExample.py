############# FUNCTIONAL PROGRAMMING ###########
# function as reference

def prodOf2num (x, y):
    return x*y

# function to retur x*y*y value => samplefpfunc (prodof2num, 10,20) outputs 4000
# (10*20)*20
def samplefpfunc (prodfunc,input1,input2):
    return prodfunc(prodfunc(input1,input2),input2)

print (samplefpfunc(prodOf2num, 10,20))

# function to add 5 to parameter

def addFive (x):
    return x+5
# when add_twice (addFive, 10) => output is 10+5+5 = 20
def add_twice( addfunc, a):
    return addfunc(addfunc(a))

print( "result is : {0} ".format(add_twice(addFive,10)))

################### IMPORTANT : PURE FUNCTION #################
# Pure function - are function return value that depends only on THEIR arguments
# Pure function - are function have no side effects
# example is math sin(x) => return the same value for x everytime

def purefunc(x,y):
    temp = x+ 5*y
    return temp/(2*(x+5*y))

print (purefunc(10,20))

#################### IMPORTANT  : NOT PURE FUNCTION ########
# Impure function - function that changes the state of variable outside
# the function block is impure function

evenNum = [1]

def impurefunc():
   # print (evenNum)
    #evenNum.append(4)
    evenNum.insert(2,4)
    return evenNum

print(impurefunc()) # state of the variable outside function is changed in the
# function

######################### NOTES : PURE FUNCTION #############
# easier to test.
#- more efficient. Once the function has been evaluated for an input,
#the result can be stored and referred to the next time the function
#of that input is needed, reducing the number of times the function is called.
#This is called ************memoization**************.
#- easier to run in parallel.
# difficult to make it easier

###################### IMPORTANT : LAMBDA ##################
# this are called ananymous function => lambda derived from claculas
# invented by Alonzo Church.
# generally when you create a variable like int, string some object is created.
# in case of lambda, the object is created on fly.
#
# lambda is declared using lambda keyword
# it can only take simple expression, not much useful as named functions

def sampleLambda(f,arg):
    return f(arg)

print ("2 * 5 * 5 = {0} ".format(sampleLambda(lambda x: 2*x*x, 5)))


#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

######################### NOTE #####################
# lambda functions can be assigned to variable and used like function

squareUsinglambda = lambda y : y*y

print (squareUsinglambda(5))

################ MORE USAGE IS TO USED NAMED FUNCTION ####

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))

############### IMPORTANT : MAP #####################

# Map and filters are built-in function are very useful higher order function
# that operate on lists or similar object called iterable.

# map function takes a function and iterable as argument and retruns a new iterable
# with the function applied to the argument.

def addThree(arg):
    return arg+3

num = [1,2,3,4,5,6,7,8,9,0]
print ("using map function => {0} + 3 = {1} ".format(num,list(map(addThree,num))));
# list is used to convert the value into list

# Same using lambda

oddNum = [1,3,5,7,9,11,13,15]
print("using map lambda => {0} + 3 = {1} ".format( oddNum,list(map(lambda x: x+3,oddNum))))

##################### IMPORTANT : FILTER ####################

# Filter function also takes a function and iterable, but removes the items that
# didn't match a predicate.
# predicate is a function which retruns Boolean

sqnum = [1,4,9,16,25,36,49,64,81]

print("square numbers between 1- 9 that are even {0}".format((list(filter(lambda x: x%2==0, sqnum)))))

################## NOTE ######################
# result can be converted explicitly to list similar to Map.

############################## IMPORTANT GENERATORS ####################

# Generator are type of iteratable, like List or tuple
# Generator don't allow indexing with arbitary indicies like list.
# Generator still can be iterated using for loop

# Generators are created using funtions and *** yield ***** statement.


def count ():
    i =5
    while i >0:
        yield i
        i -=1

for idx in count():
    print(idx)

############ NOTE : Generators breaks memory restriction ########

# Generator yeild one item at a time, they don't have memory restrictions like list

# infinite loop using generators

# uncomment the line to test
#def infiniteLoop ():
#    while True:
#        yield 1

#for val in infiniteLoop():
#    print(val)

# print 1 infinity using generator
# uncomment below for testing
#def countNum ():
#    num=0
#    while True:
#        yield num ** num 
#        num +=1

#for val in countNum():
#    print (val)

########################## IMPORTANT : FINITE Generator #############

# Finite generators can be converted to into a list by passing them as argument
# to the list function

# use of range in the function limits the generators to a finite loop
def num(x):
    for i in range (x):
        if i%2 ==0:
            yield i

print(list(num(20)))

#################### NOTES : Generators #######################
# Using generators results in improved performance, which is the result of
# the lazy (on demand) generation of values, which translates to lower
# memory usage.
# Furthermore, we do not need to wait until all the elements have been
# generated before we start to use them.
###############################################################


######################@ IMPORTANT : DECORATOR #################
# Decorators provide a way to modify functions using other functions. 

# This is ideal when you need to extend the functionality of functions
# that you don't want to modify.

def decorator(funcasarg):  # Decorator function example 
    def wrap():            # nested function to decorate the data
        print("***********")
        funcasarg()        # function call that will be decorated.
        print("-----------")
    return wrap  # don't use () paranthesis, using it leads to error NoneType 

def textfunction():
    print("INPUT")

decorate = decorator(textfunction)
decorate()

textfunction = decorator(textfunction)
textfunction()  # this corresponds to decorated version


################# USING @<decorator_name> ####################

# for @<decorator_funtion_name> in the below example the function is already
# provided above. resuing the same.

# using @ provide the user not to pass the function to decorator

@decorator
def print_text():
    print ("using @decorator")

print_text()    

# To achieve the same behavior as my_func = my_dec(my_func) => @my_dec

# custome example test

## EXAMPLE of extending a simple number function to print square number 
def number(x):
    return x

def decoratorSquare(funcasarg, a):
    def square(a):
        print("before {0} ".format(a))
        res = funcasarg(a*a)
        print ("after {0} ".format(res))
    return square

x = 10;
number = decoratorSquare(number,x) # note in case we need to pass the arguments to a
# functional reference use this way
number(x)

# @decoratorSquare => in this case the @ will not work
def numberfunc(numberfunc,x):
    return x

#n1 =200
#numberfunc(numberfunc,n1)

############################ IMPORTANT : RECURSION #############

# It uses self-reference function calling themselves.
# solves the problem that can break up into easier sub-problems of the same type

def factorial (x):
    if x == 1:
        return 1  # This is called bases case, after which the call exists
    else:
        return x * factorial (x-1)

print ("Factorial of 5 is {0}".format(factorial(5)))

################# NOTE: #######################

# if the base case is not provided in a recursion it leads to infinite loop
# RuntimeError occurs with maximum recursion depth exceeded.

# uncomment to test this
# def factorial (x):
#     return x * factorial (x-1)

# factorial(10)

###################### IMPORTANT:  INDIRECT RECURSION ###########

# one function is being called in another function,
# the first function is again called in invoked (another) function

def is_even(x):
    if x ==0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print("is 17 even? {0} ".format(is_even(17)))
print("is 23 odd? {0}".format(is_odd(23)))
print("is 0 odd ? {0}".format(is_odd(0)))

def fib(x):
    if x==0 or x==1:
        return 1
    else:
        print (x)
        return fib(x-1)+fib(x-2)

print (fib(4))

# fib(3) + fib (2)
# fib (2) + fib(1)/1
#fib(0)/1 + fib(-1)

# fib(2)/ + fib(0)/1
# fib(1)/1 + fib(0)/1

######################### IMPORTANT : SET ###########################

# set are data structure similar to lists or dictionary.
# set are created using curly braces {} / or using set function

# {} => represents empty dictionary*; to create empty set use set().  

# set includes some functionality of list like in to check item present

odd_num = {1,3,5,7,9,11}
random_word =set(["rout","alleviate","confer","permeate","sagacious","aussage"])
# using set function not the square bracket.

print(5 in odd_num)
print( "permeate" not in random_word)  

#################### NOTES: ON SET #######################

# SET is different from list, but shares several operations of list like in, leng
# SET is unordered, they cannot be indexed
# SET cannot contain duplicate element

# SET - faster to check whether the item is part of a set, rather than part of list. - because
# of the way they are stored.

# SET uses add, instead of append
# SET operation remove(index) => removes specific indexed element from the set
# SET operation pop => removes an arbitrary element.

# SET is used for memebership testing and scenarion where duplicate entries to
# be eliminated

# Example

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3) # reporst keyError
print(nums)

number = {1,2,1,4,5,6,9}
print(number)
number.add(-5)
number.remove(2)
print(number)
number.pop()
print(number)

######################### NOTES : SET  Mathematical operation #######################
# Sets can be combined using mathematical operations.
# | = The union operator | combines two sets to form a new one containing items in either. 
# & = The intersection operator & gets items only in both. 
# - = The difference operator - gets items in the first set but not in the second. 
# ^ = The symmetric difference operator ^ gets items in either set, but not both

print ("SET MATHEMITCAL OPERATION")
numberset1 = {1,2,3,4,5,6,7,8}
numberset2 = {6,7,8,9,10,11,12}
print ("numberset1 = {0} && numberset2 = {1} ".format(numberset1,numberset2))
print ("union : {0}".format(numberset1 | numberset2)) # union
print ("intersecton : {0}".format(numberset1 & numberset2)) # intersecton / common
print ("difference  : {0}".format(numberset1 - numberset2)) # diff only in one set /first set
print ("symmetric diff : {0}".format(numberset1 ^ numberset2)) # symmetric differnce

##################### IMPORTANT : USING LIST, SET, DICTIONARY , TUPLE ##########

# python datastructure - supports list, tuples, dictionaries, sets
# USAGE
#When to use a dictionary:
#- When you need a logical association between a *key:value* pair.
#- When you need fast lookup for your data, based on a custom key.
#- When your data is being constantly modified. Remember, dictionaries are mutable.

#When to use the other types:
#   - Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
#  - Use a set if you need uniqueness for the elements. 
#  - Use tuples when your data cannot change.

# A tuple is used in combination with a dictionary,
# for example, a tuple might represent a key, because it's immutable.

######################## IMPORTANT : ITERTOOLS ######################3

# ITERTOOLS is a module, which is a starndard library contaning several functions
# that are useful in functional programming

# One type of function it produces is infinite iterators. 
#    - The function *count* counts from the value to infinite (count(n)). 
#    - The function *cycle* infinitely iterates through an iterable (for instance a list or string). 
#    - The function *repeat* repeats an object, either infinitely or a specific number of times.

# using the whole module
# Recap excercise
#import itertools as iter

print ("ITETTOOLS MODULE ")
# using particular module from itertools
from itertools import count
# from itertools import cycle  # other modules

for i in count(3): #  3- initial counter / index from which look will start
    print(i)
    if i >=11:
        break

# output : 3 4 5 6 7 8 9 10 11

############################### NOTE : ITERTOOLS ADDITION FUNCTION ###########

# takewhile - takes items from an iterable while a predicate function remains true;
# chain - combines several iterables into one long one; 
# accumulate - returns a running total of values in an iterable.

# product & permutations - combinatoric function to perform combination task

from itertools import takewhile,accumulate

nums = list(accumulate(range(10)))
print ("Accumulate function from 0-10: {0}".format(nums))

print("takewhile function : {0} ".format(list(takewhile(lambda x: x<=6, nums))))

# product & permuationa

from itertools import product,permutations

alphabets =('A','B')
print (list (product (alphabets, range(2))))
print (list (permutations(alphabets)))

a={1, 2}
print(len(list(product(range(3), a)))) # note length - not actual product
print(list(product(range(3), a))) # note product

nums = { 1,2,3,4,5,6}
nums = {0,1,2, 3} & nums
print(nums)
nums = filter(lambda x : x>1, nums)
print (len(list(nums)))

def powerfunc(x,y):
    if y==0:
        return 1
    else:
        return x * powerfunc(x,y-1)

print(powerfunc(2,3))
    
a = (lambda x : x * (x+1)) (6)
print(a)





























    
