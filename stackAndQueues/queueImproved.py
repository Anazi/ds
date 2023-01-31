class Queue:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = list()
        else:
            self.elements = elements

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        if len(self.elements) > 0:
            return self.elements.pop(0)

    def get_first(self):
        if len(self.elements) > 0:
            return self.elements[0]

    def peek(self):
        """Show last element"""
        if len(self.elements) > 0:
            return self.elements[-1]

    def get_size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def __str__(self):
        return str(self.elements)


class Stack:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = list()
        else:
            self.elements = elements

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop()

    def peek(self):
        """Show last element"""
        if len(self.elements) > 0:
            return self.elements[-1]

    def __str__(self):
        return str(self.elements)


ss = Stack()
ss.push(1)
# ss.push(2)
# ss.push(3)
# ss.push(4)
print(ss)
print(ss.pop())
print(ss)
print(ss.peek(), 'peek')
print(ss)
