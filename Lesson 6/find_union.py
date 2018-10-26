def find_union(list_a, list_b):
  union = []
  
  for element in list_a + list_b:
    if element not in union:
      union.append(element)
      
  return union