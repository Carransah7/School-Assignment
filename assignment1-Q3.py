def validate(n):
    #Changes n to string
    n = str(n)

    # Check if the input is a 14-digit number
    if len(n) != 14:
        return "You did not enter a 14-digit integer."
    
    #Initializes sum1 and sum2
    sum1 = 0
    sum2 = 0
    
    #Loops through 14-digit integer
    for i in range(14):
        num = int(n[i])
        #Checks if the number is even
        if i % 2 == 0:
            # Double it
            doubled = num * 2
            #Checks if the doubled number is greater than 9
            if doubled > 9:
                doubled -= 9
            #Adds it to sum1
            sum1 += doubled
        #Adds the number to sum2     
        else:
            sum2 += num
    #Adds sum1 and sum2
    total = sum1 + sum2
    #Checks if the total is divisible by 10
    return total % 10 == 0

#Asks user to enter a 14-digit integer
user = input("Enter a 14-digit integer: ")

#Validates the user input
result = validate(user)
#Checks if result is a boolean
if type(result) == bool:
    #If result is True prints that the user input is validated
    if result:
        print(user, "is validated.")
    #If result is False prints that the user input is not validated     
    else:
        print(user, "is NOT validated.")
#If result is not a boolean prints the result        
else:
    print(result)