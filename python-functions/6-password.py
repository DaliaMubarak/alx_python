def validate_password(password):
      if len(password) <8:
            return False
      
      else:  

        for character in password:
             if character.isspace():
                  return False
             elif any(character.isupper()) and any (character.islower()) and any(character.isdigit()):
                  return True
             else:
                 return False
           
            
