'''
LIFO
Can only remove from, add to or read from the top
Absract Data Type - it’s a kind of data type that is based on a set of theoretical rules that revolve around some other
built-in data structure.
Applications: Linter(maybe for brackets), Undo and Redo(Ctrl + Z),
'''
from queue import Queue
class Stack:
    #All O(1) operations
    def __init__(self) -> None:
        self.stack_list = []
        self.stack_size = 0
    def isEmpty(self):
        return self.stack_size == 0
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack_list[-1]
    def push(self, element):
        self.stack_list.append(element)
        self.stack_size += 1
    def pop(self):
        self.stack_size -= 1
        return self.stack_list.pop()
    def size(self):
        return self.stack_size
    

class TwoStacks:
    # 2 stacks with a single list. All O(1)
    # constructor
    def __init__(self, n):  
        self.size = n
        # populating 0s on all n indices of array arr
        self.arr = [0] * n  
        self.top1 = -1
        self.top2 = self.size

    # Method to push an element x to stack1
    def push1(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow ")
            exit(1)

    # Method to push an element x to stack2
    def push2(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x

        else:
            print("Stack Overflow ")
            exit(1)

    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

    # Method to pop an element from second stack
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print("Stack Underflow ")
            exit()

# Reverse first k elements of a queue
def reverseK(queue, k):
    if k > queue.size() or k < 0:
        return
    if queue.is_empty():
        return

    stack = Stack()
    new_queue = Queue()
    for _ in range(k):
        stack.push(queue.dequeue())

    while not stack.is_empty():
        new_queue.enqueue(stack.pop())

    while not queue.is_empty():
        new_queue.enqueue(queue.dequeue())
    
    return new_queue

class QueueUsingStacks:
    def __init__(self) -> None:
        self.stack_1 = Stack()
        self.stack_2 = Stack()
    def enqueue(self, element):
        self.stack_1.push(element)
    def dequeue(self):
        if self.stack_2.isEmpty():
            while not self.stack_1.isEmpty():
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()

def sort_stack(stack):
    # Sort recursively
    if (not stack.is_empty()):
        # Pop the top element off the stack
        value = stack.pop()
        # Sort the remaining stack recursively
        sort_stack(stack)
        # Push the top element back into the sorted stack 
        insert(stack, value) 
 
def insert(stack, value):
    # Insertion helper
    if (stack.is_empty() or value < stack.peek()):
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)

# Alternatively,
"""
1. Use a second temp_stack.
2. Pop value from mainStack.
3. If the value is greater or equal to the top of temp_stack,
  then push the value in temp_stack
  else pop all values from temp_stack
      and push them in mainStack
      and in the end push value in temp_stack
4.repeat from step 2 till mainStack is not empty.
5. When mainStack will be empty,
    temp_stack will have sorted values in descending order.
6. Now transfer values from temp_stack to mainStack
    to make values sorted in ascending order.
"""
def sort_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        value = stack.pop()
        # if value is not none and larger, push it at the top of temp_stack
        if temp_stack.peek() is not None and value >= temp_stack.peek():
            temp_stack.push(value)
        else:
            while not temp_stack.is_empty():
                stack.push(temp_stack.pop())
            # place value as the smallest element in temp_stack
            temp_stack.push(value)
    # Transfer from temp_stack => stack
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    return stack


def evaluate_post_fix(exp):
    stack = Stack()
    operations = '+-*/'

    for char in exp:
        if char == ' ':
            continue
        if char in operations:
            second, first = stack.pop(), stack.pop()
            stack.push(str(eval(first+char+second)))
        else:
            stack.push(char)

    return int(float(stack.pop()))

def next_greater_element(lst):
    stack = Stack()
    res = [-1] * len(lst)
    # Reverse iterate list
    for i in range(len(lst) - 1, -1, -1):
        ''' While stack has elements and current element is greater 
        than top element, pop all elements '''
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()
        ''' If stack has an element, top element will be 
        greater than ith element '''
        if not stack.is_empty():
            res[i] = stack.peek()
        # push in the current element in stack
        stack.push(lst[i])
    for i in range(len(lst)):
        print(str(lst[i]) + " -- " + str(res[i]))
    return res

''' Iterate through the string exp.
For each opening parentheses, push it into stack
For every closing parentheses check
for its opening parentheses in stack
If you can't find the opening parentheses
for any closing one then returns false.
and after complete traversal of string exp,
if there's any opening parentheses left
in stack then also return false.
At the end return true if you haven't
encountered any of the above false conditions '''

def is_balanced(exp):
    closing = ['}', ')', ']']
    stack = Stack()
    for character in exp:
        if character in closing:
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if character is '}' and top_element is not '{':
                return False
            if character is ')' and top_element is not '(':
                return False
            if character is ']' and top_element is not '[':
                return False
        else:
            stack.push(character)
    if not stack.is_empty():
        return False
    return True