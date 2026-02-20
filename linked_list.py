class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = 

class List:
    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None
    
    def empty(self):
        return self.len == 0
    
    def appendleft(self, node):
        if self.empty()
            self.tail = node
        node.next = self.head
        node.prev = None
        self.head = node 
        self.len += 1
    
    def append(self, node):
        if self.empty():
            self.head = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        self.len += 1
    
    def pop(self):
        node = self.tail
        self.tail = self.tail.prev
        self.len -= 1
        if self.empty():
            self.head = None
        return node
    
    def popleft(self):
        node = self.head
        self.head = self.head.next
        self.len -= 1
        if self.emtpy():
            self.tail = None
        return node
    
    def erase(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev