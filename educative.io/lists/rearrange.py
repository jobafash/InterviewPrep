def rearrange(lst):
    # Write your code here
    op = []
    for ele in lst:
        if ele < 0:
            op.insert(0,ele)
        else:
            op.append(ele)
    return op
print(rearrange([10,-1,20,4,5,-9,-6]))

#From educative
# def rearrange(lst):
#     # get negative and positive list after filter and then merge
#     return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


# print(rearrange([10, -1, 20, 4, 5, -9, -6]))
