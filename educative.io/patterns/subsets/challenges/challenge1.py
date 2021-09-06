'''
Evaluate Expression (hard) ##

Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.

Example 1:

Input: "1+2*3"
Output: 7, 9
Explanation: 1+(2*3) => 7 and (1+2)*3 => 9

Example 2:

Input: "2*3-4-5"
Output: 8, -12, 7, -7, -3 
Explanation: 2*(3-(4-5)) => 8, 2*(3-4-5) => -12, 2*3-(4-5) => 7, 2*(3-4)-5 => -7, (2*3)-4-5 => -3

Solution ##

This problem follows the Subsets pattern and can be mapped to Balanced Parentheses. We can follow a similar BFS approach.

Let’s take Example-1 mentioned above to generate different ways to evaluate the expression.

    We can iterate through the expression character-by-character.
    we can break the expression into two halves whenever we get an operator (+, -, *).
    The two parts can be calculated by recursively calling the function.
    Once we have the evaluation results from the left and right halves, we can combine them to produce all results.

'''
def diff_ways_to_evaluate_expression(input):
  result = []
  # base case: if the input string is a number, parse and add it to output.
  if '+' not in input and '-' not in input and '*' not in input:
    result.append(int(input))
  else:
    for i in range(0, len(input)):
      char = input[i]
      if not char.isdigit():
        # break the equation here into two parts and make recursively calls
        leftParts = diff_ways_to_evaluate_expression(input[0:i])
        rightParts = diff_ways_to_evaluate_expression(input[i+1:])
        for part1 in leftParts:
          for part2 in rightParts:
            if char == '+':
              result.append(part1 + part2)
            elif char == '-':
              result.append(part1 - part2)
            elif char == '*':
              result.append(part1 * part2)

  return result


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
'''
Time complexity ##

The time complexity of this algorithm will be exponential and will be similar to Balanced Parentheses. Estimated time complexity will be O(N∗2N)O(N*2^N)O(N∗2​N​​) but the actual time complexity ( O(4n/n)O(4^n/\sqrt{n})O(4​n​​/√​n​​​) ) is bounded by the Catalan number and is beyond the scope of a coding interview. See more details here.
Space complexity ##

The space complexity of this algorithm will also be exponential, estimated at O(2N)O(2^N)O(2​N​​) though the actual will be ( O(4n/n).O(4^n/\sqrt{n}).O(4​n​​/√​n​​​).
Memoized version ##

The problem has overlapping subproblems, as our recursive calls can be evaluating the same sub-expression multiple times. To resolve this, we can use memoization and store the intermediate results in a HashMap. In each function call, we can check our map to see if we have already evaluated this sub-expression before. Here is the memoized version of our algorithm; please see highlighted changes:

'''
def diff_ways_to_evaluate_expression(input):#This
  return diff_ways_to_evaluate_expression_rec({}, input)#This


def diff_ways_to_evaluate_expression_rec(map, input):
  if input in map:#This
    return map[input]#This

  result = []
  # base case: if the input string is a number, parse and return it.
  if '+' not in input and '-' not in input and '*' not in input:
    result.append(int(input))
  else:
    for i in range(0, len(input)):
      char = input[i]
      if not char.isdigit():
        # break the equation here into two parts and make recursively calls
        leftParts = diff_ways_to_evaluate_expression_rec(
          map, input[0:i])
        rightParts = diff_ways_to_evaluate_expression_rec(
          map, input[i+1:])
        for part1 in leftParts:
          for part2 in rightParts:
            if char == '+':
              result.append(part1 + part2)
            elif char == '-':
              result.append(part1 - part2)
            elif char == '*':
              result.append(part1 * part2)

  map[input] = result #This
  return result


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
