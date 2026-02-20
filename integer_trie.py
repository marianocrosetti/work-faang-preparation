import math
from collections import defaultdict

class IntegerTrie:
    def __init__(self, bit_length, offset):
        self.children = defaultdict(lambda : IntegerTrie(bit_length, offset))
        self.bit_length = bit_length
        self.offset = offset
        self._reset_internals()
    
    def _reset_internals(self):
        self.count = 0
        self.max = - math.inf
        self.min = math.inf
        for b in self.children:
            self.max = max(self.max, self.children[b].max)
            self.min = min(self.min, self.children[b].min)
            self.count += self.children[b].count 
    
    def add(self,x):
        #print('add', x)
        self._add(x + self.offset,self.bit_length-1)
    
    def _add(self, x, bit_idx):
        self.count += 1
        self.max = max(self.max, x)
        self.min = min(self.min, x)
        if bit_idx < 0:
            return
        current_bit = (x >> bit_idx) & 1
        self.children[current_bit]._add(x, bit_idx-1)
    
    def bisect_left(self, x):
        ans = self._bisect(x + self.offset, side_left=True, bit_idx=self.bit_length-1)
        return ans
    
    def bisect_right(self, x):
        ans = self._bisect(x + self.offset, side_left=False, bit_idx=self.bit_length-1)
        return ans
    
    def _bisect(self, x, side_left, bit_idx):
        if bit_idx < 0:
            return 0 if side_left else self.count 
        current_bit = (x >> bit_idx) & 1
        count = 0
        if current_bit:
            if 0 in self.children:
                count += self.children[0].count
            if 1 in self.children:
                count += self.children[1]._bisect(x, side_left, bit_idx-1)
        else:
            if 0 in self.children:
                count += self.children[0]._bisect(x, side_left, bit_idx-1)
        return count

    def erase(self,x):
        self._erase(x + self.offset ,self.bit_length-1)
    
    def _erase(self, x, bit_idx):
        if bit_idx < 0:
            self.count -= 1
            return
        current_bit = (x >> bit_idx) & 1
        if current_bit in self.children:
            self.children[current_bit]._erase(x, bit_idx-1)
            if not self.children[current_bit].count:
                del self.children[current_bit]
            self._reset_internals()

if __name__ == "__main__"
    t = IntegerTrie(4)
    # 1 1 1 2 2 2 3 3  
    # 0 1 2 3 4 5 6 7
    t.add(1)
    t.add(1)
    t.add(1)
    t.add(2)
    t.add(2)
    t.add(2)
    t.add(3)
    t.add(3)
    print(f"{t.bisect_left(0)=}")
    print(f"{t.bisect_right(0)=}")
    print(f"{t.bisect_left(1)=}")
    print(f"{t.bisect_right(1)=}")
    print(f"{t.bisect_left(2)=}")
    print(f"{t.bisect_right(2)=}")
    print(f"{t.bisect_left(3)=}")
    print(f"{t.bisect_right(3)=}")
    print(f"{t.bisect_left(4)=}")
    print(f"{t.bisect_right(4)=}")
    print("\n\n")
    # 1 1 2  
    # 0 1 2
    t.erase(1)
    t.erase(2)
    t.erase(2)
    t.erase(3)
    t.erase(3)
    t.erase(3)
    print(f"{t.bisect_left(0)=}")
    print(f"{t.bisect_right(0)=}")
    print(f"{t.bisect_left(1)=}")
    print(f"{t.bisect_right(1)=}")
    print(f"{t.bisect_left(2)=}")
    print(f"{t.bisect_right(2)=}")
    print(f"{t.bisect_left(3)=}")
    print(f"{t.bisect_right(3)=}")
    print(f"{t.bisect_left(4)=}")
    print(f"{t.bisect_right(4)=}")