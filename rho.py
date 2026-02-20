"""
Used in:
    - https://leetcode.com/problems/largest-component-size-by-common-factor/
"""
import math
import random
from collections import Counter

def miller_rabin_a_base_check(n, d, s, a):
    if n == a:
        return True
    # If a^d == +/- 1 (mod n)
    x = pow(a,d,n)
    if x == 1 or x == n-1:
        return True
    
    for _ in range(s-1):
        x = (x*x) % n
        if x == 1:
            return False
        if x+1 == n:
            return True
    return False
        

def is_prime_miller_rabin(n):
    """ True iff n is prime """
    if n == 1:
        return False
    
    # Let s,d be so: 2^s * d == n - 1
    d = n - 1
    s = 0
    while not (d&1):
        s += 1
        d = d>>1
    
    bases = [2,3,5,7,11,13,17,19,23]
    for a in bases:
        if not miller_rabin_a_base_check(n, d, s, a):
            return False
    return True

def get_divisor_rho(n):
    """ Finds a divisor or loop forever """
    if not (n&1):
        return 2
    
    while True:
        constant = random.randint(1,n)
        def f(x):
            return (x*x + constant) % n

        a = 2
        b = 2
        d = 1
        while d == 1:
            a = f(a)
            b = f(f(b))
            d = math.gcd(abs(a-b), n)
        
        if d < n:
            return d

def factorization_rho(n):
    factors = Counter()
    if n == 1:
        return factors
    stack = []
    stack.append(n)
    while stack:
        x = stack.pop()
        if is_prime_miller_rabin(x):
            factors[x]+=1
        else:
            d = get_divisor_rho(x)
            stack.append(d)
            stack.append(x//d)
    return factors
    
if __name__ == "__main__":
    print(factorization_rho(24))
    print(factorization_rho(200))