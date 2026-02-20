
class Solution:
    def __init__(self):
        pass
    
    def solve(self, x):
        return x
        

def check_eq(a,b):
    assert a==b, print(f"Expected: {a}\nResult:{b}")        

if __name__ == "__main__":
    solution = Solution()
    
    check_eq( 10 , solution.solve(10)  )
    print('OK!')
    
