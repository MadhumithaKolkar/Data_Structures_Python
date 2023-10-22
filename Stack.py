from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        if len(self.container) == 0:
            return True

    def length_of(self):
        return len(self.container)


if __name__ == '__main__':
    stack_object = Stack()
    stack_object.push(5)
    print(stack_object.is_empty())
    stack_object.push(9)
    print(stack_object)
    print(stack_object.pop())
    print(stack_object.pop())
    print(stack_object.is_empty())
