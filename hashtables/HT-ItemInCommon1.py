def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


list1 = [1,3,5]
list2 = [2,3,6]

# print(item_in_common(list1, list2))


def comm(l1, l2):
    d1 = {}
    for i in l1:
        d1[i] = True
    for i in l2:
        if i in d1.keys():
            return True
    return False


print(comm(list1, list2))
