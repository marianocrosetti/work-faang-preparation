# 137, 1000000007 1000000009
class HashSubstring:
    def __init__(self, s, base_p=137, mod_p=10**9+7):
        self.n = len(s)
        self.mod_p = mod_p
        
        self.pot = [ 1 for _ in range(self.n+1) ]
        for i in range(1,n+1):
            self.pot[i] = base_p * self.pot[i-1]
            self.pot[i] %= mod_p 

        self.hash_prefix = [ 0 for _ in range(n+1) ]
        for i in range(1,n+1):
            self.hash_prefix[i] = self.hash_prefix[i-1] + (self.pot[i-1] * ord(s[i-1])) % mod_p
            self.hash_prefix[i] %= mod_p
§
    def hash_substr(self, i, j):
        h = self.hash_prefix[j] - self.hash_prefix[i]
        h = (h + self.mod_p) % self.mod_p
        h *= self.pot[self.n - i]
        h %= self.mod_p
        return h