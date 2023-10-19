class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
         h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        value = self.get_hash(key)
        return self.arr[value]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__=="__main__":
    hm = HashTable()
    print(hm.get_hash('march 6'))
    hm['Apr'] = 964
    hm['July 6'] = 'Hello'
    hm['Dog'] = 'Cat'
    print(hm.arr)
    print(hm['Apr'])
    print(hm['Dog'])
    del hm['Dog']
    print(hm.arr)
    print(hm['Dog'])