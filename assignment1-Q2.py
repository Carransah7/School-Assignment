#imports random module
import random

#Generates a random number between 5 million and 500 trillion
num = random.randint(5000000, 500000000000000)

#Prints number without and with grouping(s)
print(f"Without grouping n = {num}")
print(f"With grouping n = {num:,}")

def verbalize(n):
    #List of word endings for the number
    endings = ['','thousand','million','billion','trillion']
    #Empty list to store words
    words = []
    #Iterates through the number and appends the word ending to the list
    for end in endings:
        #Checks if the number remainder is greater than 0 when divided by 1000
        if n % 1000 > 0:
            #Inserts the remainder and word ending to the list
            words.insert(0, f"{n % 1000} {end}")
        #Divides the n by 1000 and rounds down to the nearest whole number
        #Reduce the number N BY FACTORS OF 1000 helps to verbalize the number in terms of thousands, millions, billions and trillions     
        n //= 1000
        #Returns list of words
    return '\n'.join(words)

#Calls verbalize() with the random integer generated from the random module and prints the verbalization
print(verbalize(num))

#For part iii there was no sample output in the assignment so I wasn't sure how you wanted this part to be displayed
#Calls verbalize() with n = 2983004456000
print("Verbalization of 2983004456000:")
print(verbalize(2983004456000))
