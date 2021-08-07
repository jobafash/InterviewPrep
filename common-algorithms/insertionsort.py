def insertionsort(A):
    for i in range(1, len(A)):
        #Each iteration, from second element
        temp = A[i]
        position = i - 1
        while position >= 0:
            #Keep comparing the elements before temp 
            # and swap where  necessary
            if A[position] > temp:
                A[position + 1] = A[position]
                position -= 1
            else:
                break
        A[position + 1] = temp
    return A
print(insertionsort([4,2,7,1,3]))