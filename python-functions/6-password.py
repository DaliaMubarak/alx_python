
      
def validate_password(password):
      if len(password) <8:
            return False
      
      
      else:
            for character in password:
             if " " in password:
                  return False
             if character.isupper() + character.islower() + character.isdigit():
                     return True
             else:
                  return False
          
             