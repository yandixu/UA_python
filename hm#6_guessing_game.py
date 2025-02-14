#Yandi Xu
#CSC110, Section: 001k
#Project #6: Guessing Game
#This project uses while loops, input,and random numbers to build a program
# allow users to guessing a random number， and return the total time they did
# correct.

from random import*
CONSTANT = 5  #define the constant number used in whole program
def main():
    haiku()
    print()
    new = 0   #the replay times of guessing function.
    games = 1  #the total times that the game been played.(accumulated)
    best = 1000  #a number used to find the minimum guessing times in pre game.
    guesses = guessing()  #total guessing time among all guesses.(accumulated)
    #compare to find the minimum of each time used by user.
    best = min(best,guesses) 
    replay = input("Do you want to play again? ")

    #the while loop is used to replay game.
    while replay.lower() in "yes":
        games += 1
        print()
        new = guessing() #redefine the parameter.
        guesses += new 
        best = min(best,new)
        replay = input("Do you want to play again? ")
   
    print()
    overall(guesses,games,best)

#This function wrote a haiku intro. of the wholr program.        
def haiku():
    print("A random number")
    print("Guessed by player, compare")
    print("Repeat, accumulate")

#This function used input, while loops, and return to run a game once.
#Parameter: time: how many time user used to guess the number.
#           num: the ranodm number user suppose to guess.
#           guess: the number user guessed.
#Return: the time user used to guessed the random number.
def guessing():
    time = 1
    num = randint(1,CONSTANT)
    print("I'm thinking of a number between 1 and",str(CONSTANT)+"...")
    guess = int(input("Your guess? "))

    # the while loop is used to compare and give results.
    while (guess != num):
        time += 1
        if (guess < num):
            print("It's higher.")
        elif (guess > num):
            print("It's lower.") 
        guess = int(input("Your guess? "))
           
    print("You got it right in",time,"guesses!")
    return time  #return total guessing times in one game.

#This function is used to get the summary information of total guessing game.
#Parameter: guesses
#           games
#           best
def overall(guesses,games,best):
    print("Overall results:")
    print("Total games   =",games)
    print("Total guesses =",guesses)
    print("Guesses/game  =",guesses/games)
    print("Best game     =",best)

main()
    
