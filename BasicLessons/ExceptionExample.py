############# EXCEPTION , ASSERTION #################

# Example of causing an exception
#print(7/0)

################### IMPORTANT - Different EXCEPTION #####
#ImportError: an import fails;
#IndexError: a list is indexed with an out-of-range number;
#NameError: an unknown variable is used;
#SyntaxError: the code can't be parsed properly; 
#TypeError: a function is called on a value of an inappropriate type;
#ValueError: a function is called on a value of the correct type, but with an inappropriate value.
#OSError : caused by os
#########################################################

##################### IMPORTANT - EXCEPTION HANDLING ########
# to handle the exception, we can use try/except statement

try:
    num1 = 7
    num2 =0
    print(num1/num2)
except ZeroDivisionError:
    print ("Cannot divide by Zero - infinite!!")

try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")

########################### NOTE: except: without any exception #########
# if not exception is specified in the except, all exception will be catched.

try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except:
   print("All - error")

import random as m
try:
   variable = m.randint(1,10)
   if variable >5:
       print(variable + "hello")
   else:
       print(variable / 0)
except:
   print("All - error  %d " % variable)

############################ IMPORTANT : finally ##########33
# finally block will be executed no matter in case of exception or otherwise.

try:
   print("TRY EXAMPLE")
   print(1 / 0)
except :
   print("Some Error")
finally:
   print("FINALLY  - This code will run all cases")

########################### IMPORTANT : RAISING EXCEPTIONS ##########
# raise statement can be used to raise exception, example

print (1)
#raise ValueError  # need to specify the type of exception raised.
print (2)

# Exception can be raised with an argument _> arguments details the raised exception

#print (11)
#raise NameError("Invalid name")

########################## NOTE: raise without exception in except: to re-raise ########

try:
   print("TRY EXAMPLE")
   print(1 / 0)
except ZeroDivisionError:
   print("Some Error")
   # raise # uncomment latter for practical example

############################ IMPORTANT : ASSERTION #############
# using assert statement an expression is tested, if a false is evaluated
# exception is raised
# USEFUL TO TEST THE FUNCTION CALL AND RESULT
print ("step1 - true")
assert 5+5==10
print ("step2 - false")
#assert 5+4==10  # throws assertion error # uncomment for testing
print ("end")

############## NOTE : ASSERTION WITH ARGUMENTS #############
# this assertion error can also be caught using try except
# assert exception will terminate the program, if not handled using try except
threshold = 11
# assert ( threshold > 15), "below threshold" # uncomment for testing

try:
    threshold = 11
    assert ( threshold > 15), "below threshold"
except :
    print ("warning of threshold")














   
