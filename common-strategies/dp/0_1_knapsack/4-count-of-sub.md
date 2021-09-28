Problem Statement#

Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
Example 1:#

Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.

Example 2:#

Input: {1, 2, 7, 1, 5}, S=9
Output: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

Basic Solution#

This problem follows the 0/1 Knapsack pattern and is quite similar to Subset Sum. The only difference in this problem is that we need to count the number of subsets, whereas in the Subset Sum we only wanted to know if there exists a subset with the given sum.

A basic brute-force solution could be to try all subsets of the given numbers to count the subsets that have a sum equal to ‘S’. So our brute-force algorithm will look like:

```py
for each number 'i'
  create a new set which includes number 'i' if it does not exceed 'S', and recursively
      process the remaining numbers and sum
  create a new set without number 'i', and recursively process the remaining numbers
return the count of subsets who has a sum equal to 'S'
```

```py
def count_subsets(num, target_sum):
  return count_subsets_recursive(num, target_sum, 0)


def count_subsets_recursive(num, target_sum, currentIndex):
  # base checks
  if target_sum == 0:
    return 1
  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0

  # recursive call after selecting the number at the currentIndex
  # if the number at currentIndex exceeds the target_sum, we shouldn't process this
  sum1 = 0
  if num[currentIndex] <= target_sum:
    sum1 = count_subsets_recursive(
      num, target_sum - num[currentIndex], currentIndex + 1)

  # recursive call after excluding the number at the currentIndex
  sum2 = count_subsets_recursive(num, target_sum, currentIndex + 1)

  return sum1 + sum2


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
```

The time complexity of the above algorithm is exponential O(2n)O(2^n)O(2​n​​), where ‘n’ represents the total number. The space complexity is O(n)O(n)O(n), this memory is used to store the recursion stack.
Top-down Dynamic Programming with Memoization#

We can use memoization to overcome the overlapping sub-problems. We will be using a two-dimensional array to store the results of solved sub-problems. As mentioned above, we need to store results for every subset and for every possible sum.
Code#

Here is the code:

```py
def count_subsets(num, target_sum):
  # create a two dimensional array for Memoization, each element is initialized to '-1'
  dp = [[-1 for x in range(target_sum+1)] for y in range(len(num))]
  return count_subsets_recursive(dp, num, target_sum, 0)


def count_subsets_recursive(dp, num, target_sum, current_index):
  # base checks
  if target_sum == 0:
    return 1

  n = len(num)
  if n == 0 or current_index >= n:
    return 0

  # check if we have not already processed a similar problem
  if dp[current_index][target_sum] == -1:
    # recursive call after choosing the number at the current_index
    # if the number at current_index exceeds the sum, we shouldn't process this
    sum1 = 0
    if num[current_index] <= target_sum:
      sum1 = count_subsets_recursive(
        dp, num, target_sum - num[current_index], current_index + 1)

    # recursive call after excluding the number at the current_index
    sum2 = count_subsets_recursive(dp, num, target_sum, current_index + 1)

    dp[current_index][target_sum] = sum1 + sum2

  return dp[current_index][target_sum]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
```

Bottom-up Dynamic Programming#

We will try to find if we can make all possible sums with every subset to populate the array db[TotalNumbers][s+1].

So, at every step we have two options:

    Exclude the number. Count all the subsets without the given number up to the given sum => dp[index-1][sum]
    Include the number if its value is not more than the ‘sum’. In this case, we will count all the subsets to get the remaining sum => dp[index-1][sum-num[index]]

To find the total sets, we will add both of the above two values:

    dp[index][sum] = dp[index-1][sum] + dp[index-1][sum-num[index]])

Let’s start with our base case of size zero:

```py
def count_subsets(num, target_sum):
  n = len(num)
  dp = [[-1 for x in range(target_sum+1)] for y in range(n)]

  # populate the sum = 0 columns, as we will always have an empty set for zero sum
  for i in range(0, n):
    dp[i][0] = 1

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for s in range(1, target_sum+1):
    dp[0][s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(1, target_sum+1):
      # exclude the number
      dp[i][s] = dp[i - 1][s]
      # include the number, if it does not exceed the sum
      if s >= num[i]:
        dp[i][s] += dp[i - 1][s - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][target_sum]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
```

The above solution has time and space complexity of O(N∗S)O(N\*S)O(N∗S), where ‘N’ represents total numbers and ‘S’ is the desired sum.
Challenge#

Can we further improve our bottom-up DP solution? Can you find an algorithm that has O(S)O(S)O(S) space complexity?

```py
def count_subsets(num, sum):
  n = len(num)
  dp = [0 for x in range(sum+1)]
  dp[0] = 1

  # with only one number, we can form a subset only when the required sum is equal to the number
  for s in range(1, sum+1):
    dp[s] = 1 if num[0] == s else 0

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(sum, -1, -1):
      if s >= num[i]:
        dp[s] += dp[s - num[i]]

  return dp[sum]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
```
