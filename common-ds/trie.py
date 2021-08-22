'''
A tree-like data structure that proves to be really efficient while solving programming problems related to strings.

This data structure is called a trie and is also known as a Prefix Tree. We will soon find out why.

The tree trie is derived from “retrieval.” As you can guess, the main purpose of using this structure is to provide fast retrieval. 
Tries are mostly used in dictionary word searches, Spell-Checking,  search engine auto-suggestions, and IP routing as well.

Another real-life use of Tries is searching for contacts in our contact list. It provides auto-suggestions based on the combination of letters that we enter. As you’ll see later on, this can also be performed with hash tables,
but a hash table won’t be as efficient as a trie.

'''

'''
Properties of a Trie #

To maintain its overall efficiency, tries follow a certain structure:

    Tries are similar to graphs as they are a combination of nodes where each node represents a unique letter.

    Each node can point to None or other children nodes.

    The size of a trie depends upon the number of characters. For example, in the English alphabet, there are 26 letters so the number of unique nodes cannot exceed 26.

    The depth of a trie depends on the longest word that it stores.

    Another important property of a trie is that it provides the same path for words which share a common prefix. For example, “there” and “their” have a common prefix “the.” Hence, they will share the same path till “e.” After that, the path will split into two branches. This is the backbone of the trie functionality.

'''

'''
The Trie Node Class #

The node of a trie represents a letter. For example, if you want to insert “hello” in the trie, we will need to add 5 nodes, one for each letter. A typical node in a trie consists of three data members:

    char: This stores the character in the node.
    children: An array which consists of pointers to children nodes. The size of this array depends on the size of the alphabet, which is 26 for English.
    is_end_word: A flag to indicate the end of a word. It is set to False by default and is only updated when a word ends during insertion. When this flag is True, the node is treated as a leaf.

'''

class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26  # This will store pointers to the children
        self.is_end_word = False  # true if the node represents the end of word
        self.char = char  # To store the value of a particular key

trie_node = TrieNode('a')
print(trie_node.char)

'''
The Trie will be implemented using the TrieNode class. As discussed above, a trie node represents one letter which keeps pointers to its children nodes. Each node can have at max 26 children if we are storing English words.

A root node is placed at the top and contains 26 pointers (one per letter). These pointers hold either None or another trie_node. The root is similar to the head_node from linked lists.

All the words are stored in a top-bottom manner. While storing the last character, we should always set the is_end_word flag as True to indicate the end of a word. This technique helps us in searching for a word to see if it even exists.

'''

from TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to insert a key in the Trie O{n}
    def insert(self, key):
        pass

    # Function to search a given key in Trie O{}
    def search(self, key):
        return False

    # Function to delete given key from Trie O{}
    def delete(self, key):
        pass


trie_node = TrieNode('a')
print(trie_node.char)

'''
The insertion process is fairly simple. For each character in the key, we check if it exists at the position we desire. If the character is not present, then we insert the corresponding trie node at the correct index in children. While inserting the last node, we also set the value of isEndWord to True.

There are three primary cases we need to consider during insertion

Case 1: No Common Prefix #

In this situation, we want to insert a word whose characters are not common with any other node path.

The illustration below shows the insertion of any in a trie which consists of only the.

We need to create nodes for all the characters of the word any as there is no common subsequence between any and the.

Case 2: Common Prefix #

This occurs when a portion of the starting characters of your word already in the trie starting from the root node.

For example, if we want to insert a new word there in the trie which consists of a word their, the path till the already exists. After that, we need to insert two nodes for r and e as shown below.

Case 3: Word Exists #

This occurs if your word is a substring of another word that already exists in the trie.

For example, if we want to insert a word the in the trie which already contains their, the path for the already exists. Therefore, we simply need to set the value of isEndWord to true at e in order to represent the end of the word for the as shown below.

'''

from TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of character 't'
    def get_index(self, t):
        return ord(t) - ord('a')

    # Function to insert a key in the Trie
    def insert(self, key):
        if key is None:
            return False  # None key

        key = key.lower()  # Keys are stored in lowercase
        current = self.root

        # Iterate over each letter in the key
        # If the letter exists, go down a level
        # Else simply create a TrieNode and go down a level
        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, "inserted")

            current = current.children[index]

        current.is_end_word = True
        print("'" + key + "' inserted")

    # Function to search a given key in Trie
    def search(self, key):
        return False

    # Function to delete given key from Trie
    def delete(self, key):
        pass


# Input keys (use only 'a' through 'z')
keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]

t = Trie()
print("Keys to insert:\n", keys)

# Construct Trie
for words in keys:
    t.insert(words)

'''
The function takes in a string key indicating a word. None keys are not allowed, and all keys are stored in lowercase.

To make things easier, we use the get_index() method to return the index of a character. The get_index method subtracts the ordinal value of ‘a’ from the character to return a numerical value in the range of 0 to 25.

To insert a key, we iterate over the characters in the key. For each character, we check if a TrieNode exists for it. If it does not exist, we insert a new TrieNode in the children array at the index returned by the get_index function. However, if a TrieNode already exists, we simply move on to the next character by setting our current node to the TrieNode at the character’s index.

Once we have iterated over all the letters, we mark the last node as leaf since the word has ended

'''

'''
If we want to check whether a word is present in the trie or not, we just need to keep tracing the path in the trie corresponding to the characters/letters in the word.

The logic isn’t too complex, but there are a few cases we need to take care of.

Case 1: Non-Existent Word #

If we are searching for a word that doesn’t exist in the trie and is not a subset of any other word, by principle, we will find None before the last character of the word can be found

Case 2: Word Exists as a Substring #

This is the case where our word can be found as a substring of another word, but the isEndWord property for it has been set to False.

In the example below, we are searching for the word be. It is a subset of the already existing word bed, but the e node has not been flagged as the end of a word. Hence, be will not be detected.

Case 3: Word Exists #

The success case is when there exists a path from the root to the node of the last character and the node is also marked as isEndWord:


'''

from TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of character 't'
    def get_index(self, t):
        return ord(t) - ord('a')

    # Function to insert a key in the Trie
    def insert(self, key):
        if key is None:
            return False  # None key

        key = key.lower()  # Keys are stored in lowercase
        current = self.root

        # Iterate over each letter in the key
        # If the letter exists, go down a level
        # Else simply create a TrieNode and go down a level
        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, "inserted")

            current = current.children[index]

        current.is_end_word = True
        print("'" + key + "' inserted")

    # Function to search a given key in Trie
    def search(self, key):
        if key is None:
            return False  # None key

        key = key.lower()
        current = self.root

        # Iterate over each letter in the key
        # If the letter doesn't exist, return False
        # If the letter exists, go down a level
        # We will return true only if we reach the leafNode and
        # have traversed the Trie based on the length of the key

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current is not None and current.is_end_word:
            return True

        return False

    # Function to delete given key from Trie
    def delete(self, key):
        pass


# Input keys (use only 'a' through 'z')
keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]
res = ["Not present in trie", "Present in trie"]

t = Trie()
print("Keys to insert: \n", keys)

# Construct Trie
for words in keys:
    t.insert(words)

# Search for different keys
print("the --- " + res[1] if t.search("the") else "the --- " + res[0])
print("these --- " + res[1] if t.search("these") else "these --- " + res[0])
print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])

'''
The function takes in a string key as an argument and returns True if the key is found. Otherwise, it returns False.

Much like the insertion process, None keys aren’t allowed and all characters are stored in lowercase.

Beginning from the root, we will traverse the trie and check if the sequence of characters is present. Another thing we need to make sure is that the last character node has the isEndWord flag set to True. Otherwise, we will fall into Case 2.
Time Complexity #

If the length of the word is hhh, the worst-case time complexity is O(h)O(h)O(h). In the worst case, we have to look at hhh consecutive levels of a trie for a character in the key being searched for. The presence or absence of each character from the key in the trie can be determined in O(1)O(1)O(1) because the size of the alphabet is fixed. Thus, the running time of search in a trie is O(h)O(h)O(h).

'''

'''
Deleting a Word in a Trie #

While deleting a node, we need to make sure that the node that we are trying to delete does not have any further child branches. If there are no branches, then we can easily remove the node.

However, if the node contains child branches, this opens up a few scenarios

Case 1: Word with No Suffix or Prefix #

If the word to be deleted has no suffix or prefix and all the character nodes of this word do not have any other children, then we will delete all these nodes up to the root.

However, if any of these nodes have other children (are part of another branch), then they will not be deleted. This will be explained further in Case 2.

In the figure below, the deletion of the word bat would mean that we have to delete all characters of bat

Case 2: Word is a Prefix #

If the word to be deleted is a prefix of some other word, then the value of is_end_word of the last node of that word is set to False and no node is deleted.

For example, to delete the word the, we will simply unmark e to show that the word doesn’t exist anymore.

Case 3: Word Has a Common Prefix #

If the word to be deleted has a common prefix and the last node of that word does not have any children, then this node is deleted along with all the parent nodes in the branch which do not have any other children and are not end characters.

Take a look at the figure below. In order to delete their, we’ll traverse the common path up to the and delete the characters i and r.

'''

from TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of character 't'
    def get_index(self, t):
        return ord(t) - ord('a')

    # Function to insert a key in the Trie
    def insert(self, key):
        if key is None:
            return False  # None key

        key = key.lower()  # Keys are stored in lowercase
        current = self.root

        # Iterate over each letter in the key
        # If the letter exists, go down a level
        # Else simply create a TrieNode and go down a level
        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, "inserted")

            current = current.children[index]

        current.is_end_word = True
        print("'" + key + "' inserted")

    # Function to search a given key in Trie
    def search(self, key):
        if key is None:
            return False  # None key

        key = key.lower()
        current = self.root

        # Iterate over each letter in the key
        # If the letter doesn't exist, return False
        # If the letter exists, go down a level
        # We will return true only if we reach the leafNode and
        # have traversed the Trie based on the length of the key

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current is not None and current.is_end_word:
            return True

        return False

    # Recursive function to delete given key
    def delete_helper(self, key, current, length, level):
        deleted_self = False

        if current is None:
            print("Key does not exist")
            return deleted_self

        # Base Case:
        # We have reached at the node which points
        # to the alphabet at the end of the key
        if level is length:
            # If there are no nodes ahead of this node in
            # this path, then we can delete this node
            print("Level is length, we are at the end")
            if current.children.count(None) == len(current.children):
                print("- Node", current.char, ": has no children, delete it")
                current = None
                deleted_self = True

            # If there are nodes ahead of current in this path
            # Then we cannot delete current. We simply unmark this as leaf
            else:
                print("- Node", current.char, ": has children, don't delete \
                it")
                current.is_end_word = False
                deleted_self = False

        else:
            index = self.get_index(key[level])
            print("Traverse to", key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(
                key, child_node, length, level + 1)
            # print( "Returned from", key[level] , "as",  child_deleted)
            if child_deleted:
                # Setting children pointer to None as child is deleted
                print("- Delete link from", current.char, "to", key[level])
                current.children[index] = None
                # If current is a leaf node then
                # current is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current.is_end_word:
                    print("- - Don't delete node", current.char, ": word end")
                    deleted_self = False

                # If child_node is deleted and current has more children
                # then current must be part of another key
                # So, we cannot delete current Node
                elif current.children.count(None) != len(current.children):
                    print("- - Don't delete node", current.char, ": has \
                    children")
                    deleted_self = False

                # Else we can delete current
                else:
                    print("- - Delete node", current.char, ": has no children")
                    current = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            print("None key or empty trie error")
            return
        print("\nDeleting:", key)
        self.delete_helper(key, self.root, len(key), 0)


# Input keys (use only 'a' through 'z')
keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]
res = ["Not present in trie", "Present in trie"]

t = Trie()
print("Keys to insert: \n", keys)

# Construct Trie
for words in keys:
    t.insert(words)

# Search for different keys
print("the --- " + res[1] if t.search("the") else "the --- " + res[0])
print("these --- " + res[1] if t.search("these") else "these --- " + res[0])
print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])

# Delete abc
t.delete("abc")
print("Deleted key \"abc\" \n")

print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])

'''
The delete function takes in a key of type string and then checks if either the trie is empty or the key is None. For each case, it simply returns from the function.

delete_helper() is a recursive function to delete the given key. Its arguments are a key, the key’s length, a trie node (root at the beginning), and the level (index) of the key.

It goes through all the cases explained above. The base case for this recursive function is when the algorithm reaches the last node of the key:

At this point, we check if the last node has any further children or not. If it does, then we simply unmark it as an end word. On the other hand, if the last node doesn’t contain any children, all we have to do is to set the parameter deleted_self to True to mark this node for deletion.
Time Complexity #

If the length of the word is h, the worst-case time complexity is O(h). 
In the worst case, we have to look at hhh consecutive levels of a trie for a character in the key being searched for.
The presence or absence of each character from the key in the trie can be determined in O(1) because the size of the alphabet is fixed.
Subsequently, in the worst case, we may have to delete hhh nodes from the trie. Thus, the running time of delete in a trie is O(h).

'''


'''
Challenge 1
Implement the total_words() function which will find the total number of words in a trie.

Input #

The root node of a trie.

Sample Input #

keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]


Output #

Returns total number of words in a trie.

O(n)
'''
from Trie import Trie
from TrieNode import TrieNode


# TrieNode => {children, is_end_word, char}
def total_words(root):
	result = 0

	# Leaf denotes end of a word
	if root.is_end_word:
		result += 1

	for letter in root.children:
		if letter is not None:
			result += total_words(letter)
	return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()

for key in keys:
    trie.insert(key)

print(total_words(trie.root))

'''
Challenge 2
You have to implement the find_words() function which will return a sorted list of all the words stored in a trie.

Input #

The root node of a trie.
Output #

A sorted list of all the words stored in a trie.
Sample Input #

keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]

Sample Output #

["a", "abc", "answer", "any", "by", "bye", "the", "their", "there"] // Sorted alphabetically

'''
from Trie import Trie
from TrieNode import TrieNode


# Create Trie => trie = Trie()
# TrieNode => {children, is_end_word, char}
# Insert a Word => trie.insert(key)
# Search a Word => trie.search(key) return true or false
# Delete a Word => trie.delete(key)
# Recursive Function to generate all words
# The find_words(root) function contains a result list which will contain all the words in the trie. word is a character array in which node characters are added one by one to keep track of all the letters in the same recursive call.

# get_words() is our recursive function which begins from the root and traverses every node. Whenever a node is the end of a word, temp(containing the character array) is converted into a string and inserted into result.

# Since word cannot be reset before recording every new word, we simply update the values at each index using level.
# Time Complexity #

# As the algorithm traverses all the nodes, its run time is O(n) where n is the number of nodes in the trie.

def get_words(root, result, level, word):

    # Leaf denotes end of a word
    if root.is_end_word:
        # current word is stored till the 'level' in the character array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(str(temp))

    for i in range(26):
        if root.children[i]:
            # Non-None child, so add that index to the character array
            word[level] = chr(i + ord('a'))  # Add character for the level
            get_words(root.children[i], result, level + 1, word)


def find_words(root):
    result = []
    word = [None] * 20  # assuming max level is 20
    get_words(root, result, 0, word)
    return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
t = Trie()
for i in range(len(keys)):
    t.insert(keys[i])
lst = find_words(t.root)
print(str(lst))

'''
Challenge 3
implement the sort_list() function which will sort the elements of a list of strings.

Input #

A list of strings.
Output #

Returns the input list in a sorted state.
Sample Input #

keys = ["the", "a", "there", "answer", "any",
                     "by", "bye", "their","abc"]

Sample Output #

['a', 'abc','answer','any','by','bye','the','their','there']

This exercise is very similar to Challenge 2, except the fact that you have to create the trie yourself.

Since the children list for each node stores letters in alphabetical order, the tree itself is ordered from top to bottom. All we need to do is make a pre-order traversal (think of a as the left most child and z as the right most child) and store the words in a list just like we did in the previous challenge.
Time Complexity #

We first insert the nodes into the graph and then traverse all the existing nodes. Hence, the bottleneck worst case time complexity is O(n).

'''
from Trie import Trie
from TrieNode import TrieNode
# Recursive Function to generate all words in alphabetic order


def get_words(root, result, level, word):
    # Leaf denotes end of a word
    if (root.is_end_word):
        # current word is stored till the 'level' in the character array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(temp)

    for i in range(26):
        if (root.children[i] is not None):
            # Non-null child, so add that index to the character array
            word[level] = chr(i + ord('a'))
            get_words(root.children[i], result, level + 1, word)


def sort_list(arr):
    result = []

    # Creating Trie and Inserting words from array
    trie = Trie()
    for word in arr:
        trie.insert(word)

    word = [''] * 20
    get_words(trie.root, result, 0, word)
    return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
print(sort_list(keys))

'''
Challenge 4
implement the is_formation_possible() function which will find whether a given word can be formed by combining two words from a dictionary. We assume that all words are in lower case.
Input #

A dictionary and a query word containing lowercase characters.
Output #

Returns True if the given word can be generated by combining two words from the dictionary.
Sample Input #

dictionary = ["the", "hello", "there", "answer", "any", "by", "world", "their", "abc"]
word = "helloworld"

Sample Output #

True
'''
from Trie import Trie
from TrieNode import TrieNode


def is_formation_possible(dct, word):

    # Create Trie and insert dctionary elements in it
    trie = Trie()
    for elem in dct:
        trie.insert(elem)

    # Get Root
    current = trie.root

    # Iterate all the letters of the word
    for i in range(len(word)):
        # get index of the character from Trie
        char = trie.get_index(word[i])

        # if the prefix of word does not exist, word would not either
        if current.children[char] is None:
            return False

        # if the substring of the word exists as a word in trie,
        # check whether rest of the word also exists,
        # if it does return true
        elif current.children[char].is_end_word:
            if trie.search(word[i+1:]):
                print(word[:i + 1], word[i+1:])
                return True

        current = current.children[char]

    return False


keys = ["the", "hello", "there", "answer",
        "any", "educative", "world", "their", "abc"]
print(is_formation_possible(keys, "helloworld"))

'''
The algorithm can be divided into three parts. The first and simplest part is making a trie for the words in the dictionary.

The second part is to check if there is a word in the trie which can become a prefix for the query word. In the case of “helloworld”, we can find “hello” in the trie. Since there can be multiple prefixes of a word, we have to check for every such prefix. As we iterate through the trie, looking for prefix, whenever we find a prefix that exists as a word in the trie, we lookup the remaining word in the trie using the search function. If this substring exists we have found a solution

Time Complexity #

We perform the insert operation m times for a dictionary of size m. After that, the search operation runs on the word in the sequence:

"h", "he", "hel", "hell"...

If the size of the word is n, the complexity for this turns out to be n2. Hence, the total time complexity is O(m + n2)
'''