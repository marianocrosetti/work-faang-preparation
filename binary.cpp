def binary(A, x):
    n = len(A)
    a = -1 # C[a] == 0
    b = n  # C[b] == 1
    """
    a  ....  m  .... b
    0  ....  1  .... 1
    """
    while b - a > 1:
        m = (a+b)//2
        if (A[m] >= x) == False:
            a = m # C[a] == 0
        else:
            b = m # C[b] == 1
    
    # a y b son consecutivos
    # o sea: a + 1 == b
    # Ademas el invariante nos dice que:
    # C[a] == 0
    # C[b] == 1
    if b == n:
        return -1
    
    if A[b] == x:
        return b
    
    return -1
            
    

A = [3,5,7,12,22,22,37,40]
p = binary(A, 60)
print(p)
    
