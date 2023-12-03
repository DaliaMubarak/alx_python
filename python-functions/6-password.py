def validate_password(password):
      if len(password) >0  and len(password) <=8:
            return False
      


      for character in password:
            if character.isupper() or character.islower() or character.isdigit():
                  return False
            
