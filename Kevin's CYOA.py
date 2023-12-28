yes_no = ["yes", "no"]

name = input("Who disturbs my slumber?\n")
print("Enter if you dare, " + name)
print("But be warned! Your fate will be decided by the roll of a die.")
print("Do you want to continue?\n")

response = " "
while response not in yes_no:
    response = input("Would you like to continue on your quest?\nyes/no\n")
    if response == "yes":
       print("Roll the die to reveal your fate. you have to reach 25 to win\n")
       print("You have 7 moves...may the fates be with you\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that. Try again\n")

import random
def roll_die():
  # Generate a random number between 1 and 6 (for a 6-sided die)
  roll = random.randint(1, 6)
  return roll

new_position = 0
roll_limit = 7

while True:
  # Prompt the user to press Enter to roll the die
  input("Press Enter to roll the die: ")

  # Roll the die and print the result
  roll_result = roll_die()

 # Update the cumulative sum
  new_position += roll_result

  # Print the roll result and the cumulative sum
  print("Roll result:", roll_result)
  print("New position:", new_position)

   # Decrement the roll limit
  roll_limit -= 1

  # Print a message when the roll limit is reached
  print("Number of moves remaining:", roll_limit)



  if new_position>=25:
     print("Congratulations " + name, " you won the quest!")
     print("You have safe passage!")
     break
  elif roll_limit==0:
    print("You are out of time " + name, " Now you are mine! Ha ha ha ha")
    break

  if (new_position==16):
      new_position=8
      print("You fell down a trap door!, you have slid down to 8")
  elif (new_position==19):
      new_position=7
      print("You fell down a trap door!, you have slid down to 7")
  elif (new_position==23):
      new_position=9
      print("You fell down a trap door!, you have slid down to 9")


  if (new_position==4):
      new_position=15
      print("You found a lift!, ride up to 15")
  elif (new_position==13):
      new_position=17
      print("You found a lift!, ride up to 17")
  elif (new_position==11):
      new_position=21
      print("You found a lift!, ride up to 21")

