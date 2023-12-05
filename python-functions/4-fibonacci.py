def fibonacci_sequence(n):
 a=0
 b=1
 
 if n <1:
   return list()
 elif n==1:
    return [a]
 for i in range (2,n):
       c=a+b
       a=b
       b=c
       return [c]