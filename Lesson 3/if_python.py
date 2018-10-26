answer = input("Return TRUE or FALSE: Python was released in 1991:\n")

if answer == "TRUE":
 print('Correct')
elif answer == "FALSE":
 print('Wrong')
elif answer != ("TRUE" or "FALSE"):
 print('Please answer TRUE or FALSE')
print('Bye!')