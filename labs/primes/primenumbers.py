#The function can be represented with O(N2)

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
            raise ValueError
    else:
        raise TypeError