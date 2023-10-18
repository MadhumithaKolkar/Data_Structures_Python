class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        iteration = self.head
        llist = ''
        while(iteration):
            llist += str(iteration.data) + '--> ' if iteration.next else str(iteration.data)
            iteration = iteration.next
        print(llist)

    def get_length(self):
        iteration = self.head
        count = 0
        while(iteration):
            count +=1
            iteration = iteration.next

        return count

    def insert_at_start(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        iteration = self.head
        while iteration.next:
            iteration = iteration.next

        iteration.next = Node(data, None)

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_start(data)
            return

        iteration = self.head
        count = 0
        while(iteration):
            if count == index-1:
                iteration.next = Node(data, iteration.next)
                break

            count += 1
            iteration = iteration.next

    def remove_at(self, index):
        if index<0 or index>self.get_length():
            raise Exception("Index Invalid")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        iteration = self.head
        while iteration:
            if count == index-1:
                iteration.next = iteration.next.next
                break

            count += 1
            iteration = iteration.next

    def add_list(self,data_list):
        for values in data_list:
            self.insert_at_end(values)

    def clear(self):
        self.head = None
        return

if __name__ == '__main__':
    ll = Linked_List()
    ll.add_list(['Hello','What','are','you','1'])
    ll.print()
    ll.insert_at(2,'Bug')
    ll.print()
    ll.remove_at(3)
    ll.print()
    len = ll.get_length()
    print('Length of Linked_list '+str(len))

    ll.add_list(['1','2','3','4'])
    ll.print()
    ll.insert_at_end(99)
    ll.print()
    ll.clear()
    ll.print()
