

T = [
    [1,7,9,2],
    [8,6,3,2],
    [1,6,7,8],
    [2,9,8,2],
]

T = [[1 for _ in range(13)] for _ in range(13)]

N = len(T)
M = len(T[0])

# con cache complejidad:
# O(cant estados . complejidad cada estado sin tener en cuenta las llamdas recursivas)
# O( N^2 . )

distMin = [[ None for _ in range(M)] for _ in range(N)]


for j in range(M-1,-1,-1):
    for i in range(N-1,-1,-1):
        # calcule distMin[i][j]
        if i==N-1 and j==M-1:
            distMin[i][j] = T[i][j]
        elif j==M-1:
            distMin[i][j] = T[i][j] + distMin[i+1][j]
        elif i==N-1:
            distMin[i][j] = T[i][j] + distMin[i][j+1]
        else:
            distMin[i][j] =  min(
                T[i][j] + distMin[i][j+1],
                T[i][j] + distMin[i+1][j],
            )

print(distMin[0][0])
    
