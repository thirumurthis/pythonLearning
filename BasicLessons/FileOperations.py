####################### IMPORTANT - FILE OPERATION##########
# opening a file
# open function is used to open the file before editing, text file are easy to manipulate

openfile= open("testFile.txt") # argument -> path of the file, expect the file to be at this python script level in this case

# additional arguments can be passed, to sepcify the mode of operation

# openfile=open("testFile.txt","w")
# w - means open in write mode (for re-writting the file)
# r - means open in read mode (default)
# a - means open in append mode (for adding new content)
# b - means open in binary mode. (for non-text image files)

# openfile=open("testFile.txt","rb") # binary write mode.

##################### IMPORTANT - FILE READ OPERATION ##############
# reading a file using read functon

### BELOW WILL READ THE ENTIRE CONENT
#content= openfile.read() # uncomment
#print (content) # uncomment

## TO READ ONLY FEW CONTENT
#uncomment 2 lines for testing
#for i in range(4):
#    print(openfile.read(6)) # argument number of bytes

#### NOTE: once the file i read using .read function, then it will reach EOF
#### There won't be any content, will print empty

# uncomment the below statment for testing
#print(openfile.read())
#print(openfile.read()) # empty string, since already read in above statment

########### NOTE: TO READ the file LINE BY LINE use readlines function
# uncomment below statment to test
#print(openfile.readlines()) # as an list of lines


#for loop for testing the same
# uncomment two lines below for testing
#for line in openfile:
#    print(line)

######################## IMPORTANT- WRITING TO THE FLE ############
# write function
# 1. open the fle in write mode

file = open("testFile1.txt","w")
############ NOTE: W mode ############
# w = mode will automatically create a file if not exsists
# w = when file is opened in w (write mode) on read the content is deleted

############ NOTE : Write function ########3
# write function returns number of bytes written successfully 
file.write("Content included \n using the python functions")

file.close()

msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

########### IMPORTANT - USE try except #############33
# good practise to use close function in finally block
try
file = open("newfile.txt", "w")
print( file.read())
except:
    print ("some error occurred")
finally:
    file.close();
    
######################## IMPORTANT - file close function Tips - WITH ################
# if developer need not worry of closing the file then below is the option to use WITH
#An alternative way of doing this is using with statements.
#This creates a temporary variable (often called f), which is only accessible
#in the indented block of the with statement.

with open ("filename.txt") as file:
    print(file.read())  # file is a temp variable accessed within the indented block
        

############################ IMPORTANT - FILE CLOSE OPERATION ########33
# ONCE FILE IS OPENED IT SHOULD BE CLOSED AFTER OPERATION

openfile.close()



