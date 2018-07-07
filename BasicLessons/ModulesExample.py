# in python modules are piece of code where other developers have developed
# example mathematical operation etc.

# to include a module in our code, use
# import statement.

import random

for i in range (4):
    value = random.randint(0,50)  # randint a function in the random module
    print(value)

###################### IMPORTANT ######################
# another form of import, is to only use sepecif function of the module

# use from ... approach and set that to a varaible, genaral syntax

# from module_name import var

from math import pi
print (pi)

from math import pi,sqrt

# to import all the objects from the module using *

from math import * # not a best practise.

# using alias name or assigning a different variable name - using as

from math import sqrt as squareroot

print(squareroot(9))

# sample

import math as m
print (m.sqrt(25))
# print (math.sqrt(25))  # error occurs in this case

########################## IMPORTANT - TYPES OF MODULES #################
# 1. USER DEVELOPED
# 2. INSTALLED FROM EXTERNAL SOURCE
# 3. PRE-INSTALLED WITH PYTHON
#
#  last #3 is called standard library, example: random, math, os, string, multiprocessing
#  ,sys, subprocess, email, json, doctest, unittest, pdb, argparse and sys
######################################################################


###################### IMPORTANT ################################
# Third-party modules are stored on Python package index (PyPI)
# The best way to install them are using program called pip.
# pip is included in most of the latset python distribution, if not included
# those can be installed easily
# once pip is present, PyPI is easy to install using "pip install library_name"
# command needs to be provided at the command line.
###############################################################






    
