# Program pick a number 1-100
# User pick one number
# Program output right or wrong
# Program give hint if the number too high or low
# Keep track of tries


import random

def pick_number(start, end):
    return random.randint(start, end)

number = pick_number(1, 100)
print(number)  # This will show the number, if you want it to be a surprise, remove this line

while True:
  guess = int(input("Guess a number from 1 to 100: "))
    
  if guess == number:
    print("Correct")
    break
  elif guess > number:
    print("Incorrect! The number is smaller, please guess again: ")
      
  elif guess < number:
    print("Incorrect! The number is bigger, please guess again: ")

  else:
    print("That number is invalid! Try again:")