'''
Base case
Recursive call
Break down before/within recursive call
If it's not up to base case, break it down and call it again, rinse and repeat
Implementations: Factorial, traversing a filesystem
'''

'''
Recursive Category 1: Repeatedly Execute A Task
For problems of this category, the last line of code in the function
is a simple, single call to the function again e.g count() as shown below
Extra params

'''
# Trick 1: For loops, we use an index to track eles, in recursion, we use 
# an extra parameter. The “trick” of using extra function parameters is a common technique in
# writing recursive functions, and a handy one. 

def count(num):
    if num < 0:
        return
    print(num)
    return count(num - 1)
#count(10)

def double_array(arr, index=0):
    if index == len(arr):
        return
    arr[index] *= 2
    double_array(arr, index + 1)
    return arr
print(double_array([1,2,3,4]))

'''Recursive Category 2: Calculations
Performing a calculation based on a subproblem

A second area in which recursion shines is where
it is able to make a calculation based on a subproblem of the problem at hand.

when writing a function that makes a calculation, there are
two potential approaches: we can try to build the solution from the “bottom
up,” or we can attack the problem going “top down” by making the calculation
based on the problem’s subproblem. that’s what is so great about top-down thinking: in
a way, we can solve the problem without even knowing how to solve the
problem

1. Imagine the function you’re writing has already been implemented by
someone else.
2. Identify the subproblem of the problem.
3. See what happens when you call the function on the subproblem and go
from there.
'''

# def fac(n):
#     produ = 1
#     for i in range(1, n + 1):
#         produ *= i
#     return produ
# print(fac(6))


#Staircase problem
def staircase(n):
    if n < 0: return 0
    if n == 1 or n == 0: return 1
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
print(staircase(5))

# Anagram permutation