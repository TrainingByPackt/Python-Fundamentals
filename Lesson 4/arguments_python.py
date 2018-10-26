def print_arguments(*args):
  for value in args:
    if type(value) == int:
      continue
    print(value)