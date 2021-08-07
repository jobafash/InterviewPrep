'''
Connected data(nodes) is dispersed throughout memory.
In a linked list, each node represents one item in the list. 

This is the key to the linked list: each node also comes with a little extra
information, namely, the memory address of the next node in the list.

This extra piece of data—this pointer to 
the next node’s memory address—is known as a link. 

A really important point emerges: when dealing with a linked list, we only
have immediate access to its first node. This is going to have serious ramifica-
tions as we’ll see shortly.
'''

#Working with LL - Create node, connect, update
class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        return self.head_node == None
    '''

    The three types of insertion strategies used in singly linked-lists are:

    Insertion at the head
    Insertion at the tail
    Insertion at the kth index

    '''
    def insert_at_head(self, data):
        # Create a new node containing your specified value
        temp_node = Node(data)
        temp_head = self.get_head()
        if not temp_head:
            self.head_node = temp_node
        # The new node points to the same node as the head
        temp_node.next_element = self.head_node
        self.head_node = temp_node  # Make the head point to the new node
        return
    
    #Inserting at the tail of a LL
    def insert_at_tail(lst, value):
        newest = Node(value)
        temp = lst.get_head()
        if temp is None:
            lst.head_node = newest
            return
        while temp.next_element is not None:
            temp = temp.next_element
        temp.next_element = newest
        return
    
    def insert_at_kth(lst, value, k):
        new_node = Node(value)
        temp = lst.get_head()
        if not temp:
            lst.head_node = new_node
        k -= 1
        while k > 1 and temp.next_element:
            temp = temp.next_element
            k -= 1
        temp.next_element = new_node
        new_node.next_element = temp.next_element.next_element
        return
    
    def search(lst, value):
        temp = lst.get_head()
        if not temp: return False
        if temp.data == value: return True
        while temp.next_element:
            if temp.next_element == value:
                return True
            temp = temp.next_element
        return False

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True
    '''
    There are three basic delete operations for linked lists:

    Deletion at the head
    Deletion by value
    Deletion at the tail

    '''
    def delete_at_head(lst):
    # Get Head and firstElement of List
        first_element = lst.get_head()

    # if List is not empty then link head to the
    # nextElement of firstElement.
        if first_element is not None:
            lst.head_node = first_element.next_element
            first_element.next_element = None
        return
    
    def delete(lst, value):
    # Write your code here
        deleted = False
        
        if lst.is_empty():
            return deleted
        val = lst.get_head()
        previous = None
        if val.data is value:
            lst.delete_at_head()
            deleted = True
            return deleted
        while val is not None:
            if val.data == value:
                previous.next_element = val.next_element
                val.next_element == None
                deleted=True
                break
            previous = val
            val = val.next_element
        return deleted
    
    def length(lst):
        temp = lst.get_head()
        size = 0
        if not temp: return 0
        while temp is not None:
            temp = temp.next_element
            size += 1
        return size
    
    def reverse(lst):
        current = lst.get_head()
        previous = None
        next = None
        while current:
            next = current.next_element #Save what we're working on next
            current.next_element = previous #Reversal
            previous = current #After reversal, make it previous
            current = next #Get our current
            lst.head_node = previous #Set head to previous so we can iterate again
        return lst
    
    def detect_loop(lst): # Floyd’s Cycle-Finding Algorithm
        slow = lst.get_head()
        fast = lst.get_head()
        while fast and fast.next_element:
            slow = slow.next_element
            fast = fast.next_element.next_element
            if slow == fast: return True
        return False

    def find_mid(lst):
        length = lst.length()
        mid = 0
        if length % 2 == 0: mid = length // 2
        if length % 2 == 1: mid = (length // 2) + 1
        temp = lst.get_head()
        while mid > 0 and temp:
            temp = temp.next_element
            mid -= 1
        return temp.data

    def remove_duplicates(lst):
        if lst.is_empty():
            return None

        # If list only has one node, leave it unchanged
        if lst.get_head().next_element is None:
            return lst

        outer_node = lst.get_head()
        while outer_node:
            inner_node = outer_node  # Iterator for the inner loop
            while inner_node:
                if inner_node.next_element:
                    if outer_node.data == inner_node.next_element.data:
                        # Duplicate found, so now removing it
                        new_next_element = inner_node.next_element.next_element
                        inner_node.next_element = new_next_element
                    else:
                        # Otherwise simply iterate ahead
                        inner_node = inner_node.next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            outer_node = outer_node.next_element

        return lst
    
    def union(list1, list2):
    # Return other List if one of them is empty
        if (list1.is_empty()):
            return list2
        elif (list2.is_empty()):
            return list1

        start = list1.get_head()

        # Traverse the first list till the tail
        while start.next_element:
            start = start.next_element

        # Link last element of first list to the first element of second list
        start.next_element = list2.get_head()
        list1.remove_duplicates()
        return list1

    def intersection(list1, list2):

        result = LinkedList()
        current_node = list1.get_head()

        # Traversing list1 and searching in list2
        # insert in result if the value exists
        while current_node is not None:
            value = current_node.data
            if list2.search(value) is not None:
                result.insert_at_head(value)
            current_node = current_node.next_element

        # Remove duplicates if any
        result.remove_duplicates()
        return result

    def find_nth(lst, n):
        if (lst.is_empty()):
            return -1

        # Find Length of list
        length = lst.length() - 1

        # Find the Node which is at (len - n + 1) position from start
        current_node = lst.get_head()

        position = length - n + 1

        if position < 0 or position > length:
            return -1

        count = 0

        while count is not position:
            current_node = current_node.next_element
            count += 1

        if current_node:
            return current_node.data
        return -1