print("welcome to roller coaster planet")
height = int(input("Enter the height :"))

if height > 120:
  print("You can ride this roller coaster!")
  age =int(input("Enter the age :"))
  
  if age <12:
    print("Childs tickets are $5")
    
  elif age <=18:
    print("Youth tickets are $8")
    
  else:
    print("Adult tickets are $20")
else:
  print("You are too short ..please eat complain")