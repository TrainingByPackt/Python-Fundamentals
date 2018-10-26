def dictionary_masher(dict_a, dict_b):
  for key, value in dict_b.items():
    if key not in dict_a:
      dict_a[key] = value
      
  return dict_a