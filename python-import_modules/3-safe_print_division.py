

def safe_print_division(a, b):
 
 try:
   a/b
 except:
  return "none"
 else:
   return (a/b)
 finally:
  print ("inside result: {}".format(safe_print_division(a,b))) 
 
 