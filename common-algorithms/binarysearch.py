
def binarysearch(list, item):
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = (low+high)//2
        if list[mid] == item:
            return mid
        if list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
print(binarysearch([1,2,3,4,6,8], 6))