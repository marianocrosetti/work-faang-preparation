
cache = [None for _ in range(100)]

def fibo(n):
    if cache[n] is not None:
        return cache[n]
    if n<=1:
        cache[n] = 1
    else:
        cache[n] = fibo(n-1) + fibo(n-2)
    return cache[n]
            
    

for i in range(35):
    print(i, fibo(i))
    
