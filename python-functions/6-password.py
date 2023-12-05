def validate_password(password):
      if len(password) <8:
            return False
      
      else:  

        for character in password:
             if character.isspace():
                  return False
             elif character.isupper():
                  return False
             if character.islower():
                  return False
             if character.isdigit():
                  return True
             else:
                 return False
           
            
