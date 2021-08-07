'''
FIFO
Data can only be removed from the front, added to end, read from the front
Absract Data Type - it’s a kind of data type that is based on a set of theoretical rules that revolve around some other
built-in data structure.
Applications: Several real world scenarios, We want to prioritize something over another, A resource is shared between multiple devices

Listed below are the four most common types of queues.

    Linear Queue
    Circular Queue
    Priority Queue --> In priority queues, all elements have a priority associated with them and are sorted such that the most prioritized object appears at the front and the least prioritized object appears at the end of the queue. These queues are widely used in most operating systems to determine which programs should be given more priority.
    Double-ended Queue --> The double-ended queue acts as a queue from both ends(back and front). It is a flexible data structure that provides enqueue and dequeue functionality on both ends in O(1). Hence, it can act like a normal linear queue if needed. Python has a built-in deque class that can be imported from the collections module. The class contains several useful methods such as rotate

'''

class Queue:
    def __init__(self) -> None:
        self.queue_list = []
        self.queue_size = 0
    def isEmpty(self):
        return self.queue_size == 0
    def front(self):
        if self.isEmpty():
            return None
        return self.queue_list[0]
    def rear(self):
        if self.isEmpty():
            return None
        return self.queue_list[-1]
    def size(self):
        return self.queue_size
    def enqueue(self, element):
        self.queue_size += 1
        self.queue_list.append(element)
    def dequeue(self):
        if self.isEmpty():
            return None
        front = self.front()
        self.queue_list.remove(self.front())
        self.queue_size -= 1
        return front
        # Alternatively, just return self.queue_list.pop(0)

def convert(n):
    st = ""
    if n == 0 or n == 1:
        st += str(n)
        return st
    if n % 2 == 0:
        st += "0"
    else:
        st += "1"
    return convert(n // 2) + st
def find_bin(n):
    out = []
    for i in range(1, n + 1):
        out.append(convert(i))
    return out

#Educative soln
def find_bin(number):
    result = []
    queue = Queue()
    queue.enqueue(1)
    for i in range(number):
        result.append(str(queue.dequeue()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)

    return result  # For number = 3 , result = {"1","10","11"}
'''
Start with Enqueuing 1. Dequeue a number from the queue, append 0 to it, 
and enqueue it back to queue. Perform the second step, 
but with appending 1 to the original number and enqueue back to the queue. 
The size of Queue should be 1 more than the number because, for a single number,
we’re enqueuing two variations of it, one with appended 0 while the other with 1 being appended.
'''
print(find_bin(5))

