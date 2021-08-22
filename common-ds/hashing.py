'''
Hashing #

Until now, the overall time complexity accomplished by most of the data structures in insertion, deletion, and search was up to O(logn) or O(nlogn), which is pretty good. But for a significantly large amount of data, this complexity starts to adversely affect the efficiency of an algorithm.

The ideal data structure is one that takes a constant amount of time to perform all three operations. And that is where hashing steps into the spotlight!

Hashing is a process used to store an object according to a unique key. This means that hashing always creates a key-value pair. A collection of such pairs forms a dictionary where every object or value can be looked up according to its key. Hence, the search operation can be performed in O(1).

The concept of hashing has given birth to several new data structures, but the most prominent one is the hash table.

Hash Tables #

If your algorithm prioritizes search operations, then a hash table is the best data structure for you. In Python, hash tables are generally implemented using lists as they provide access to elements in constant time.

In Python, we have several in-built types such as set and dict which can provide us the hash table functionality

In this section, we will implement our own hash table since it is a very popular topic in coding interviews.

Let’s get started by defining the building blocks on an efficient hash table.

The performance of a hash table depends on three fundamental factors:

    Hash function
    Size of the hash table
    Collision handling method

Restricting the Key Size #

In the last lesson, we learned that a list can be used to implement a hash table in Python. A key is used to map a value on the list and the efficiency of a hash table depends on how a key is computed. At first glance, you may observe that we can directly use the indices as keys because each index is unique.

The only problem is that the key would eventually exceed the size of the list and, at every insertion, the list would need to be resized. Syntactically, we can easily increase list size in Python, but as we learned before, the process still takes O(n) time at the back end.

In order to limit the range of the keys to the boundaries of the list, we need a function that converts a large key into a smaller key. This is the job of the hash function.

A hash function simply takes an item’s key and returns the corresponding index in the list for that item. Depending on your program, the calculation of this index can be a simple arithmetic or a very complicated encryption method. However, it is very important to choose an efficient hashing function as it directly affects the performance of the hash table mechanism.

Let’s have a look at some of the most common hash functions used in modern programming
'''
#Arithmetic Modular #

def hash_modular(key, size):
    return key % size


lst = [None] * 10  # List of size 10
key = 35
index = hash_modular(key, len(lst))  # Fit the key into the list size
print("The index for key " + str(key) + " is " + str(index))

# Truncation #

# Select a part of the key as the index rather than the whole key. Once again, we can use a mod function for this operation, although it does not need to be based on the list size:

# key=123456 −> index=3456 key = 123456 \text{ } -> \text{ } index = 3456 key=123456 −> index=3456
def hash_trunc(key):
    return key % 1000  # Will always give us a key of up to 3 digits


key = 123456
index = hash_trunc(key)  # Fit the key into the list size
print("The index for key " + str(key) + " is " + str(index))

# Folding #

# Divide the key into small chunks and apply a different arithmetic strategy at each chunk. For example, you add all the smaller chunks together:

# key=456789,  chunk=2 −> index=45+67+89key = 456789
def hash_fold(key, chunk_size):  # Define the size of each divided portion
    str_key = str(key)  # Convert integer into string for slicing
    print("Key: " + str_key)
    hash_val = 0
    print("Chunks:")
    for i in range(0, len(str_key), chunk_size):
        if(i + chunk_size < len(str_key)):
            # Slice the appropriate chunk from the string
            print(str_key[i:i+chunk_size])
            hash_val += int(str_key[i:i+chunk_size])  # convert into integer
        else:
            print(str_key[i:len(str_key)])
            hash_val += int(str_key[i:len(str_key)])
    return hash_val


key = 3456789
chunk_size = 2
print("Hash Key: " + str(hash_fold(key, chunk_size)))

'''
When you map large keys into a small range of numbers from 0-N, where N is the size of the list, there is a huge possibility that two different keys may return the same index. This phenomenon is called collision.

Strategies to Handle Collisions #

There are several ways to work around collisions in the list. The three most common strategies are:

    Linear Probing
    Chaining
    Resizing the list

Linear Probing #

This strategy suggests that if our hash function returns an index that is already filled, move to the next index. This increment can be based on a fixed offset value to an already computed index. If that index is also filled, traverse further until a free spot is found.

One drawback of using this strategy is that if we don’t pick an offset wisely, we can end up back where we started and, hence, miss out on so many possible positions in the list.
Example #

Let’s say the size of our list is 20. We pass a key to the hash function which takes the modular and returns 2.

If the second position is already filled, we jump to another location based on the offset value. Let’s say this value is 4. Now we reach the sixth position. If this is also occupied, we repeat the process and move to the tenth position and so on.

2. Chaining #

In the chaining strategy, each slot of our hash table holds a pointer to another data structure such as a linked list or a tree. Every entry at that index will be inserted into the linked list for that index.

As you can see, chaining allows us to hash multiple key-value pairs at the same index in constant time (insert at head for linked lists).

This strategy greatly increases performance, but it is costly in terms of space.

3. Resizing the List #

Another way to reduce collisions is to resize the list. We can set a threshold and once it is crossed, we can create a new table which is double the size of the original. All we have to do then is to copy the elements from the previous table.

Resizing the list significantly reduces collisions, but the function itself is costly. Therefore, we need to be careful about the threshold we set. A typical convention is to set the threshold at 0.6, which means that when 60% of the table is filled, the resize operation needs to take place.

Another factor to keep in mind is the content of the hash table. The stored records might be concentrated in one region, leaving the rest of the list empty. However, this behavior will not be picked up by the resize function and you will end up resizing inappropriately.

Some other strategies to handle collisions include quadratic probing, bucket method, random probing, and key rehashing. We must use a strategy that best suits our hashing algorithm and the size of the data that we plan to store.
'''


'''
Hash Table Using Bucket Chaining #

As said earlier, hash tables are implemented using lists in Python. The implementation itself is quite simple. We will use the chaining strategy along with the resize operation to avoid collisions in the table.

All the elements with the same hash key will be stored in a linked list at that index. In data structures, these lists are called buckets. The size of the hash table is set as n*m where n is the number of keys it can hold and m is the number of slots each bucket contains. Each slot holds a key/value pair.

Implementation #

We will start by building a simple HashEntry class. As discussed earlier, a typical hash entry consists of three data members: the key, the value, and the reference to a new entry. Here’s how we will code this in Python:


'''
class HashEntry:
    def __init__(self, key, data):
        # key of the entry
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.nxt = None

    def __str__(self):
        return str(entry.key) + ", " + entry.value

entry = HashEntry(3, "Educative")
print(entry)

'''
Now, we’ll create the HashTable class which is a collection of HashEntry objects. We will also keep track of the total number of slots in the hash table and the current size of the hash table. These two variables will come in handy when we need to resize the table.
'''

class HashTable:
    # Constructor
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots
    # Helper Functions

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.get_size() == 0


ht = HashTable()
print(ht.is_empty())
'''
The last thing we need is a hash function where a hash function maps values to a slot in the hash table. We tried out some different approaches in the previous lessons. For our implementation, we will simply take the modular of the key with the total size of the hash table (slots).
'''

# Hash Function
def get_index(self, key):
    # hash is a built in function in Python
    hash_code = hash(key)
    index = hash_code % self.slots
    return index

'''
Resizing in a Hash Table #

To start things off, we will make sure that the hash table doesn’t get loaded up beyond a certain threshold. Whenever it crosses the threshold, we shift the elements from the current table to a new table with double the capacity. This helps us avoid collisions.

To implement this, we will make the resize() function.
'''
from HashEntry import HashEntry


class HashTable:
    # Constructor
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots
        self.threshold = 0.6

    # Helper Functions
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() is 0

    # Hash Function
    def get_index(self, key):
        # hash is a built in function in Python
        hash_code = hash(key)
        index = hash_code % self.slots
        return index

    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        # rehash all items into new slots
        for item in self.bucket:
            head = item
            while head is not None:
                new_index = hash(head.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value
                            node = None
                        elif node.nxt is None:
                            node.nxt = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.nxt
                head = head.nxt
        self.bucket = new_bucket
        self.slots = new_slots

    def insert(self, key, value):
        # Find the node with the given key
        b_index = self.get_index(key)
        if self.bucket[b_index] is None:
            self.bucket[b_index] = HashEntry(key, value)
            self.size += 1
        else:
            head = self.bucket[b_index]
            while head is not None:
                if head.key is key:
                    head.value = value
                    break
                elif head.nxt is None:
                    head.nxt = HashEntry(key, value)
                    self.size += 1
                    break
                head = head.nxt

        load_factor = float(self.size) / float(self.slots)
        # Checks if 60% of the entries in table are filled, threshold = 0.6
        if load_factor >= self.threshold:
            self.resize()
        
    # Return a value for a given key
    def search(self, key):
        # Find the node with the given key
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # Search key in the slots
        while head is not None:
            if head.key == key:
                return head.value
            head = head.nxt
        # If key not found
        return None

    # Remove a value based on a key
    def delete(self, key):
        # Find index
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        # If key exists at first slot
        if head.key is key:
            self.bucket[b_index] = head.nxt
            # Decrease the size by one
            self.size -= 1
            return self
        # Find the key in slots
        prev = None
        while head is not None:
            # If key exists
            if head.key is key:
                prev.nxt = head.nxt
                # Decrease the size by one
                self.size -= 1
                return
            # Else keep moving in chain
            prev = head
            head = head.nxt

        # If key does not exist
        return

from HashTable import HashTable

table = HashTable()  # Create a HashTable
print(table.is_empty())
table.insert("This", 1)
table.insert("is", 2)
table.insert("a", 3)
table.insert("Test", 4)
table.insert("Driver", 5)
print("Table Size: " + str(table.get_size()))
print("The value for 'is' key: " + str(table.search("is")))
table.delete("is")
table.delete("a")
print("Table Size: " + str(table.get_size()))


# Insertion in Table #

# Insertion in hash tables is a simple task and it usually takes a constant amount of time. When the hash function returns the index for our input key, we check if there is a hash entry already present at that index (if it does, a collision has occurred). If not, we simply create a new hash entry for the key/value. However, if the index is not None, we will traverse through the bucket to check if an object with our key exists.

# It is possible that the key we are inserting already exists. In this case, we will simply update the value. Otherwise, we add the new entry at the end of the bucket. The average cost of insertion is O(1). However, the worst case is O(n) as for some cases, the entire bucket needs to be traversed where all n elements are in a single bucket.

# After each insertion, we will also check if the hash table needs resizing. The threshold will be a data member of the HashTable class with a fixed value of 0.6

'''
Search in a Hash Table #

One of the features that make hash tables efficient is that search takes O(1) amount of time. The search function takes in a key and sends it through the hash function to get the corresponding index in the table. If a hash entry with the desired key/value pair is found at that index, its value is returned. Search can take up to O(n) time, where n is the number of hash entries in the table. This is possible if all values get stored in the same bucket, then we would have to traverse the whole bucket to reach the entry.

Deletion in Table #

Deletion can take up to O(n) time where n is the number of hash entries in the table. If they all get stored in the same bucket, we would have to traverse the whole bucket to reach the entry we want to delete. The average case, however, is still O(1).
'''

'''
Comparison Between Trees and Hash Tables #

Both of these data structures can be used for the same job, but their performance would vary based on the nature of your program. Let’s take a look at some of the factors we need to keep in mind when deciding the appropriate data structure.
Basic Operations #

On average, hash tables can perform search, insertion, and deletion in constant time whereas trees usually work in O(log n). However, in the worst case, the performance of hash tables can come down to O(n) where n is the total number of hash entries. An AVL tree would maintain O(log n) even in the worst case.
Hash Function #

An efficient hash table requires a smart hash function that would distribute the keys over all the space that is available to us. A tree is simpler to implement in this regard as it accesses extra space only when needed and no hash function is required to optimize its structure.
Order of Data #

If our application needs data to be ordered in a specific sequence, trees would prove more useful because a BST or an AVL tree maintains order. Hash tables are the smarter choice if your data can be stored randomly.

'''

'''
Dict vs Set

dict or dictionary is a Mapping Type object which maps hashable values to arbitrary objects. It stores an element in the form of key-value pairs.

It provides the basic functionality of hashing along with some helper functions that help in the process of insertion, deletion, and search.

Some of the key features of dict are given below:

    An dict stores key-value pairs (examples given below) to map a key to the value:

abc−>123

xyz−>456

    dict cannot contain duplicate keys. It can, however, have duplicate values.

    dict does not store elements in any order either by the key or the value.


    dict uses a hash table for its implementation. It takes the key and then maps it into the range of hash table using the hash function.

    On average, the complexity of the basic operation is O(1)O(1)O(1). It will go up to O(n)O(n)O(n) in the worst-case.

'''

'''
Challenge 1
Implement the is_subset(list1,list2) function which will takes two lists as input and checks whether one list is the subset of the other. This method is already available in Python, but we’ll be implementing it using hash tables.

    Note: The input lists do not contain duplicate values.

Use the Python set as your hash table.
Input #

Two lists of integers.
Output #

True if list2 is a subset of list1.
Sample Input #

list1 = [9,4,7,1,-2,6,5]
list2 = [7,1,-2]

Sample Output #

True
'''
def is_subset(list1, list2):
    s = set(list1)  # Create a set with list1 values
    # Traverse list 2 elements
    for elem in list2:
        # Return false if an element not in list1
        if elem not in s:
            return False
    # Return True if all elements in list1
    return True


list1 = [9, 4, 7, 1, -2, 6, 5]
list2 = [7, 1, -2]
list3 = [10, 12]
print(is_subset(list1, list2))
print(is_subset(list1, list3))

'''
The solution is very simple when working with the Pythonic hash table Set. We simply iterate over list2 and list3 to see whether their elements can be found in list1.

At the back end, the values are checked against their hashed indices in list1.
Time Complexity #

For a lookup list with m elements and a subset list with n elements, the time complexity is O(m+n).

'''
'''
Challenge 2

You have to implement the is_disjoint() function which checks whether two given lists are disjoint or not. Two lists are disjoint if there are no common elements between them. The assumption is that there are no duplicate elements in each list.
Input #

Two lists of integers.
Output #

It returns True if the two are disjoint. Otherwise, it returns False.
Sample Input #

list1 = [9,4,3,1,-2,6,5]
list2 = [7,10,8]

Sample Output #

True
'''

def is_disjoint(list1, list2):
    s = set(list1)  # Create set of list1 elements
    # iterate list 2
    for elem in list2:
        # if element in list1 then return False
        if elem in s:
            return False
    # Return True if no common element
    return True


list1 = [9, 4, 3, 1, -2, 6, 5]
list2 = [7, 10, 8]
list3 = [1, 12]
print(is_disjoint(list1, list2))
print(is_disjoint(list1, list3))

'''
Nothing tricky going on here. The problem is very similar to the previous one. All we have to do is create a set for list1 and as soon as we find value from list2 or list3 in the set, we can conclude that the two lists are not disjoint. Since the set uses a hash table under the hood, the complexity for checking an element to be in the set will be O(1)O(1)O(1).
Time Complexity #

For a lookup list with m elements and a subset list with n elements, the time complexity is O(m+n).

'''
'''
Challenge 3
By definition, (a, b) and (c, d) are symmetric pairs iff, a = d and b = c. In this problem, you have to implement the find_symmetric(list) function which will find all the symmetric pairs in a given list.
Input #

A list.
Output #

A list containing all the symmetric pairs of elements in the input list.
Sample Input #

list = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]

Sample Output #

[[3, 4], [4, 3], [5, 9], [9, 5]]

'''
def find_symmetric(my_list):
    # Create an empty set
    pair_set = set()
    result = []
    # Traverse through the given list
    for pair in my_list:
        # Make a tuple and a reverse tuple out of the pair
        pair_tup = tuple(pair)
        pair.reverse()
        reverse_tup = tuple(pair)
        # Check if the reverse tuple exists in the set
        if(reverse_tup in pair_set):
            # Symmetric pair found
            result.append(list(pair_tup))
            result.append(list(reverse_tup))
        else:
            # Insert the current tuple into the set
            pair_set.add(pair_tup)
    return result


arr = [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]]
symmetric = find_symmetric(arr)
print(symmetric)

'''
The solution above uses a Python set. However, a dictionary can be used as well. For each pair in the list, we create a tuple and a reverse tuple.

    Note: Tuples are an immutable sequence of elements in python.

If the reverse tuple already exists in the set, we have found symmetric pairs.

If not, we can add the tuple to the list. If a symmetric pair exists, it will be able to find this pair later in the loop.
Time Complexity #

The hash table lookups work in constant time. Hence, our traversal of the input list makes the algorithm run in O(n) where n is the list size.

'''
'''
Challenge 4
You have to implement the trace_path() function which will take in a list of source-destination pairs and return the correct sequence of the whole journey from the first city to the last.
Input #

A Python dict containing string pairs of source-destination cities.
Output #

A list of source-destination pairs in the correct order.
Sample Input #

dict = {
  "NewYork": "Chicago",
  "Boston": "Texas",
  "Missouri": "NewYork",
  "Texas": "Missouri"
}

Sample Output #

[["Boston", "Texas"] , ["Texas", "Missouri"] , ["Missouri", "NewYork"] , ["NewYork", "Chicago"]]

'''
def trace_path(my_dict):
    result = []
    # Create a reverse dict of the given dict i.e if the given dict has (N,C)
    # then reverse dict will have (C,N) as key-value pair
    # Traverse original dict and see if it's key exists in reverse dict
    # If it doesn't exist then we found our starting point.
    # After the starting point is found, simply trace the complete path
    # from the original dict.
    reverse_dict = dict()
    # To fill reverse dict, iterate through the given dict
    keys = my_dict.keys()
    for key in keys:
        reverse_dict[my_dict.get(key)] = key
    # Find the starting point of itinerary
    from_loc = None
    keys_rev = reverse_dict.keys()
    for key in keys:
        if key not in reverse_dict:
            from_loc = key
            break
            # Trace complete path
    to = my_dict.get(from_loc)
    while to is not None:
        result.append([from_loc, to])
        from_loc = to
        to = my_dict.get(to)
    return result


my_dict = dict()
my_dict["NewYork"] = "Chicago"
my_dict["Boston"] = "Texas"
my_dict["Missouri"] = "NewYork"
my_dict["Texas"] = "Missouri"
print(trace_path(my_dict))


'''
The first thing we need to do is find the starting point of the journey. A reverse_dict is created to switch the sources and destinations in the original map.

The key which does not appear in reverse_dict has never been a destination in map. Hence, it is the starting city.

From here, we simply traverse from city to city based on the previous destination.
Time Complexity #

Although a hash table is created and traversed, both take the same amount of time. The complexity for this algorithm is O(n) where n is the number of source-destination pairs.

'''

'''
Challenge 5
In this problem, you have to implement the find_pair() function which will find two pairs, [a, b] and [c, d], in a list such that :

a+b=c+da+b = c+da+b=c+d

You only have to find the first two pairs in the list which satisfies the above condition.
Input #

A list of distinct integers.
Output #

A list containing two pairs, (a, b) and (c, d), which satisfy a + b = c + d
Sample Input #

my_list = [3, 4, 7, 1, 12, 9]

Sample Output #

[[4,12],[7,9]]

'''
def find_pair(my_list):
    result = []
    # Create a dictionary my_dict with the key being the sum
    # and the value being a pair, i.e key = 3 , value = {1,2}
    # Traverse all possible pairs in my_list and store sums in my_dict
    # If sum already exists then print out the two pairs.
    my_dict = dict()
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            added = my_list[i] + my_list[j]  # calculate sum
            # the 'in' operator on dict() item has a complexity of O(1)
            # This is due to hashing
            # On a list, the 'in' operator would have the complexity of O(n)
            if added not in my_dict:
                # If added is not present in dict then insert it with pair
                my_dict[added] = [my_list[i], my_list[j]]
            else:
                # added already present in the dictionay
                prev_pair = my_dict.get(added)
                # Since list elements are distinct, we don't
                # need to check if any element is common among pairs
                second_pair = [my_list[i], my_list[j]]
                result.append(prev_pair)
                result.append(second_pair)
                return result
    return result


my_list = [3, 4, 7, 1, 12, 9, 0]
print(find_pair(my_list))
'''
Each element in my_list is summed with all other elements one by one and the pair is stored. The sum becomes the key in the my_dict dictionary. At every key, we store the integer pair whose sum generated that key.

Whenever a sum is found such that its key in the dictionary already has an integer pair stored in it, we can conclude that this sum can be made by two different pairs in the list. These two pairs are then returned in the result list.
Time Complexity #

The algorithm contains a nested loop. However, the inner loop always starts one step ahead of the outer loop:

for i in range(len(my_list)):
  for j in range(i+1,len(my_list)):

As the outer loop grows, the inner loop gets smaller. First, the inner loop runs n - 1 times, then n - 2, and so on…

This is an arithmetic series.

After evaluating the series for these values, the time complexity of this algorithm is O(n2)
'''

'''
Challenge 6
You must implement the find_sub_zero(my_list) function which will take in a list of positive and negative integers. It will tell us if there exists a sublist in which the sum of all elements is zero. The term sublist implies that the elements whose sum is 0 must occur consecutively.

A list with these contents would return True:

[6, 4, -7, 3, 12, 9]

Whereas this would return False as the elements which sum up to be 0 do not appear together:

[-7, 4, 6, 3, 12, 9]

Input #

A list containing positive and negative integers.
Output #

Returns True if there exists a sublist with its sum equal to 0. Otherwise, the function returns False.
Sample Input #

my_list = [6, 4, -7, 3, 12, 9]

Sample Output #

True

'''
def find_sub_zero(my_list):
    # Use hash table to store the cumulative sum as a key and
    # the element as the value till which the sum has been calculated
    # Traverse the list and return true if either
    # elem == 0 or sum == 0 or hash table already contains the sum
    # If you completely traverse the list and haven't found any 
    # of the above three conditions, then simply return false
    ht = dict()
    total_sum = 0
    # Traverse through the given list
    for elem in my_list:
        total_sum += elem
        if elem is 0 or total_sum is 0 or ht.get(total_sum) is not None:
            return True
        ht[total_sum] = elem
    return False


my_list = [6, 4, -7, 3, 12, 9]

print(find_sub_zero(my_list))
'''
The naive solution would be to iterate the list in a nested loop, summing each element with all the elements succeeding it.

A hash table makes things much simpler.

We basically have to check for 3 conditions:

    If 0 exists in the list
    If the sum becomes zero in the iteration
    If the sum reverts back to a value which was already a key in the hash table. This means that there was a sublist that has a sum of zero making the overall sum to go back to a previous value.

Any of these three conditions confirms the existence of a sublist that sums up to be zero.
Time Complexity #

As always, a linear iteration over n elements means that the algorithm’s time complexity is O(n).

'''

'''
Challenge 7
You have to implement the is_formation_possible() function which will find whether a given word can be formed by combining two words from a dictionary. We assume that all words are in lower case.
Input #

A list and a query word containing lowercase characters.
Output #

Returns True if the given word can be generated by combining two words from the list.
Sample Input #

lst = ["the", "hello", "there", "answer", "any",
       "by", "world", "their","abc"]

word = "helloworld"

Sample Output #

True
'''
from HashTable import HashTable


def is_formation_possible(lst, word):

    if len(word) < 2 or len(lst) < 2:
        return False

    hash_table = HashTable()
    for elem in lst:
        hash_table.insert(elem, True)

    for i in range(1, len(word)):
        # Slice the word into two strings in each iteration
        first = word[0:i]
        second = word[i:len(word)]
        check1 = False
        check2 = False

        if hash_table.search(first) is not None:
            check1 = True
        if hash_table.search(second) is not None:
            check2 = True

        # Return True If both substrings are present in the hash table
        if check1 and check2:
            return True

    return False


keys = ["the", "hello", "there", "answer",
        "any", "educative", "world", "their", "abc"]
print(is_formation_possible(keys, "helloworld"))
'''
This is as efficient as the implementation as the trie implementation. We insert all the dictionary words into a hash table.

Just like before, a for loop begins and slices the word into two substrings in each iteration. Whenever both substrings are found in the hash table, the function returns True.

    Note: The solution only works for two words and not more.

Time Complexity #

We perform the insert operation m times for a list of size m. After that, we linearly traverse the word of size n once. Furthermore, we slice strings of size n in each iteration. Hence the total time complexity is O(m+n2)O(m + n^2)O(m+n​2​​).

'''

'''
Challenge 8
In this problem, you have to implement the findSum(lst,k) function which will take a number k as input and return two numbers that add up to k.

You have already seen this challenge previously in chapter 2 of this course. Here you would use HashTables for a more efficient solution.
Input #

A list and a number k
Output #

A list with two integers a and b that add up to k
Sample Input #

lst = [1,21,3,14,5,60,7,6]
k = 81

Sample Output #

lst = [21,60]

For example, in this illustration, we are given 81 as the number k and when we traverse the whole list we find that 21 and 60 are the integers that add up to 81.

'''
def findSum(lst, k):
    foundValues = {}
    for ele in lst:
        # Check for value in dictionary
        # If found return 
        try:
            foundValues[k - ele]
            return [k - ele, ele]
        except KeyError:
            foundValues[ele] = 0
    return "No numbers add upto k"


print(findSum([1, 3, 2, 4], 6))
 
'''
The best way to solve this problem is to insert every element into a dictionary. This takes O(1) as constant time insertion.

Then, for every element x in the list, we can just look up its complement, kkk−xxx, and, if found, return both kkk−xxx and xxx.
Time Complexity #

Each lookup is a constant time operation. Overall the running time of this approach is O(n)O(n)O(n).

Solution #2: Using the Python set() #
'''

def findSum(lst, value):
    foundValues = set()
    for ele in lst:
        if value - ele in foundValues:
            return [value-ele, ele]
        foundValues.add(ele)
    return False


print(findSum([1, 2, 3, 4], 6))
'''
This solution does the same thing as solution #1 except that it uses Python’s built-in set() which makes foundValues an iterable sequence like a dictionary. Note that set.add method adds an element if element is not present in the set as in line 6.
Time Complexity #

The time complexity of the solution above is O(n)O(n)O(n).

'''
'''
Challenge 9
Implement a function, findFirstUnique(lst) that returns the first unique integer in the list. Unique means the number does not repeat and appears only once in the whole list.

You have already seen this challenge previously in chapter 2 of this course. Here you would use dict or set for a more efficient solution.
Input #

A list of integers
Output #

The first unique element in the list
Sample Input #

[9,2,3,2,6,6]

Sample Output #

9
'''

def findFirstUnique(lst):
    counts = {}  # Creating a dictionary
    # Initializing dictionary with pairs like (lst[i],count)
    counts = counts.fromkeys(lst, 0)
    for ele in lst:
        # counts[ele] += 1  # Incrementing for every repitition
        counts[ele] = counts[ele]+1
    answer_key = None
    # filter first non-repeating 
    for ele in lst:
        if (counts[ele] is 1):
            answer_key = ele
            break
    return answer_key


print(findFirstUnique([1, 1, 1, 2]))

#ORRRR

import collections


def findFirstUnique(lst):
    orderedCounts = collections.OrderedDict()  # Creating an ordered dictionary
    # Initializing dictionary with pairs like (lst[i],0)
    orderedCounts = orderedCounts.fromkeys(lst, 0)
    for ele in lst:
        orderedCounts[ele] += 1  # Incrementing for every repitition
    for ele in orderedCounts:
        if orderedCounts[ele] == 1:
            return ele
    return None


print(findFirstUnique([1, 1, 1, 2, 3, 2, 4]))

'''
The keys in the counts dictionary are the elements of the given list and the values are the number of times each element appears in the list. We return the element that appears at most once in the list on line 23. We return the first non-repeating element in the list after traversing lst.

    Caveat Note that Python dictionaries do not maintain the order that elements were added to them so this solution will not necessarily display the FIRST non-repeating integer when traversing the dictionary! To get around this, we can use Python’s ordered dictionary as follows.

Time Complexity #

Since the list is only iterated over only twice and the counts dictionary is initialized with linear time complexity, therefore the time complexity of this solution is linear, i.e., O(n)O(n)O(n).

Since the list is only iterated over only once, therefore the time complexity of this solution is linear, i.e., O(n)O(n)O(n).
'''
'''
Challenge 10

By definition, a loop is formed when a node in your linked list points to a previously traversed node.

You must implement the detect_loop() function which will take a linked list as input and deduce whether or not a loop is present.

You have already seen this challenge previously in chapter 3 of this course. Here you would use HashTables for a more efficient solution.
Input #

A singly linked list.
Output #

Returns True if the given linked list contains a loop. Otherwise, it returns False
Sample Input #

LinkedList = 7->14->21->7 # Both '7's are the same node. Not duplicates.

Sample Output #

True
'''

from LinkedList import LinkedList
from Node import Node


def detect_loop(lst):
    # Used to store nodes which we already visited
    visited_nodes = set()
    current_node = lst.get_head()

    # Traverse the set and put each node in the visitedNodes set
    # and if a node appears twice in the map
    # then it means there is a loop in the set
    while current_node:
        if current_node in visited_nodes:
            return True
        visited_nodes.add(current_node)  # Insert node in visitedNodes set
        current_node = current_node.next_element
    return False

# ------------------------------
'''
This is the primitive approach, but it works nonetheless.

We iterate over the whole linked list and add each visited node to a visited_nodes set. At every node, we check whether it has been visited or not.

By principle, if a node is revisited, a cycle exists!
Time Complexity #

We iterate the list once. On average, lookup in a set takes O(1) time. Hence, the average runtime of this algorithm is O(n). However, in the worst case, lookup can increase up to O(n), which would cause the algorithm to work in O(n2).

'''

lst = LinkedList()

lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
print(detect_loop(lst))

head = lst.get_head()
node = lst.get_head()

# Adding a loop
for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element

print(detect_loop(lst))

'''
Challenge 11
You will now be implementing the remove_duplicates() function. When a linked list is passed to this function, it removes any node which is a duplicate of another existing node.

You have already seen this challenge previously in chapter 3 of this course. Here you would use HashTables for a more efficient solution.

Input #

A linked list.
Output #

A list with all the duplicates removed.
Sample Input #

LinkedList = 1->2->2->2->3->4->4->5->6

Sample Output #

LinkedList = 1->2->3->4->5->6
'''

from LinkedList import LinkedList
from Node import Node


def remove_duplicates(lst):
    current_node = lst.get_head()
    prev_node = lst.get_head()
    # To store values of nodes which we already visited
    visited_nodes = set()
    # If List is not empty and there is more than 1 element in List
    if not lst.is_empty() and current_node.next_element:
        while current_node:
            value = current_node.data
            if value in visited_nodes:
                # current_node is already in the HashSet
                # connect prev_node with current_node's next element
                # to remove it
                prev_node.next_element = current_node.next_element
                current_node = current_node.next_element
                continue
            # Visiting currentNode for first time
            visited_nodes.add(current_node.data)
            prev_node = current_node
            current_node = current_node.next_element


lst = LinkedList()
lst.insert_at_head(7)
lst.insert_at_head(7)
lst.insert_at_head(22)
lst.insert_at_head(14)
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)

lst.print_list()

remove_duplicates(lst)
lst.print_list()

'''
This is, perhaps, the most efficient way of removing duplicates from a linked list. We’ve seen this approach before in Challenge 10 when we detected a loop in our linked list.

Every node we traverse is added to the visited_nodes set. If we reach a node that already exists in the set, it must be a duplicate.

prev_node is used to keep track of the preceding node. This allows us to easily manipulate the previous and next nodes during the deletion of our current_node.
Time Complexity #

This is a linear algorithm, hence, the time complexity is O(n).
'''
'''
Challenge 12
Union and intersection are two of the most popular operations which can be performed on data sets. Now, you will be implementing them for linked lists! Let’s take a look at their definitions:
Union #

    Given two lists, A and B, the union is the list that contains elements or objects that belong to either A, B, or to both.

Intersection #

    Given two lists, A and B, the intersection is the largest list which contains all the elements that are common to both the sets.

The union function will take two linked lists and return their union.

The intersection function will return all the elements that are common between two linked lists.

You have already seen this challenge previously in chapter 3 of this course. Here you would use HashTables for a more efficient solution.
Input #

Two linked lists.
Output #

    A list containing the union of the two lists.
    A list containing the intersection of the two lists.

Sample Input #

list1 = 10->20->80->60
list2 = 15->20->30->60->45

Sample Output #

union = 10->20->80->60->15->30->45
intersection = 20->60

'''
from LinkedList import LinkedList
from Node import Node


def union(list1, list2):
    # Return other List if one of them is empty
    if (list1.is_empty()):
        return list2
    elif (list2.is_empty()):
        return list1
    
    unique_values = set()
    result = LinkedList()

    start = list1.get_head()

    # Traverse the first list till the tail
    while start:
        unique_values.add(start.data)
        start = start.next_element

    start = list2.get_head()

    # Traverse the second list till the tail
    while start:
        unique_values.add(start.data)
        start = start.next_element
    
    # Add elements of unique_vales to result
    for x in unique_values:
        result.insert_at_head(x)
    return result


ulist1 = LinkedList()
ulist2 = LinkedList()
ulist1.insert_at_head(8)
ulist1.insert_at_head(22)
ulist1.insert_at_head(15)

ulist2.insert_at_head(21)
ulist2.insert_at_head(14)
ulist2.insert_at_head(15)
ulist2.insert_at_head(7)

new_list = union(ulist1,ulist2)

new_list.print_list()
'''
Nothing too tricky going on here. We traverse to the tail of the first list and link it to the first node of the second list. All we have to do now is remove duplicates from the combined list.

Another approach would be to add all unique elements to a set. It would also work in the same time complexity, assuming that hashing is O(1) on average.
Time Complexity #

If we did not have to care for duplicates, The runtime complexity of this algorithm would be O(m) where m is the size of the first list. However, because of duplicates, we need to traverse the whole union list. This increases the time complexity to O(m + n) where m is the size of the first list and n is the size of the second list.

'''
from LinkedList import LinkedList
from Node import Node


def intersection(list1, list2):

    result = LinkedList()
    visited_nodes = set()  # Keep track of all the visited nodes
    current_node = list1.get_head()

    # Traversing list1 and adding all unique nodes into the hash set
    while current_node is not None:
        value = current_node.data
        if value not in visited_nodes:
            visited_nodes.add(value)  # Visiting current_node for first time
        current_node = current_node.next_element

    start = list2.get_head()

    # Traversing list 2
    # Nodes which are already present in visited_nodes are added to result
    while start is not None:
        value = start.data
        if value in visited_nodes:
            result.insert_at_head(start.data)
        start = start.next_element
    result.remove_duplicates()
    return result


ilist1 = LinkedList()
ilist2 = LinkedList()

ilist1.insert_at_head(14)
ilist1.insert_at_head(22)
ilist1.insert_at_head(15)

ilist2.insert_at_head(21)
ilist2.insert_at_head(14)
ilist2.insert_at_head(15)

lst = intersection(ilist1, ilist2)
lst.print_list()

'''
You are already familiar with this approach. We simply create a set that contains all the unique elements from list1. If any of these values are found in list2, it is added to the result linked list. Since we insert at head, as shown on line 25, insert works in constant time.
Time Complexity #

The time complexity will be O(m + n) where m is the size of the first list and n is the size of the second list.

'''