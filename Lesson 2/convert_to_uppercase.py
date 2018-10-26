string = input("String to convert: ")
n = int(input("How many last letters should be converted? "))

# First part of the string
start = string[:len(string) - n]
# last part of the string that we're converting.
end = string[len(string) - n:]

print(start + end.upper())
