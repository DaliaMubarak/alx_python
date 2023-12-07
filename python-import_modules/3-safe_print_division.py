

def safe_print_division(a, b):
 if b==0:
   return None
 else:
   return a/b
 
a=15
b=0


try:
   a/b

except:
  print ("inside result: {}".format(safe_print_division(a,b))) 
 
else:
  print("inside result: {}".format(safe_print_division(a,b)))

finally:
   print ("{} / {} = {} ".format(a,b,(safe_print_division(a,b))))

safe_print_division(a,b)