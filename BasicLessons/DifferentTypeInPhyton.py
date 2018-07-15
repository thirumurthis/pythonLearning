################ IMPORTANT: None #############
# None object is used to represent the absence of value. (simillar to null in java)
# values like 0,[], "", False -for Boolean variable

None
print(None)
print(None==None)

##### NOTE: None is returned by any function, that doesn't have explicit return

def funct():
    print ("call passed in function")

var = funct();
print (var) # prints None

############## IMPORTANT : Dictionaries ###########
# Dictionaries are datastructure used to map arbitary keys to values.
# Dictionaries can be indexed in same way as lists, using square brackets containing keys
# Each element in dictionaries is displayed in key:value pairs like map in java
ages = { "Tom": 19, "Kim" :20, "Rock" : 23}
print (ages["Tom"])

# keyError - Occurs when trying to index an key that is not present, example
# uncommet for testing
#print (ages["Bob"]) # keyError: 'Bob'

dictionary = {} # empty dictionary declaration
color = { "red" : [255,0,0], "blue":[0,255,0]};
print(color["red"]) 

###### NOTE: only immutable objects can be used as keys in dictionary #######
# uncomment for testing
#dict_incorrect = {[3,2,1]:"three two one"} # incorrect TypeError unhasable key

#################### Dictionary function ####################
# like list dictionary keys can be assigned with a value

squares = {1:1,2:4,3:"error",4:16}
squares[8]=64
squares[9]=81
squares[3]=9
squares[0]=0
print(squares)

################### NOTE : in and not in ##############33
# to determine key is present in the dictionary use in or not in

dictionary1 ={ 1:"one",2:"two"}
print(1 in dictionary1) # True


################ NOTE: get method ####################
# get takes the key and returns either None by default.
# we can provide specific message to

print(dictionary1.get(1)) # prints one
print(dictionary1.get(3)) # None
print(dictionary1.get(4),"Not in the dictionary") # Prints None Not in the dictionary


#################### IMPORTANT : Tuples #####################
# Tuples are similar to list, only difference is Tuples are IMMUTABLE.
# values cannot be changed.
# declared usign () - parantesis rather than []

test1=("one","two","three")

#access using index like list
print(test1[0]) # one

# tuple can be nested like list and dictionarly
test2=("one", ("1-two","1-three"))
print(test2[1])

# Tuple can be created without parantesis ()
test3 = "four","five","six"
print(test3[2]) # six

test4=() # empty tuple

####################### IMPORTANT : LIST Slice #############
# An advanced way of retrieving data from list.
# list slicing involves index of the list seperated by colon (1:5)
# returns a new list with the values between the indeices of the old list

evenNum=[2,4,6,8,10,12,14,16]  # => index : 0,1,*2[6]*,3,4,5,6,7,8
print(evenNum[2:6]) # [6,8,10,12] => old index: 2~6; etc.

###################### NOTES ########################
# Like range, slicing also includes the very first index specifed
# The end of the list will be indecies -1 specifed in the :

###################### NOTES ########################
# Other representation
# if list[:4] - slice from the first index to 4th
# if list[4:] - slice from the 4th index to the end

squareNum =[0,1,4,9,16,25,36,49,64,81,100]
print(squareNum[:5])
print(squareNum[5:])

##################### NOTES #########################
# TUPLES can be also SLICED

evenNumwithZero=[0,2,4,6,8,10,12,14,16,18,20]
print("different approach for slicing ")
print(evenNumwithZero[::3]) # prints all element with index incremented by 3 # 0,6,12,18
print(evenNumwithZero[2:10:3]) # will include elements starting from the 2nd index
# upto 8 with the step 3
print(evenNumwithZero[2:8:2]) # middle integer represents max slicing number,
#return list will be assmuing index less than it. value at 8th index will not be
# considered output is [4,8,12]
print (evenNumwithZero[1::4]) # prints till the end. [2,10,18]

##################### NOTES #######################
# Negative numbers
# p
print(squareNum[1:-1]) # prints the element till the last index -1
# output [1,4,9,16,25,36,49,64,81]
print(squareNum[1:-3]) # prints the element tille the last index -3
# output [1,4,9,16,25,36,49]

# list [::-1] = is used to print the list in reverse order.
print (squareNum[::-1]) # idiomatic way to reverse a list. since it prints from the last

print(squareNum[7:5:-1])

######################### IMPORTANT - LIST COMPREHENSION ########
# create a new list based on some rule.

square = [i**2 for i in range (12) ]
print(square)

# USING IF in the comprehension

evenSquare = [i**2 for i in range (10) if i%2 ==0 ]
print (evenSquare)

############################# NOTES #######################
# Geneartion of large numbers using comprehension leads to MemoryError
# uncomment to test 
#even = [2*i for i in range(10**100)]

# This issue is solved by Generators

###########################################################
######################### STRING FORMATTING ###############
# to combine a string with non-string we used to convert non-string to string
# uncomment to test it
#print ("t"+1) # TypeError

#String formatting provides a powerful way to embed non-string within string.
# this is performed using format method in the string, with number of arguments

squarenumber = [4,9,25]
sqrmsg = "square of 2,3,5 are {0},{1},{2}".format(squarenumber[0],squarenumber[1],squarenumber[2])
print (sqrmsg)
# each values int string are replaced with the value determined using {}

print("{0}{1}{0}".format("Zero","One")) #ZeroOneZero

##################### NOTES #########################
# String formatting with Named arguments

msg =" equation of square {x}^2 + {y}^2 =1*C ".format(x=2,y=4)
print (msg)

##################### NOTES - STRING MANIPULATION #########################
# function like => join, replace, startswith, endswith, lower ,upper

str1 =" funny "
str2 =" joined "
print(str1.join(str2)) # str2 each word will be joined with funny
print(",".join(["hello","hello","help"]))

print (" Help me".replace("me","yourself"))

print ("converted to upper".upper())
print ("This to check starts with ".startswith("This"))

#################### NOTES - NUMBERIC FUNCTIONS ######################
# function like => min, max, abs, sum
print (min([10,22,-1]))
print (abs (-9)) # not an array 
print (sum([10,11]))

#################### NOTES - LIST FUNCTION ALL & ANY ##################
# conditional statments - all & any
# all & any, takes a list as an argument and return true if all or any of the
# arguments evaluates as true (or false otherwise)

# *** ENUMERATE *****
# enumerate is used to iterate throug values and indices of a list simultaneously

squareN = [i**2 for i in range (12)]
# note not all the value are greater than 25 - False
if all(i > 25 for i in squareN):  
    print ("all greater than 25")

# note at least one value is greater than 25 - True
if any(i > 25 for i in squareN):
    print ("any greater than 25")

# prints index and value as tuple
for val in enumerate(squareN):
    print (val)

















