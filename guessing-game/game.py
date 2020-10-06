"""A number-guessing game."""
import random

# Put your code here
secret_num = random.randint(1 , 100) #creates a random number between 1-100
print(secret_num) #prints the random number that has been generated 
guesscount = 0

#asking user for their name and their first guest
username = input("Howdy, What is your name?")
print(f"{username}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

#created two empty variables so they can be populated within the loop 
userguess_str = None
userguess = None

#loop runs until the user guesses the correct number
while secret_num != userguess:
    userguess_str = input("Your guess? ") #Asks the user for their guess
    userguess = int(userguess_str) #turns the users guess from a string to an int
    if secret_num > userguess: #checks if the random number is less than the users guess if so prints the statement and increases the guess count by 1
        print("Your guess is too low, try again.")
        guesscount += 1
    elif secret_num < userguess: #checks if the random number is greater than the users guess if so prints the statement and increases the guess count by 1
        print("Your guess is too high, try again.")
        guesscount += 1
    else:
        guesscount += 1 #count needs to come before the print statement otherwise the guesscount will be one off 
        print(f"Well done, {username}! You found my number in {guesscount} tries.")
        
