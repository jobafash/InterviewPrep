#Sorting from the last index, so that after the nth iteration,
# n largest element(s) will be sorted from the end
def bubblesort(A):
    for i in range(len(A)):
        #Last element(s) is sorted
        for j in range(len(A) - i - 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

print(bubblesort([4,2,7,1,3]))
