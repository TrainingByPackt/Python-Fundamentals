for number in range(0,200):
  if number == 0:
    continue
  elif number % 3 != 0:
    continue
  elif type(number) != int:
    continue
  else:
    pass
  print(number)