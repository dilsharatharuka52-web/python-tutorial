import random
dice_rool = int(random.randint(1,10))


while True:
  try:
     num = int(input("Enter random number"))
     
     if num == dice_rool:
         print("You guessed it!")
     else:
         print("Try again!")

  except ValueError:
      print("only number")