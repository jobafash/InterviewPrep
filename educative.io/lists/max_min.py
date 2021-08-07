def max_min(lst):
    new_arr = []
    while lst != [] and len(lst) > 1:
        new_arr.append(max(lst))
        new_arr.append(min(lst))
        lst.pop()
        lst.pop(0)
    new_arr += lst
    return new_arr
print(max_min([1,2,3,4,5,6,7]))

#Educative.io
# def max_min(lst):
#     result = []
#     # iterate half list
#     for i in range(len(lst)//2):
#         # Append corresponding last element
#         result.append(lst[-(i+1)])
#         # append current element
#         result.append(lst[i])
#     if len(lst) % 2 == 1:
#         # if middle value then append
#         result.append(lst[len(lst)//2])
#     return result


# print(max_min([1, 2, 3, 4, 5, 6]))

#Alternatively, 
#Note: This approach only works for non-negative numbers!
# def max_min(lst):
#     # Return empty list for empty list
#     if (len(lst) is 0):
#         return []

#     maxIdx = len(lst) - 1  # max index
#     minIdx = 0  # first index
#     maxElem = lst[-1] + 1  # Max element
#     # traverse the list
#     for i in range(len(lst)):
#         # even number means max element to append
#         if i % 2 == 0:
#             lst[i] += (lst[maxIdx] % maxElem) * maxElem
#             maxIdx -= 1
#         # odd number means min number
#         else:
#             lst[i] += (lst[minIdx] % maxElem) * maxElem
#             minIdx += 1
#     print(lst)
#     for i in range(len(lst)):
#         lst[i] = lst[i] // maxElem
#     return lst


# print(max_min([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
