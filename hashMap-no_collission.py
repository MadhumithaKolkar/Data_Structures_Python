class HashMap:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element == 2) and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                self.arr[h].remove(element)

if __name__ == '__main__':
    hm = HashMap()
    hm['Tony'] = 'Guy'
    hm['march 6'] = 99
    hm['march 17'] = 258
    print(hm.arr)
    print(hm['march 6'])
    print(hm['march 17'])
    del hm['march 6']
    print(hm.arr)
    print(hm['march 6'])
    del hm['Tony']
    print(hm.arr)
    print(hm['march 17'])
    print(hm['Tony'])