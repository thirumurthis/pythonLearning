# function example

print ("This is a function argument")
#print -> function name
#"this a function argument -> arguments
str(32342)
range(1,20)

#USER defined function sample, uses def keyword

# myFunc - no argument function
# note : and the indentation
# function must be defined before they are called.
# using myFunc() at this line will cause error

# variables inside the function is local to that block
# using them in other part of the code will cause exception
def myFunc():
    print ("hello")
    print ("first function defined")


myFunc()

# Sample function with arguments:

def printThis(word):
    print ("function passed Text: "+word)

printThis("Wow this is cool")

# sample function to multiply by2

def multiplyBy2(inputnumber):
    print(inputnumber *2)

multiplyBy2(109)

def multiply2num (num1,num2):
    print (num1*num2)
    print (num1*num2)

multiply2num(9,9)

#################FUNCTION to return values
# return keyword will return the code flow,
#no line after that wihtin the function will be executed

def sum2num(num1, num2):
    return num1+num2

print (sum2num(10,15))

############ DOCSTRING ################
# created using """ & """ = this is retainded in the runtime
# and used if the user wanted to debug/inspect at runtime.
def sqrofnum (num1):
    """
    This function will be used to find the square of a number
    """
    return num1**2

print (sqrofnum(8))

### FUNCTIONS AS A VARIABLE #######
# FUNCTIONS can be a object itself#####
print ("################# EXPLORE FUNCTION ASSIGNED TO VARIABLE as OBJECT ####")
summing = sum2num
print(summing(89,11))

#### FUNCTIONS AS ARGUMENT TO ANOTHER FUNCTION ##############
# example below pass the function as argument

def printSumRes (func, num1, num2):
    return func(func(num1,num2),func(num1,num2))

def printSumof3num (funcasargument, num1, num2, num3):
    return funcasargument(funcasargument(num1,num2),num3)

print("Sum of two # twice 10, 20 : %d " %printSumRes(sum2num,10,20))
print("Sum of three # 10,20, 70 using func flow as arg : ")
print(printSumof3num(sum2num,10,20,70))












    
