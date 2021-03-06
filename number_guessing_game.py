'''
After many attempts to run this and get the computer to guess a number, I discovered the problem!
In the If statement, the else would always run because player_guess and pc_guess couldn't be compared.
Despite an earlier attempt to change player_guess to an int, it wouldn't work. I had to make the player
input an int right away using parantheses.
'''

import random

tries = 3
while tries > 0:
  pc_guess = random.randrange(1, 10)
  player_guess = int(input(f"Guess the number I've picked - tries remaining: {tries}: "))
  if player_guess == pc_guess:
    print(f"You win! I guessed: {pc_guess}")
    tries = 0
  else:
    print(f"You lose! I guessed: {pc_guess}, you guessed: {player_guess}")
    tries -= 1
