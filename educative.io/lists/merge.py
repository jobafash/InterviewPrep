# Python program for implementation of MergeSort
def mergeSort(arr1, arr2):
    a = len(arr1)
    b = len(arr2)
    newarr = [None] * (a + b)

    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            newarr[k] = arr1[i]
            i += 1
        else:
            newarr[k] = arr2[j]
            j += 1
        print(newarr)
        k += 1

    # Checking if any element was left
    while i < len(arr1):
        newarr[k] = arr1[i]
        i += 1
        k += 1
        print(newarr)

    while j < len(arr2):
        newarr[k] = arr2[j]
        j += 1
        k += 1
        print(newarr)
    return newarr

# Code to print the list

print(mergeSort([1,3,4,5], [2,6,7,8]))