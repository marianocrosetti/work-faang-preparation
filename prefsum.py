from collections import defaultdict

A = [ -2,	1,	-3,	4,	-1,	2,	1,	-5,	4 ]
X = 2
n = len(A)

S = [0 for _ in range(n+1)]
for i in range(n+1):
    S[i] = S[i-1] + A[i-1]

answer = 0
Sl_contador = defaultdict(int)
for r in range(n):
    # contar S[l] == S[r] - X
    Sl_contador[S[r]] += 1
    print(r, Sl_contador[S[r+1] - X])
    answer += Sl_contador[S[r+1] - X]

print(answer)
    