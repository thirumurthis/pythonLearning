useroption = ["A" , "a","S" ,"s" ,"M" ,"m", "D" , "d"]
result =0 
while True:
    print ("Enter options:")
    print ("Option to add two numbers - A/a")
    print ("Option to subtract two numbers - S/s")
    print ("Option to multiply two numbers - M/m")
    print ("Option to divide two numbers - D/d")
    print ("Option to quit - Q/q ")
    print ("Enter options A/S/M/D")
    user_input=input( "Enter an option: ")
    if not user_input in  useroption:
        break
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter second number : "))
    #print (user_input)
    if user_input == 'A' or user_input == 'a':
            result = number1+number2
    if user_input == 'S' or user_input == 's':
            result = number1-number2        
    if user_input == 'm' or user_input == 'm':
            result = number1*number2        
    if user_input == 'D' or user_input == 'd':
            result = number1/number2        
    print ("Result : %d %d = %d " %(number1,number2,result))
