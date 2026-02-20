class UnionFind:
    def __init__(self, size):
        self.size = size
        self.parent = [None for _ in range(size)]
    
    def component_id(self, i):
        if self.parent[i] is None:
            return i
        self.parent[i] = self.component_id(self.parent[i])
        return self.parent[i]
    
    def join(self, i, j):
        i_id = self.component_id(i)
        j_id = self.component_id(j)
        are_connected = i_id == j_id
        if not are_connected:
            self.parent[i_id] = j_id
    
    def are_connected(self, i, j):
        return self.component_id(i) == self.component_id(j)