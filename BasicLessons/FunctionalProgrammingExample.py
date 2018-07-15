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

























    
