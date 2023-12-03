def validate_password(password):
      if len(password) >0  and len(password) <=8:
            return False
      
        

      for character in password:
            if character.isupper() and character.islower() and character.isdigit():
                  return True
            if character.isspace():
                  return False
            
            
