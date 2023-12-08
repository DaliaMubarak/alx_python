if __name__=="__main__":
   import sys

a=len(sys.argv)-1
if a==0:
    print ("0 arguments.")
elif a==1:
    print ("1 argument:")
    print("1:{}".format(sys.argv[1]))
else:
    print ("{} arguments:".format(a))
for i in range (a):
      print("{}: {}".format(i,sys.argv[i]))

  
      

