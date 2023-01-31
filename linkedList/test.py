class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append_list(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def reverse_ll(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after







my_linked_list = LinkedList(1)
my_linked_list.append_list(2)
my_linked_list.append_list(3)
my_linked_list.append_list(4)
my_linked_list.prepend(5)

my_linked_list.print_list()
print('-------------------')
my_linked_list.reverse_ll()
#
my_linked_list.print_list()


"""
new head -- (5 -> 1)
(1(value) -> 2)
2
3
tail -- (4 -> None)


new_node.next = self.head
self.head = new_node


temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
"""