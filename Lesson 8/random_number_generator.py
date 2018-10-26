def random_number_generator(l):
    """
    Generate a list of random numbers of length l.
    """
    output = []
  
    for i in range(l):
      output.append(random.randint(0, 1000))
    
    return output