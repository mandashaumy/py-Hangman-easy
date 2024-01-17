import random
import os
import time
def word():
  words = ['audi', 'lexus', 'opel', 'ford', 'porsche']
  randomword = random.choice(words)
  return randomword

def gameplay(randomword):
  dash = '*'*len(randomword)
  listofdash = list(dash)
  listofrandomword = list(randomword)
  listofletters = []
  guesschance = 6 
  while True:
    print('Welcome to The Hangman\nTry to guess the word below')
    print('Clue: Car Brands  |  Chance:', guesschance)
    print('-'*45)
    print(listofdash)
    print('-'*45)
    print('Letters you have guessed before:\n', listofletters)
    letter = input('Choose Letter = ')
    if len(letter) == 1:
      if letter in listofletters:
        print('You have already guessed that letter before')
        time.sleep(3)
      elif letter not in listofrandomword:
        print(letter, 'is not in the word. Try Again')
        listofletters.append(letter)
        guesschance -=1
        time.sleep(3)
      elif letter in listofrandomword:
        print('Good Job', letter, 'is in the word')
        listofletters.append(letter)
        idx = listofrandomword.index(letter)
        listofdash[idx] = letter
        time.sleep(3)
      else:
        print('Something is not right. Try Again')
        time.sleep(3)
    elif len(letter) > 1:
      print('please input only 1 letter')
      time.sleep(3)
    else:
      print('Something is not right. Try Again')
      time.sleep(3)
    
    if listofdash == listofrandomword:
      print('The Word is', randomword)
      print('Congrats on Winning this game')
      break
    if guesschance == 0:
      print('The Word is', randomword)
      print('Game Over')
      break
    
    os.system('clear')


while True:
  word = word()
  gameplay(word)
  break
