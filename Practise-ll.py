class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + '---> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llist)

    def get_size(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node
        return

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at_index(self, data, index):
        if index<0 or index>self.get_size():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_start(data)
            return
        itr = self.head
        count = 0
        while itr.next:
            if count == index-1:
                itr.next = Node(data,itr.next)
                return
            count +=1
            itr = itr.next

    def remove_at(self,index):
        if index<0 or index>self.get_size():
            raise Exception("Invalid Index")

        if index ==0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count +=1
            itr = itr.next

    def add_list(self, data):
        for i in data:
            self.insert_at_start(i)

    def clear(self):
        self.head = None
        return

    def insert_after(self, data, data1):
        if self.head is None:
            print("List is empty and this element can't be found")
            return
        itr = self.head
        while itr.next:
            if itr.data == data:
                itr.next = Node(data1,itr.next)
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_start(1)
    ll.print()
    ll.insert_at_start(2)
    ll.print()
    ll.insert_at_end(3)
    ll.print()
    ll.insert_after(2,4)
    ll.print()
    ll.insert_after(1,5)
    ll.print()
    print(ll.get_size())
    ll.remove_at(3)
    ll.print()
    ll.add_list([1,'Hippo','banana','nomnoms'])
    ll.print()
    ll.insert_after('banana','apple')
    ll.print()
    ll.clear()
    ll.print()

