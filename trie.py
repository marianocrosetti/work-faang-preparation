

class Trie:
    def __init__(self):
        self.children = dict()
        self.end_of_string = False
    
    def insert(self, s, deep=0):
        if deep == len(s):
            self.end_of_string = True
            return
        c = s[deep]
        if c not in self.children:
            new_trie = Trie()
            self.children[c] = new_trie
        self.children[c].insert(s,deep+1)
    
    def show(self, deep=0):
        if not deep:
            print('(root)')
        for c in self.children:
            print( ('    '*(deep+1)) + c + ' ' + ('(*)' if self.children[c].end_of_string else ''))
            self.children[c].show(deep+1)

root = Trie()
root.insert('cat')
root.insert('car')
root.insert('care')
root.show()

    