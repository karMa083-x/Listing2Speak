'''
Mystery Number Guesser
Get a random number between 1-1000
give the player 5 guesses
  -output whether the guesses number is too high or low
after 5 guesses reveal the number if the player has guessed wrong
'''
import random
x=random.randint(1,1000)
count=5
while (count>0):
  y=input('plz guess a number')
  y=int(y)
  if (y==x):
    print('bingo')
    count=0
  if (y<x):
    print('too small')
  if (y>x):
    print('too big')
  count-=1
if(y!=x):
  print('You Lost!')
  