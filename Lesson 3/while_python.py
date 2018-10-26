user_pass = "random"
valid = False
while not valid:
 password = input("please enter your password: ")
 if password == user_pass:
   print("Welcome back user!")
   valid = True
 else:
   print("invalid password, try again... ")