class HashMap:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    hm = HashMap()
    hm['Item 1'] = 'Hello'
    hm['item 2'] = 'What up'
    print(hm['item 2'])
    print(hm['Item 1'])
    del hm['item 2']
    print(hm.arr)