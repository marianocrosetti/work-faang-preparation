class SegmentTree:
    def __init__(self, n, operation_fn):
        self.size = 1 << (n.bit_length() + 1 )
        self.tree = [None for _ in range(2*self.size)]
        self.operation_fn = operation_fn
        print(self.size)
    
    def operation(self, x, y):
        if x is None:
            return y
        if y is None:
            return x
        return self.operation_fn(x,y)
    
    def update_all(self):
        for i in range(self.size-1,-1,-1):
            self.tree[i] = self.operation(self.tree[2*i], self.tree[2*i+1])
    
    def get(self, i, j):
        return self._get(i,j,1,0,self.size)
    
    def _get(self, i, j, node, node_a, node_b):
        if i >= node_b or j <= node_a:
            return None
        if i <= node_a and j >= node_b:
            return self.tree[node]
        mid = (node_a + node_b) // 2
        left = self._get(i, j, 2*node, node_a, mid)
        right = self._get(i, j, 2*node+1, mid, node_b)
        return self.operation(left, right)

    def __getitem__(self, pos):
        return self.tree[self.size + pos]

    def __setitem__(self, pos, val):
        self.tree[self.size + pos] = val

    def update(self, pos, new_value):
        pos += self.size
        while pos>0:
            self.tree[pos] = new_value
            pos //= 2
            new_value = self.operation(self.tree[pos*2], self.tree[pos*2+1])