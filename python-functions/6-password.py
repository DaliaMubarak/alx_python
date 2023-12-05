def validate_password(password):
      if len(password) <8:
            return False
      
      
      else:
            for character in password:
             
             if not (character.isupper() and character.islower() and character.isdigit()):
                  return False
             elif ' ' in password:
                  return False
             else:
                  return False
           
            
