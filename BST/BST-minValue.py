class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        # If tree is empty
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            # If new_node already exists
            if new_node.value == temp.value:
                return False
            # Checking the left and right of temp node
            if new_node.value < temp.value:
                # If temp.left already has a value, then temp will move to temp.left
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def contains(self, value):
        temp = self.root
        # Traverse through the tree and keep changing the temp until the item is found or
        #   the temp is None(item is not available in the tree)
        while temp is not None:
            # If value is smaller the temp.left, move temp to temp.left
            if value < temp.value:
                temp = temp.left
            elif value > temp.right:
                temp = temp.right
            else:
                return True
        return False

    @staticmethod
    def min_value_node_by_given_node(current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

# print(my_tree.contains(27), '\n')
#
# print(my_tree.contains(17), '\n')


print(my_tree.min_value_node_by_given_node(
    my_tree.root.right
), " - min value to the right", "\n")

print(my_tree.min_value_node_by_given_node(
    my_tree.root
), " - min value from the Root", "\n")
