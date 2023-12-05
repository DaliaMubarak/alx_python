def is_prime(number):
    if number <=0:
        print (False )
    else:
        for i in range (2,number):
            if number % i == 0:
             print (False )
             break
        else:
             print (True )