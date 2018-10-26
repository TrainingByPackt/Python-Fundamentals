class RecipeNotValidError(Exception): 
    def __init__(self): 
        self.message = "Your recipe is not valid" 
     
try:   
    raise RecipeNotValidError 
except RecipeNotValidError as e: 
    print(e.message) 