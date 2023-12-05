def validate_password(password):
      if len(password) <8:
            return False
      
      
      else:
            for character in password:
                       
             if not (any(character.isupper()) and any (character.islower()) and any (character.isdigit())):
                  return False
             elif ' ' in password:
                  return False
             else:
                  return True
           
            
