listval = [1,2,3,4,5,6]

print ("value at idx 1 %d " % listval[1])

somenum =2**4
lst = [1, [20,21,somenum],3,4]

print(lst[1][2]) #16

lst[1][2] = somenum**2

print(lst[1][2]) #256 (16^2)

frstList = [4,3,2,1]
secondList = [10,9,8]

print (frstList + secondList) # adds both the list

print (secondList *2) # prints the same list twice.

################# USING LIST - IN operator ############
# checks if the value exists in the list
list1 = ["one","two", ["1three","1four"]]

print ("one" in list1) # True
print ( "1four" in list1) # False
print ( "1four" in list1[2]) # True

################# USING LIST - Append method ############
# appends an value to the end of the list
list1.append("new array");
print ( " new array included ") 
print( "new array" in list1) # True

################ USING LIST - len function - not within list like append ############
# len function prints the length of the list
print ("lenght of the list %d " % len(list1))

################ USING LIST - INSERT function ###############
# inserts value between list

list1.insert(2,"new insert")

print (list1)

nums= [9,8,7,6,5]
nums.append(4)
nums.insert(2,11)
print(len(nums))

#################### USING LIST - INDEX method ##################
# returns the int index of the value in the list  

indexval = list1.index('new insert')
print("new insert is at the index 2 %d " %indexval)

#There are a few more useful functions and methods for lists. 
#max(list): Returns the list item with the maximum value
#min(list): Returns the list item with minimum value
#list.count(obj): Returns a count of how many times an item occurs in a list
#list.remove(obj): Removes an object from a list
#list.reverse(): Reverses objects in a list

print (max(nums))
listtmp = [1,2,2,3,4,5,5,5,5,6,] # end , is allowable


#counts the occurance of the value in the list
print ("Count of 5 in array expected 4 = %d " %listtmp.count(5));

###################### USING LIST - RANGE ###############
# range creates set of sequenctial number in the list

rangeList = list(range(10)) # range itself creates a list object
print(rangeList)

range1= list (range(3,8)) # specify the start and the end of the range
print(range1)

print(range(20) == range(0,20)) # true

#range with three parameter
range2 = list(range(1,15,2)) # 3rd parameter is for increment sequence 
print (range2)


