'''
A graph is a set of nodes that are connected to each other in the form of a network. 
First of all, we’ll define the two basic components of a graph.

Vertex #

    A vertex is the most essential part of a graph. A collection of vertices forms a graph. In that sense, vertices are similar to linked list nodes.

Edge #

    An edge is the link between two vertices. It can be uni-directional or bi-directional depending on your graph. An edge can also have a cost associated with it (will be discussed in detail later).



    Degree of a Vertex: The total number of edges incident on a vertex. There are two types of degrees:

        In-Degree: The total number of incoming edges of a vertex.

        Out-Degree: The total number of outgoing edges of a vertex.

    Parallel Edges: Two undirected edges are parallel if they have the same end vertices. Two directed edges are parallel if they have the same starting and ending vertices.

    Self Loop: This occurs when an edge starts and ends on the same vertex.

    Adjacency: Two vertices are said to be adjacent if there is an edge connecting them directly.

In an undirected graph, the edges are bi-directional. For e.g., an ordered pair (2, 3) shows that there exists an edge between vertex 2 and 3 without any specific direction. You can go from vertex 2 to 3 or from 3 to 2.

the maximum possible edges of a graph with n vertices will be n(n−1)/2.

In a directed graph, the edges are unidirectional. For a pair (2, 3), there exists an edge from vertex 2 towards vertex 3 and the only way to traverse is to go from 2 to 3, not the other way around.

If you have n vertices, then all the possible edges become n*(n-1).

The two most common ways to represent a graph are:

    Adjacency Matrix
    Adjacency List

The adjacency matrix is a two-dimensional matrix where each cell can contain a 0 or 1. If a cell contains 1, there exists an edge between the corresponding vertices

An array of linked lists is used to store all the edges in the graph. The size of the array is equal to the number of vertices in the graph. Each index of the array contains a vertex. This vertex points to a linked list that contains all the vertices connected to this one.

implementation based on the adjacency list: linked list class will be used to represent adjacent vertices.

Graph class consists of two data members:

    The total number of vertices in the graph
    A list of linked lists to store adjacent vertices

Adjacency List #

    Adding an edge in adjacency lists takes constant time as we only need to insert at the head node of the corresponding vertex.

    Removing an edge takes O(E) time because, in the worst case, all the edges could be at a single vertex and hence, we would have to traverse all E edges to reach the last one.

    Removing a vertex takes O(V + E) time because we have to delete all its edges and then reindex the rest of the list one step back in order to fill the deleted spot.

    Searching an edge between a pair of vertices can take up to O(V) if all V nodes are present at a certain index and we have to traverse them.

Adjacency Matrix #

    Edge operations are performed in constant time as we only need to manipulate the value in the particular cell.

    Vertex operations are performed in O(V2) since we need to add rows and columns. We will also need to fill all the new cells.

    Searching an edge is O(1) because we can access each edge by indexing.

'''
from LinkedList import LinkedList

class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # definining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.array = []
        # Creating a new Linked List for each vertex/index of the list
        for i in range(vertices):
            self.array.append(LinkedList())

    # Function to add an edge from source to destination
    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
            self.array[source].insert_at_head(destination)
            # Uncomment the following line for undirected graph 
            # self.array[destination].insert_at_head(source)

        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")


#BFS
from Graph import Graph
from Queue import Queue
from Stack import Stack


def bfs_traversal_helper(g, source, visited):
    result = ""
    # Create Queue(implemented in previous lesson) for Breadth First Traversal
    # and enqueue source in it
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True # Mark as visited
    # Traverse while queue is not empty
    while not queue.is_empty():
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True  # Visit the current Node
            temp = temp.next_element
    return result, visited

def bfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices is 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = bfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result
    
if __name__ == "__main__" :
    g = Graph(4)
    num_of_vertices = g.vertices
    if num_of_vertices is 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        print(bfs_traversal(g, 0))

#DFS
from Graph import Graph
from Stack import MyStack
# You can check the input graph in console tab

def dfs_traversal_helper(g, source, visited):
    result = ""
    # Create Stack(Implemented in previous lesson) for Depth First Traversal
    # and Push source in it
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    # Traverse while stack is not empty
    while not stack.is_empty() :
        # Pop a vertex/node from stack and add it to the result
        current_node = stack.pop()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the array,
        # and if they are not already visited then push them in the stack
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                stack.push(temp.data)
                # Visit the node
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited  # For the above graph it should return "12453"

def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices is 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = dfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return result

if __name__ == "__main__" :
    g = Graph(7)
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        print("Graph is empty")
    elif num_of_vertices < 0:
        print("Graph cannot have negative vertices")
    else:
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(2, 5)
        g.add_edge(3, 6)
        print(dfs_traversal(g, 1))
        

#Detect cycle
from Graph import Graph
# We only need Graph and Stack for this Challenge!

def detect_cycle(g):
    # visited list to keep track of the nodes that have been visited
    # since the beginning of the algorithm
    visited = [False] * g.vertices
    # rec_node_stack keeps track of the nodes which are part of
    # the current recursive call
    rec_node_stack = [False] * g.vertices
    for node in range(g.vertices):
        # DFS recursion call
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True
    return False

def detect_cycle_rec(g, node, visited, rec_node_stack):
    # Node was already in recursion stack. Cycle found.
    if rec_node_stack[node]:
        return True
    # It has been visited before this recursion
    if visited[node]:
        return False
    # Mark current node as visited and
    # add to recursion stack
    visited[node] = True
    rec_node_stack[node] = True
    head_node = g.array[node].head_node
    while head_node is not None:
        # Pick adjacent node and call it recursively
        adjacent = head_node.data
        # If the node is visited again in the same recursion => Cycle found
        if detect_cycle_rec(g, adjacent, visited, rec_node_stack):
            return True
        head_node = head_node.next_element
    # remove the node from the recursive call
    rec_node_stack[node] = False
    return False

if __name__ == "__main__" :
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(3, 0)
    
    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(detect_cycle(g1))
    print(detect_cycle(g2))

#Find mother vertex in dir. graph
from Graph import Graph
from Stack import MyStack
# We only need Graph and Stack for this question!


def find_mother_vertex(g):
    # visited[] is used for DFS. Initially all are
    # initialized as not visited
    visited = [False]*(g.vertices)
    # To store last finished vertex (or mother vertex)
    last_v = 0
    # Do a DFS traversal and find the last finished
    # vertex
    for i in range(g.vertices):
        if not visited[i]:
            perform_DFS(g, i, visited)
            last_v = i

    # If there exist mother vertex (or vetices) in given
    # graph, then v must be one (or one of them)

    # Now check if v is actually a mother vertex (or graph
    # has a mother vertex). We basically check if every vertex
    # is reachable from v or not.

    # Reset all values in visited[] as false and do
    # DFS beginning from v to check if all vertices are
    # reachable from it or not.
    visited = [False]*(g.vertices)
    perform_DFS(g, last_v, visited)
    if any (not i for i in visited): # any() func iterates over a list
        return -1
    else:
        return last_v

# A recursive function to print DFS starting from v
def perform_DFS(g, node, visited):
    # Mark the current node as visited and print it
    visited[node] = True
    # Recur for all the vertices adjacent to this vertex
    temp = g.array[node].head_node
    while temp:
        if not visited[temp.data]:
            perform_DFS(g, temp.data, visited)
        temp = temp.next_element

if __name__ == "__main__" :
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    print(find_mother_vertex(g))

#Count Number of Edges in an Undirected Graph
from Graph import Graph
# We only need Graph for this Question!


def num_edges(g):
    # For undirected graph, just sum up the size of
    # all the adjacency lists for each vertex
    return sum([g.array[i].length() for i in range(g.vertices)]) // 2

if __name__ == "__main__" :

    g = Graph(9)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(5, 3)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    g.add_edge(6, 4)
    g.add_edge(7, 8)

    g2 = Graph(7)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(3, 4)
    g2.add_edge(3, 5)
    g2.add_edge(2, 5)
    g2.add_edge(2, 4)
    g2.add_edge(4, 6)
    g2.add_edge(4, 5)
    g2.add_edge(6, 5)

    print(num_edges(g))

    print(num_edges(g2))


#Check if a Path Exists Between Two Vertices
from Graph import Graph
from Queue import MyQueue
# We only need Graph and Queue for this Question!

def check_path(g, source, dest):
    # BFS to check path between source and dest
    # Keep track of visited vertices
    visited = [False]*(g.vertices)

    # Create a queue for BFS
    queue = MyQueue()

    # Enque source and mark it as visited
    queue.enqueue(source)
    visited[source] = True

    # Loop to traverse the whole graph using BFS
    while not queue.is_empty():

        node = queue.dequeue()

        # Check if dequeued node is the destination
        if node is dest:
            return True

        # Continue BFS by obtaining first element in linked list
        adjacent = g.array[node].head_node
        while adjacent:
            # enqueue adjacent node if it has not been visited
            if not visited[adjacent.data]:
                queue.enqueue(adjacent.data)
                visited[adjacent.data] = True
            adjacent = adjacent.next_element

    # Destination was not found in the search
    return False


if __name__ == "__main__" :

    g1 = Graph(9)
    g1.add_edge(0, 2)
    g1.add_edge(0, 5)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(5, 3)
    g1.add_edge(5, 6)
    g1.add_edge(3, 6)
    g1.add_edge(6, 7)
    g1.add_edge(6, 8)
    g1.add_edge(6, 4)
    g1.add_edge(7, 8)
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)

    print(check_path(g1, 0, 7))
    print(check_path(g2, 3, 0))


#Check if a Given Undirected Graph is Tree or not?
from Graph import Graph
# We only need Graph for this Question!


def is_tree(g):
    # All vertices unvisited
    visited = [False] * g.vertices

    # Check cycle using recursion stack
    # Also mark nodes visited to check connectivity
    if check_cycle(g, 0, visited, -1):
        return False

    # Check if all nodes we visited from the source (graph is connected)
    for i in range(len(visited)):
        # Graph is not connected
        if not visited[i]:
            return False
    # Not cycle and connected graph
    return True


def check_cycle(g, node, visited, parent):
    # Mark node as visited
    visited[node] = True

    # Pick adjacent node and run recursive DFS
    adjacent = g.array[node].head_node
    while adjacent:
        if not visited[adjacent.data]:
            if check_cycle(g, adjacent.data, visited, node):
                return True

        # If adjacent is visited and not the parent node of the current node
        elif adjacent.data is not parent:
            # Cycle found
            return True
        adjacent = adjacent.next_element

    return False

if __name__ == "__main__" :

    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print(is_tree(g))

#Find the Shortest Path Between Two Vertices
from Graph import Graph
from Queue import MyQueue
# We only need Graph and Queue for this Question!


def find_min(g, a, b):
    result = 0
    num_of_vertices = g.vertices
    # A list to hold the history of visited nodes (by default all false)
    # Make a node visited whenever you enqueue it into queue
    visited = [False] * num_of_vertices

    # For keeping track of distance of current_node from source
    distance = [0] * num_of_vertices

    # Create Queue for Breadth First Traversal and enqueue source in it
    queue = MyQueue()
    queue.enqueue(a)
    visited[a] = True
    # Traverse while queue is not empty
    while not queue.is_empty():
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        # and also update their distance from `a`
        # by adding 1 in current_nodes's distance
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data] or temp.data is b:
                queue.enqueue(temp.data)
                visited[temp.data] = True
                distance[temp.data] = distance[current_node] + 1
                if temp.data is b:
                    return distance[b]
            temp = temp.next_element
    # end of while
    return -1

if __name__ == "__main__" :

    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 5)
    g.add_edge(2, 5)
    g.add_edge(5, 6)
    g.add_edge(3, 6)

    print(find_min(g, 1, 5))


#Remove Edge
from Graph import Graph
# We only need Graph for this Question!


def remove_edge(graph, source, dest):
    # If empty graph
    if len(graph.array) == 0:
        return graph
    # check if source valid
    if source >= len(graph.array) or source < 0:
        return graph
    # check if dest valid
    if dest >= len(graph.array) or dest < 0:
        return graph
    # Delete by calling delete on head of LinkedList
    # Note: the delete method caters for if the edge does not exist
    graph.array[source].delete(dest)
    return graph

if __name__ == "__main__" :

    g = Graph(5)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(4, 0)

    g.print_graph()

    remove_edge(g, 1, 3)

    g.print_graph()
