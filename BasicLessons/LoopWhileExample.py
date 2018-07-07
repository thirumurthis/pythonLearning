i =1

while i <=5:
   print ("print %d" % i)
   i += 1
   print("think outside the while loop")

#a space is required to differentiate the block of the loop
   print ("atlast this is end")

# continue and break can be used.
print ("######################## ")
idx = 10

while idx >=0:
   if idx ==5:
      idx -=1
      continue   
   print ("if1 not ==5 idx val %d" %idx)
   if idx ==3:
      break
   print ("idx val %d" % idx)
   idx = idx-1
   
print ("loop ended using continue and break")
   
   
