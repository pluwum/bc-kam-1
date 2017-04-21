"""
    Function that returns Prime numbers between 0 to N
"""

#check if number is a prime
def isPrime(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    else:
        return True

#return list of primes from 0 to Number
def primes(number):
    primes = []
    if isinstance(number,int):
        if number >= 0:
            for x in range(2, number+1):
                if(isPrime(x)):
                    primes.append(x)
            return primes
        else:
            raise ValueError("Argument passed should be a positive integer")
    else:
        raise TypeError("Argument passed should be an integer")