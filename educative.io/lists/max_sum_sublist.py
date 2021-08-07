def find_max_sum_sublist(lst):
    max_so_far = float("-inf")
    max_ending_here = 0
    size = len(lst)
    for i in range(0, size):
        max_ending_here = max_ending_here + lst[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0
        print(max_ending_here)
    return max_so_far
print(find_max_sum_sublist([-2,10,7,-5,15,6]))