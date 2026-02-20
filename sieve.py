
def eratosthenes_sieve(max_num):
    sieve = [ None for _ in range(max_num+1) ]
    primes = []
    for p in range(2,max_num+1):
        if not sieve[p]:
            sieve[p]=p
            for i in range(p*p,max_num+1,p):
                if not sieve[i]:
                    sieve[i] = p
            primes.append(p)
    return sieve, primes

