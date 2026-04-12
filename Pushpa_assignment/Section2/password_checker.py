import re
password=input("Enter password: ")
score=0
if len(password)>=8:
   score+=1
else:
    print("Password should be at least 8 characters")
if re.search("[A-Z]",password):
   score+=1
else:
    print("Add uppercase letters")
if re.search("[a-z]",password):
   score+=1
else:
   print("Add lowercase letters")
if re.search("[0-9]",password):
   score+=1
else:
    print("Add numbers")
if re.search("[!@#$%^&*]",password):
   score+=1
else:
    print("Add special characters")
if score<=2:
   print("Strength: Weak")
elif score<=4:
   print("Strength: Medium")
else:
   print("Strength: Strong")
