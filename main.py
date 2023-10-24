# Program pick a number 1-100
# User pick one number
# Program output right or wrong
# Program give hint if the number too high or low
# Keep track of tries

import random


def pick_number(start, end):
  return random.randint(start, end)


number = pick_number(1, 100)
print(number)  # This will show the number to test, remove this line when finished.

tries = 0 #Initializing tracking number of tries(counter tool)

while True:

  tries += 1
  
  user_input = input("Guess a number from 1 to 100: ")

  try:
   
    guess=int(user_input)
    
    if guess == number:
      print(f"Correct! you guess it in {tries} tries.")
      break
    
    elif 1 <= guess <= 100:
      
      if guess > number: 
        print("Incorrect! The number is smaller, please guess again!")
  
      else: #This cover when user input smaller number
        print("Incorrect! The number is bigger, please guess again!")
        
    else:
      print("That number is out of the range of 1-100. Please stay within the range!")
  
  except ValueError:
    print("That is an invalid input, please enter an integer from 1-100!" )
  