def validate_password(password):
      if len(password) <8:
            return False
      elif ' ' in password:
                  return False
      
      else:
            for character in password:
             
             if character.isupper() and character.islower() and character.isdigit():
                  return True
             else:
                  return False
           
            
