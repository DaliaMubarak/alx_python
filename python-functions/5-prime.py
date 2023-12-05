def is_prime(number):
    if number == 0:
        return False
    else:
        for i in range (2,number):
            if number % i == 0:
             return False
             break
        else:
             return True