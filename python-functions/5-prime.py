def is_prime(number):
    for i in range (number,number-1):
        if number % i == 0:

          return True
    else:
          return False