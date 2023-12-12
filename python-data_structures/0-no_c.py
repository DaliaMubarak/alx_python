def no_c(my_string):
    
    for char in my_string:
        if char=="c":
         return my_string.translate({ord('c'): None})
        elif char=="C":
          return my_string.translate({ord('C'): None}) 
