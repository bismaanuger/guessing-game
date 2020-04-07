#!/usr/bin/env python
# coding: utf-8

# # Guessing Game Challenge
# 
# Let's use `while` loops to create a guessing game.
# 
# The Challenge:
# 
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
# 
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
# 

# #### First, pick a random integer from 1 to 100 using the random module and assign it to a variable
# 
# Note: `random.randint(a,b)` returns a random integer in range `[a, b]`, including both end points.

# In[20]:


#Creating a random number
from random import randint

rand_num = randint(1,101)


# #### Next, print an introduction to the game and explain the rules

# In[21]:


print("\nWELCOME TO GUESS GAME!\n")
print("I have a number from 1 to 100 in my mind.")
print("You have to pick a number to guess.\n")
print("On yours first turn, if the guess is:")
print('- Within 10 of the number, return "WARM!"')
print('- Further than 10 away from the number, return "COLD!"\n')
print('On all subsequent turns, if a guess is:')
print('- Closer to the number than the previous guess return "WARMER!"')
print('- Farther from the number than the previous guess, return "COLDER!"\n')


# #### Create a list to store guesses
# 
# Hint: zero is a good placeholder value. It's useful because it evaluates to "False"

# In[22]:


guesses = []


# #### Write a `while` loop that compares the player's guess to our number. If the player guesses correctly, break from the loop. Otherwise, tell the player if they're warmer or colder, and continue asking for guesses.
# 
# Some hints:
# * it may help to sketch out all possible combinations on paper first!
# * you can use the `abs()` function to find the positive difference between two numbers
# * if you append all new guesses to the list, then the previous guess is given as `guesses[-2]`

# In[24]:


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
                
    elif len(guesses) <= 1:
        if abs(guess_num - rand_num) <= 10:
            print("WARM!")
        else:
            print("Cold...")
            
    elif len(guesses) > 1:
        if abs(guesses[-1] - rand_num) < abs(guesses[-2] - rand_num):
            print('WARMER!!!')
        else:
            print('Colder...')
        

   


# That's it! You've just programmed your first game!
# 
# In the next section we'll learn how to turn some of these repetitive actions into *functions* that can be called whenever we need them.

# ### Good Job!
