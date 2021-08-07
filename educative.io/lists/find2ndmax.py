def find2ndmax(arr):
    maximum = arr[0]
    second_maximum = float("-inf")
    for i in range(1,len(arr)):
        if arr[i] > maximum:
            second_maximum = maximum
            maximum = arr[i]
        if arr[i] > second_maximum and arr[i] < maximum:
            second_maximum = arr[i]
    return None if second_maximum == float("-inf") else second_maximum

print(find2ndmax([1,2,4,4]))