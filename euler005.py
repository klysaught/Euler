from math import sqrt

sieveSize = 20
#print sieveSize

def simpleSieve(sieveSize):
    #creating Sieve.
    sieve = [True] * (sieveSize+1)
    # 0 and 1 are not considered prime.
    sieve[0] = False
    sieve[1] = False
    for i in xrange(2,sieveSize+1):
        if sieve[i] == False:
            continue
        pointer = pow(i,2)
        while pointer < sieveSize+1:
			sieve[pointer] = False
			pointer+=i
    # Sieve is left with prime numbers == True
    primes = []
    for i in xrange(sieveSize+1):
        if sieve[i] == True:
            primes.append(i)
    return primes

primes = simpleSieve(sieveSize)

prod=1

for prime in primes:
  i=0
  while pow(prime,i)<20:
    i+=1
    if pow(prime,i)>20:
      prod=pow(prime,i-1)*prod

print prod