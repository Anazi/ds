def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False


list1 = [1,3,5]
list2 = [2,1,6]


print(item_in_common(list1, list2))


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
        print(self.data_map, 'in the begining')

    def __hash(self, key):
        hash_val = 0
        for letter in key:
            hash_val = (hash_val + ord(letter) * 23) % len(self.data_map)
        return hash_val

    def set(self, key, val):
        # by hash val get index. Based on index, check with
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        print(self.data_map, 'when index is with []')
        # Simple approach
        # self.data_map[index].append([key, val])
        # Update the val in case if the key already exists
        if len(self.data_map[index]) > 0:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    self.data_map[index][i][1] = val
                    return
        self.data_map[index].append([key, val])
        print(self.data_map)

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return self.data_map[index][i][1]

    def delete_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return False
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                del self.data_map[index][i]
                return True

    def get_all_keys(self):
        # [ [[],[]], [[]] ]
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


my_hash_table = HashTable()

my_hash_table.set('bolts', 1400)
my_hash_table.set('bolts', 2000)
my_hash_table.set('washers', 50)
my_hash_table.set('lumber', 70)

print(my_hash_table.get_item("washers"))
print(my_hash_table.get_all_keys())
print(my_hash_table.delete_item('lumber'))
print(my_hash_table.get_all_keys())

# a = [[['a', 'b']], [['c', 'd'], ['e', 'f']]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j][0] == "e":
#             print('found')
#             del a[i][j]
#             print('found')
# print(a)