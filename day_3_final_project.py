print("Welcome to the tressure island")
print("Your mission is to find the tressure")

choice1 = input('you are at a crossroad,where do you want to go? Type "left" or "right" .').lower()

if choice1 == "left":
  choice2 = input('You have come to a lake.There is an island in the middle of the lake.Type "wait" to wait for for a boat or Type "swim" to swim across . ').lower()
  
  if choice2 == "wait":
    choice3 = input('which door you want to go? type "Red" ,"Blue" or  "Yellow".')
    if choice3 == "Red":
      print("Burned by fire.Game Over.")
    elif choice3 == "Blue":
      print("Eaten by beasts.Game Over.")
    else:
      print("yay! You win.")
  else:
    print("Attacked by trout.Game Over.")
  
else:
  print("Fall into a hole.Game Over.")