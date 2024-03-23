print("welcome to roller coaster")

height =int(input("Enter your height:"))
bill=0

if height > 120:
  print("You can ride this rollercoaster")
  age =int(input("Enter your age:"))
  if age <12:
    bill=5
    print("Children tickets are :$5")
  elif age <=18:
    bill = 9
    print("Youth tickets are :$9")
  
    
  elif age >= 45 and age <=55:
    bill =0
    print("$0")
  else :
    bill =20
    print("Adult tickets are :$20")
    
     
  want_photo = input("Do you want to take a photo! Y or N .")
  if want_photo =='Y':
    bill +=3
  print(f"Your final bill : {bill}")
    
  
  
else:
  print("You are not allowed to ride this roller")