class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash_val(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_values(self, key, value):
        index = self.__hash_val(key)

        if self.data_map[index] is None:
            self.data_map[index] = []

        if len(self.data_map[index]) > 0:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    self.data_map[index][i][1] = value
                    return
        self.data_map[index].append([key, value])
        print(self.data_map)

    def keys(self):
        res = []
        for i in range(len(self.data_map)):
            print(i, self.data_map[i], 'iiiii')
            if self.data_map[i] is None:
                continue
            for j in range(len(self.data_map[i])):
                key = self.data_map[i][j][0]
                res.append(key)
        return res


my_hash_table = HashTable()

my_hash_table.set_values('bolts', 1400)
my_hash_table.set_values('bolts', 2000)
my_hash_table.set_values('washers', 50)
my_hash_table.set_values('lumber', 70)
my_hash_table.set_values('washer', 70)

# print(my_hash_table.get_item("washers"))
# print(my_hash_table.get_all_keys())
# print(my_hash_table.delete_item('lumber'))
print(my_hash_table.keys())











