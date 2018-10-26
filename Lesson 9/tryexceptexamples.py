# simple try...except block
try: 
    with open('input.txt', 'r') as myinputfile: 
        for line in myinputfile: 
            print(line) 
except FileNotFoundError: 
    print("Whoops! File does not exist.") 
   
# try..except with error grouping
try: 
    with open('input.txt', 'r') as myinputfile: 
        for line in myinputfile: 
            print(line) 
except (FileNotFoundError, ValueError): 
    print("Whoops! File does not exist.") 
   

# try..except with individual grouping
try: 
    with open('input.txt', 'r') as myinputfile: 
        for line in myinputfile: 
            print(line) 
except FileNotFoundError: 
    print("Whoops! File does not exist.") 
except ValueError: 
    print("A value error occurred") 

# try...except...else
try: 
    with open('input.txt', 'r') as myinputfile: 
        for line in myinputfile: 
            print(line) 
except FileNotFoundError: 
    print("Whoops! File does not exist.") 
except ValueError: 
    print("A value error occurred") 
except Exception: 
    print("Something unforeseen happened") 
else: 
    print("No error because file exists") 

# using the finally keyword
try: 
    with open('input.txt', 'r') as myinputfile: 
        for line in myinputfile: 
            print(line) 
except FileNotFoundError: 
    print("Whoops! File does not exist.") 
except ValueError: 
    print("A value error occurred") 
except Exception: 
    print("Something unforeseen happened") 
finally: 
    print("I will always show up") 
   
