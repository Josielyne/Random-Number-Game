##Programmer: Joselyne Guillen
##File Name: randomNum.py 
##Date: 2/7/21
##Version: 1.5
##Explanation of Program: 
##This program generates a random number between
##1 and 100 and has the user guess the value.
##Every guess, the program tells the user if
##their guess is either too high, too low, or 
##correct. If the guess is too high or low, the
##program has the user try again. The program 
##also keeps track of how many times the user has
##guessed. If the user guesses the correct number,
##the program notifies them and tells them how many
#times they guessed. It then restarts the game with
#a new randomly generated variable.

import random #loads contents of random module into memory
def main(): #main function
    numofG = 0 #initializes variable to keep track of how many times the user guesses
    rnum = random.randint(1,100) #initializes variable with randomly generated number between 1 and 100
    guess(rnum,numofG) #function call for guess function and passes two arguments
def guess(x,y): #guess function with two parameters
    userGuess = int(input('Guess a number between 1 and 100\n'))#asks the user to guess a number between 1 and 100 and collects user input
    while y<y+1: #while loop that keeps executing as long as the user doesn't guess the correct value
        if(userGuess > x):#if statement that executes if guess is higher than randomly generated number
            print('Too high, try again\n')#tells user guess is too high
            userGuess = int(input('Guess a number between 1 and 100\n'))#has user try again
            y+=1 #increases the number of times the user has guessed by 1
        if(userGuess < x):#if statement that executes if guess is lower than randomly generated number
            print('Too low, try again\n')#tells user guess is too low
            userGuess = int(input('Guess a number between 1 and 100\n'))
            y+=1
        if(userGuess==x):#if statement that executes if user guessed the correct number
            print('****************************************************\n')#border
            print('Congratulations ^.^! You guessed the correct number!\n')#tells user they guessed correctly
            print('You guessed ',y+1, ' times\n')#tells user how many times they guessed
            print('****************************************************\n')
            y=0 #resets guess value
            break #breaks from the while loop
    print('--------------------------')#border
    print('The game will now restart.')#tells the user the game will restart with a new value
    print('--------------------------')
    main()#function call for the main function

main()
        
        
    
