#Print series 1, 2, 4, 8, 16, 32, 64.
def series():
  
  num_terms = 7  
  current_term = 1

  for _ in range(num_terms):
    print(current_term, end=" ")
    current_term *= 2  
    
series()