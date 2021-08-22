'''
Heaps are advanced data structures that are useful in applications such as sorting and implementing priority queues. 
They are regular binary trees with two special properties

'''

'''
Heaps must be Complete Binary Trees
Some Complete Binary Tree Properties:

    All leaves are either at depth ddd or depth d−1d-1d−1.
    The leaves at depth ddd are to the left of the leaves at depth d−1d-1d−1
    There is at most one node with just one child
    If the singular child exists, it is the left child of its parent
    If the singular child exists, it is the right most leaf at depth ddd.

The Heap Order Property #

The nodes must be ordered according to the Heap Order Property. The heap order property is different for the two heap structures that we are going to study in this chapter:

    Min Heap
    Max Heap

Min Heaps are built based upon the Min Heap property and Max Heaps are built based upon Max Heap Property. Let’s see how they are different.

Max Heap Property: #

All the parent node keys must be greater than or equal to their child node keys in max-heaps. So the root node will always contain the largest element in the Heap. If Node A has a child node B, then:

key(A)>=key(B)
Min Heap Property: #

In Min-Heaps, all the parent node keys are less than or equal to their child node keys. So the root node, in this case, will always contain the smallest element present in the Heap. If Node A has a child node B, then:

key(A)<=key(B)

Where are Heaps Used? #

The primary purpose of heaps is to return the smallest or largest element. This is because the time complexity of getting the minimum/maximum value from a min/max heap is O(1), i.e., constant time complexity. This way, algorithms that require retrieving the maximum/minimum value can be optimized. Heaps are also used to design Priority Queues. Some of the famous algorithms which are implemented using Heaps are Prim’s Algorithm, Dijkstra’s algorithm and the famous Heap Sort algorithm which is entirely based on the Heap data structure.

Heap Representation in Lists #

Heaps can be implemented using arrays or lists in python. The node values are stored such that all the parent nodes occur in the first half of the list (where index≤floor(n−12)index \leq floor(\frac{n-1}{2})index≤floor(​2​​n−1​​) where nnn is the last index) and the leaves exist in the rest. So the last parent will be at the floor(n−12)floor(\frac{n-1}{2})floor(​2​​n−1​​) index. The left child of the node at the kthkthkth index will be at the 2k+12k+12k+1 index and the right child will be at 2k+22k+22k+2. To put it simply, the index of each node is how much you’d count if you started from 0 at the root and went left to right level wise in a tree. See the figure below to see how nodes are mapped to a list:

As you can see, all the parent nodes are present in the first half of the list and the last parent appears at the floor(n/2th) position. In this case, ‘n’ is the last or largest index so

n=9

floor((9−1)/2)=floor(8/2)=floor(4)=4

So the last parent is at the 4th index, the key of which is 50. The children nodes appear on the second half. The following two properties also hold:

LeftChild=2k+1

RightChild=2k+2

Heaps are sometimes called Binary Heaps because they are in fact binary trees. Also, the Heap data structure is not the same as heap memory. Furthermore, it is commonly believed that the elements of Heaps are sorted. They are not at all sorted, in fact, the only key condition that a Heap follows is that the largest or smallest element is always placed at the top (parent node) depending on what type of Heap we are using (Min/Max).
'''

'''
Building a Max-Heap #

As mentioned in the previous lesson, max heaps follow the max heap property which means that the key at the parent node is always greater than the keys at the child nodes. Heaps can be implemented using lists or using node and tree classes. Although they are generally implemented using lists or arrays as that is the more space-efficient approach! To build a heap, start with an empty one and successively insert() all the elements.

Insertion in a Max-Heap #

Here is a high-level description of the algorithm to insert elements into a heap and maintain the heap property.

    Create a new child node at the end of the heap
    Place the new key at that node
    Then, restore the heap property by swapping parent and child values if the parent key is smaller than the child key. We call this ‘percolating up’.
    Continue to percolate up until the heap property is restored.

For a clearer picture, here’s a visual representation of inserting in a max heap,

Remove Maximum in a Max Heap #

Here is the algorithm that you will follow to make sure the heap property still holds after deleting the root element

    Delete the root node

    Move the key of last child node at the last level to the root

    Now compare the key with its children and if the key is smaller than the key at any of the child nodes, swap values. We call this ‘max heapifying.’

    Continue to max heapify until the heap property is restored.
'''

'''
Max-heap Implementation #

Let’s start with some function declarations for the heap class. The __percolateUp() function is meant to restore the heap property going up from a node to the root. The __maxHeapify() function restores the heap property starting from a given node down to the leaves. The two underscores before the __percolateUp() and __maxHeapify() functions imply that these functions should be treated as private functions although there is no actual way to enforce class function privacy in Python. You can still call these functions by prepending _className like so, heap._maxHeap__percolateUp(index).

'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None

    def __percolateUp(self, index):
        parent = (index-1)//2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.__percolateUp(parent)

    def __maxHeapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            tmp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = tmp
            self.__maxHeapify(largest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr)-1, -1, -1):
            self.__maxHeapify(i)


heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.getMax())

'''
Let’s derive a tight bound for the complexity of building a heap.

Notice that we start from the bottom of the heap, i.e., range(len(arr)-1,-1,-1) (line 54). The number of comparisons for a particular node at height hhh is O(h)O(h)O(h). Also, the number of nodes at height 000 is at most ⌈n2⌉\lceil \frac{n}{2}\rceil⌈​2​​n​​⌉, that at height 111 is ⌈n4⌉\lceil \frac{n}{4}\rceil⌈​4​​n​​⌉ and so on. In general, the number of nodes at height hhh is at most ⌈n2h+1⌉\lceil \frac{n}{2^{h+1}}\rceil⌈​2​h+1​​​​n​​⌉.

Thus, for a heap with nnn nodes, that has a height of log(n)log( n)log(n), the running time of bottom-up heap construction is:

'''

'''
Building a Min-Heap #

As mentioned in a previous lesson, Min Heaps follow the Min Heap property which means that the key at the parent node is always smaller than the keys at the child nodes. Heaps can be implemented using lists. Initially, elements are placed in nodes in the same order as they appear in the list. Then a function is called over the whole heap in a bottom-up manner that “Min Heapifies” or “percolates up” on this heap so that the heap property is restored. The “Min Heapify” function is bottom-up because it starts comparing and swapping parent-child key values from the last parent (at the n2\frac{n}{2}​2​​n​​and index).

For a visual demonstration of heap creation, check out the following illustration.

Insertion in Min Heap #

Here is a high-level description of the algorithm to insert elements into a heap and maintain the heap property:

    Create a new child node at the end of the heap
    Place the new key at that node (append it to the list or array)
    Percolate up until you reach the root node and the heap property is satisfied

Remove Minimum in Min Heap #

Here is the algorithm that you will follow to make sure the heap property still holds after deleting the root element

    Delete the root node

    Move the key of the last child node to root

    Perculate down: if the key is larger than the key at any of the child nodes, swap values

    Repeat until you reach the last node

'''
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    def getMin(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMin(self):
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__minHeapify(0)
            return min
        elif len(self.heap) == 1:
            min = self.heap[0]
            del self.heap[0]
            return min
        else:
            return None

    def __percolateUp(self, index):
        parent = (index-1)//2
        if index <= 0:
            return
        elif self.heap[parent] > self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.__percolateUp(parent)

    def __minHeapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest = left
        if len(self.heap) > right and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            tmp = self.heap[smallest]
            self.heap[smallest] = self.heap[index]
            self.heap[index] = tmp
            self.__minHeapify(smallest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr)-1, -1, -1):
            self.__minHeapify(i)


heap = MinHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.getMin())
print(heap.removeMin())
print(heap.getMin())
heap.insert(-100)
print(heap.getMin())

'''
Challenge 1
Implement a function convertMax(maxHeap) which will convert a binary Max-Heap into a binary Min-Heap. Where maxHeap is a list which is given in the maxHeap format, i.e, the parent is greater than its children.

Returns converted list in string format

Sample Input #

maxHeap = [9,4,7,1,-2,6,5]

Sample Output #

result = [-2,1,5,9,4,6,7]

Remember that we can consider the given maxHeap to be a regular list of elements and reorder it so that it represents a min heap accurately. We do exactly that in this solution. The convertMax() function restores the heap property on all the nodes from the lowest parent node by calling the minHeapify() function on each.
Time Complexity #

As discussed here, the time complexity of building a heap is O(n).
'''
def minHeapify(heap, index):
    left = index * 2 + 1
    right = (index * 2) + 2
    smallest = index
    # check if left child exists and is less than smallest
    if len(heap) > left and heap[smallest] > heap[left]:
        smallest = left
    # check if right child exists and is less than smallest
    if len(heap) > right and heap[smallest] > heap[right]:
        smallest = right
    # check if current index is not the smallest
    if smallest != index:
        # swap current index value with smallest
        tmp = heap[smallest]
        heap[smallest] = heap[index]
        heap[index] = tmp
        # minHeapify the new node
        minHeapify(heap, smallest)
    return heap


def convertMax(maxHeap):
    # iterate from middle to first element
    # middle to first indices contain all parent nodes
    for i in range((len(maxHeap))//2, -1, -1):
        # call minHeapify on all parent nodes
        maxHeap = minHeapify(maxHeap, i)
    return maxHeap


maxHeap = [9, 4, 7, 1, -2, 6, 5]
print(convertMax(maxHeap))

'''
Challenge 2

Implement a function findKSmallest(lst,k) that takes an unsorted integer list as input and returns the “k” smallest elements in the list using a Heap. The minHeap class that was written in a previous lesson is prepended to this exercise so feel free to use it! Have a look at the illustration given for a clearer picture of the problem.
Output #

Returns integer list that contains the first kkk smallest elements from the given list

Sample Input #

lst = [9,4,7,1,-2,6,5]
k = 3

Sample Output #

[-2,1,4]

Here, we create a new heap from the given list on line 15. Then, we removeMin() from the heap kkk times and save the result to the list kSmallest using list comprehension on line 12. We return kSmallest at the end.
Time Complexity #

The time complexity of creating a heap is O(n) and removing min is O(klogn). So the total time complexity is O(n+klogn) which is basically O(klogn).

Solution #2: Using Quickselect #

You can optimize this further by calling the Quick Select algorithm on the given list kkk times where the input to the algorithm goes from 1 till kkk. We have not presented the code here because it is not relevant to heaps, but we felt that the optimal solution should be mentioned.
Time Complexity #

The average-case complexity of quick select is O(n)O(n)O(n). So when called kkk times it will be in O(nk)−>O(n)O(nk) -> O(n)O(nk)−>O(n).
'''
from MinHeap import MinHeap


def findKSmallest(lst, k):
    heap = MinHeap()  # Create a minHeap
    # Populate the minHeap with lst elements
    heap.buildHeap(lst)
    # Create a list of k elements such that:
    # It contains the first k elements from
    # removeMin() function
    kSmallest = [heap.removeMin() for i in range(k)]
    return kSmallest


lst = [9, 4, 7, 1, -2, 6, 5]
k = 3
print(findKSmallest(lst, k))

'''
Challenge 3

Implement a function findKLargest(lst,k) that takes an unsorted integer list as input and returns the kkk largest elements in the list using a Max Heap. The maxHeap class that was written in a previous lesson is prepended in this exercise so feel free to use it! Have a look at the illustration given for a clearer picture of the problem. Implement a function findKlargest() which takes a list as input and finds the “k” largest elements in the list using a Max-Heap

Output: #

Returns integer list containing first k largest elements from my_list
Sample Input #

lst = [9,4,7,1,-2,6,5] 
k = 3

Sample Output #

[9,7,6]

Explanation #

As “k” is 3, so we need to find the top 3 maximum elements from the given list. 9 is the largest value in the list, while 7 is the second maximum, and 6 is the third max.


'''
'''
Solution #1: Creating a Max-Heap and removing max kkk times 

We first create a max-heap out of the given list by inserting the list elements into an empty heap on line 7. We then call removeMax() on the heap kkk times, save the output in a list, and return it.
Time Complexity #

The time complexity of creating a heap is O(n)O(n)O(n) and removing max is O(klogn)O(klogn)O(klogn). So the total time complexity is O(n+klogn)O(n + klogn)O(n+klogn) which is the same as O(klogn)O(klogn)O(klogn)

Solution #2: Using Quickselect #

You can optimize this further by calling the Quick Select algorithm on the given list kkk times where the input to the algorithm goes from nnn till n−kn-kn−k. We have not presented the code here because it is not relevant to heaps, but we felt that the optimal solution should be mentioned.
Time Complexity #

The average-case complexity of quick select is O(n)O(n)O(n). So when called kkk times it will be in O(nk)−>O(n)O(nk) -> O(n)O(nk)−>O(n).
'''

from MaxHeap import MaxHeap


def findKLargest(lst, k):
    heap = MaxHeap()  # Create a MaxHeap
    # Populate the MaxHeap with elements of lst
    heap.buildHeap(lst)
    # Create a list such that:
    # It has k elements where
    # the k elements are the first k
    # elements received from calling removeMax()
    kLargest = [heap.removeMax() for i in range(k)]
    return kLargest


lst = [9, 4, 7, 1, -2, 6, 5]
k = 3
print(findKLargest(lst, k))
