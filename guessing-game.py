#!/usr/bin/env python
# coding: utf-8

# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# 
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is
#  * within 10 of the number, return "WARM!"
#  * further than 10 away from the number, return "COLD!"
# 3. On all subsequent turns, if a guess is 
#  * closer to the number than the previous guess return "WARMER!"
#  * farther from the number than the previous guess, return "COLDER!"
# 4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!



#Creating a random number
from random import randint

rand_num = randint(1,101)

#Game Introduction
print("\nWELCOME TO GUESS GAME!\n")
print("I have a number from 1 to 100 in my mind.")
print("You have to pick a number to guess.\n")
print("On yours first turn, if the guess is:")
print('- Within 10 of the number, return "WARM!"')
print('- Further than 10 away from the number, return "COLD!"\n')
print('On all subsequent turns, if a guess is:')
print('- Closer to the number than the previous guess return "WARMER!"')
print('- Farther from the number than the previous guess, return "COLDER!"\n')

#Placeholder
guesses = []




while True:
    #Player input a number
    guess_num = int(input("Please pick a number: "))
       
    #Logic if "out of bound"
    if guess_num < 1 or guess_num > 100:
        print("OUT OF BOUND")
        continue
        
    guesses.append(guess_num)
                
    #Logic if correct
    if guess_num == rand_num:
        print(f"Congratulation, you're correct! Your guess is {len(guesses)} times.")
        break
    
    #Logic for the first try            
    elif len(guesses) <= 1:
        if abs(guess_num - rand_num) <= 10:
            print("WARM!")
        else:
            print("Cold...")

    #logic for second try and so on
    elif len(guesses) > 1:
        if abs(guesses[-1] - rand_num) < abs(guesses[-2] - rand_num):
            print('WARMER!!!')
        else:
            print('Colder...')
        
