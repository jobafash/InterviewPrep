def find_min(list):
    smallest = list[0]

    for ele in list:
        if ele < smallest:
            smallest = ele
    return smallest
print(find_min([1,100000,-10000,4,-1])) 