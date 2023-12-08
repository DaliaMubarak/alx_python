if __name__=="__main__":
   import sys
for arg in sys.argv[1:]:
  a=len(sys.argv)-1
  if a==0:
    print ("0 arguments.")
  elif a==1:
    print ("1 argument:")
    print("1: {}".format(arg))
  else:
    print("{} arguments\n".format(a)"{}: {}".format(sys.argv.index(arg),arg))

  
      

