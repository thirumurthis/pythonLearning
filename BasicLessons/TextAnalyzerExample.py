############## TEXT ANAYZER ###############

# OPEN A FILE
#From documentation of python max split
# uncomment for testing
#print('1,2,3,4,5'.split(',', maxsplit=1))
# out put ['1','2,3,4,5']

#counts the char
def charCount(text, character):
    charCnt=0
    for char in text:
        if char == character:
            charCnt +=1
    return charCnt

#compute simple percentage
def computePercentage(text):
    for char in 'abcdefghijklmnopqrstuvwxyz':
        percent = 100 * charCount(text,char) / len(text)
        print ("{0}-{1}%".format(char,round(percent,2)))

with open("newfile.txt","r") as file:
    for text in file.readlines():
        #charCount(text,"e")
        computePercentage(text)   


# Text analysis to be improvized more - declared as doc comments for now
# remove this """ latter if needed
# with open("newFile.txt","r") as file:
#    for text in file.readlines():
#        for word in text.split():
#            for idx in range(0,len(word)):
#                print ("%s %s %d"%(word,word[idx], charCount(word,word[idx])))

########################### QUIZ ########################
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))

# output ??? 44
