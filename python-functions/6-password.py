def validate_password(password):
      if len(password) <8:
            return False
      
      else:  

        for character in password:
             if character.isspace():
                  return True
             elif character.isupper():
                  return True
             if character.islower():
                  return True
             if character.isdigit():
                  return True
             else:
                 return False
           
            
