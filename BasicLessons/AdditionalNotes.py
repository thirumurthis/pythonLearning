# below module prints the zen of python code (python design principles)
import this

# PEF (python enchancement proposals) -
# PEP 8 is style guide on writting readable code

#guidelines in reference to variable names, which are summarized here:
#- modules should have short, all-lowercase names; 
#- class names should be in the CapWords style; 
#- most variables and function names should be lowercase_with_underscores; 
#- constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
#- names that would clash with Python keywords (such as 'class' or 'if') should
# have a trailing underscore.
#- lines shouldn't be longer than 80 characters; 
#- 'from module import *' should be avoided; 
#- there should only be one statement per line.

#NOTE : PASSING n Number of argument in function
# Python allows to have function with varying number of arguments.
# Using *args as a function parameter enables you to pass an
# arbitrary number of arguments to that function.
# The arguments are then accessible as the tuple args
# in the body of the function.
# The parameter *args must come after the named parameters to a function.

def func(named_arg, *multiargs):
   print(named_arg)
   print(multiargs)

func(1, 2, 3, 4, 5)

# NOTE : DEFAULT parameter #####################
# Named parameters to a function can be made optional
# by giving them a default value. 
# These must come after named parameters without a default value.

def myfunc(x, y, defarg="defaultValue"):
   print(defarg)

myfunc(1, 2)
myfunc(3, 4, "checks")

# NOTE : FUNCTIONAL ARGUMENTS #######################
# **kwargs (standing for keyword arguments) allows you to
# handle named arguments that you have not defined in advance.
# The keyword arguments return a dictionary in which the keys
# are the argument names, and the values are the argument values.

def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

# NOTE : Tuple unpacking
# Tuple unpacking allows you to assign each item in an iterable
# (often a tuple) to a variable

numbers = (1,2,3)
a,b,c = numbers
print ("{},{}".format(a,b))
a,b=b,a # swap values since right hand side is a tuple
print ("{},{}".format(a,b))

x,y = [1,2]
x,y=y,x
print(y)

# Assigning left over variable in a list or tuple to one varliabe
# A variable that is prefaced with an asterisk (*) takes all values
# from the iterable that are left over from the other variables.

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)


# IMPORTANT : Terniary operator

# Conditional expressions are also known as applications of the ternary operator.

a = 7
b = 1 if a >= 5 else 42
print(b)

a = -7
b = 1 if a >= 5 else 42
print(b)

# IMPORTANT : else in for and while loop

# The else statement is most commonly used along with the if statement,
# but it can also follow a for or while loop, which gives it a different meaning. 
# With the for or while loop, the code within it is called if the loop finishes
# normally (when a break statement does not cause an exit from the loop).


for i in range(10): # 1 to 10
   if i == 999:
      break
else:
   print("Unbroken 1")

for i in range(10):
   if i == 5:
      break
else: 
   print("Unbroken 2")

# NOTE : else in try/ except

# In this case, the code within it is only executed if no error occurs
# in the try statement

try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)

############### IMPORTANT : __main__ ####################

# Most of the python code is either a module to be imported, or a script that
# does something.

# Sometimes it is useful to make a file that can be both imported as module or
# run as a script.

# To do this, place script code inside if __main__ == "__main__"
# This ensures that this peice of code wont be executed, if the file is imported


#def func():
#    print("This describes a module function")

#if __main__=="__main__":
#    print ("This is a script example")


import mainusage

mainusage.func()

###################### IMPORTANT : THIRD PARTY LIBRARIES ###########
# Django - The most frequently used web framework written in Python, Django
# powers websites that include Instagram and Disqus. It has many useful features,
# and whatever features it lacks are covered by extension packages.

# CherryPy and Flask are also popular web frameworks.
# For Scraping data from website, the library BeautifulSoup is very useful.

# A number of third-party modules are available that make it much easier to carry out scientific and mathematical computing with Python.
# The module matplotlib allows you to create graphs based on data in Python. 
# The module NumPy allows for the use of multidimensional arrays that are much faster than the native Python solution of nested lists. It also contains functions to perform mathematical operations such as matrix transformations on the arrays. 
# The library SciPy contains numerous extensions to the functionality of NumPy.

# Python can also be used for game development. 
# Usually, it is used as a scripting language for games written in other languages, but it can be used to make games by itself. 

# For 3D games, the library Panda3D can be used. For 2D games, you can use pygame











