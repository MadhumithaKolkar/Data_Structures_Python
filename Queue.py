from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self,val):
        self.container.appendleft(val)

    def dequeue(self):
        if len(self.container)==0:
            print("Can't pop from an empty queue")
        else:
            return self.container.pop()

    def is_empty(self):
        return len(self.container) ==0

    def size(self):
        return len(self.container)

    def peek(self):
        return self.container[-1]

    def add_list(self,list):
        for ent in list:
            # self.container.appendleft(ent)
            self.enqueue(ent)

if __name__ == '__main__':
    q = Queue()
    q.enqueue({
        'Hey' : 1,
        "Bye" : 2
    })
    q.add_list([1,2,3,99999,{'Oops':'Is the best'}])
    q.enqueue(5)
    q.enqueue(6)
    print(q.size())
    print(q.container)
    q.enqueue(7)
    print(q.is_empty())
    print(q.container)
    print(q.peek())

