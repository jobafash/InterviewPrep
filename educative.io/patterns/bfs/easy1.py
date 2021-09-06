'''
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Example 1:


Solution#

Since we need to traverse all nodes of each level before moving onto the next level, we can use the Breadth First Search (BFS) technique to solve this problem.

We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:

    Start by pushing the root node to the queue.
    Keep iterating until the queue is empty.
    In each iteration, first count the elements in the queue (let’s call it levelSize). We will have these many nodes in the current level.
    Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
    After removing each node from the queue, insert both of its children into the queue.
    If the queue is not empty, repeat from step 3 for the next level.

'''
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    currentLevel = []
    for _ in range(levelSize):
      currentNode = queue.popleft()
      # add the node to the current level
      currentLevel.append(currentNode.val)
      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    result.append(currentLevel)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
#Level order traversal: [[12], [7, 1], [9, 10, 5]]

'''
Time complexity#

The time complexity of the above algorithm is O(N)O(N)O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.
Space complexity#

The space complexity of the above algorithm will be O(N)O(N)O(N) as we need to return a list containing the level order traversal. We will also need O(N)O(N)O(N) space for the queue. Since we can have a maximum of N/2N/2N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N)O(N)O(N) space to store them in the queue.

'''