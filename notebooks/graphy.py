#  Singly Linked List
class ListNode:
    def __init__(self, value):
        self.value = value

        self.next = None

        # self.prev if DLL

# LL traversal
current = node
while current is not None:
    current = current.next


class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value

        self.left = None
        self.right = None

# BST traversal
## DFT, BFT
### Stack, Queue

while node is not None:
    recursed(self.left)
    recursed(self.right)

class GraphNode:
    def __init__(self, value):
        self.value = 'B'

        # options: dictionary, array, set
        # B's connections
        self.connections = set('A', 'C', 'D')

        # A's connections
        self.connections = set('B')

        # D's connections - Billy no mates
        self.connections = set()


# outbound vs inbound connections?

# Graph termonology for 2-way vs 1-way connections
## undirected graph vs directed graph
## (FB, LinkedIn) vs (Instagram, Twitter, TikTok)


## Graph Traversals

## Depth First Traversal, stack
### Check every node once, check every connection once

# make a stack
stack = Stack(3, 6)
# make a set to track visited
visited = set(1, 2, 4)  # O(1)

# visited = ['A']  # O(n) do not use

# put the start node into the stack

# while the stack is not empty

# pop off the top of the stack, this is current our node
current_node = 7

## check if have visited this node yet
### if not, add it our visited set
### and add each of its neighbors to our stack

## Time complexity?
### How many times did we visit each node? once
### How many times did we check each connection? once

## O(number of nodes + number of connections)
### O(n + n)
## so linear!

https://slack-imgs.com/?c=1&o1=ro&url=https%3A%2F%2Fraw.githubusercontent.com%2FLambdaSchool%2FGraphs%2Fmaster%2Fobjectives%2Fgraph-representations%2Fimg%2Fsample-graph.PNG

# BFT, queue
q = Queue('D', 'C')

# make a set to track visited
visited = set('A', 'B')

# enqueue the start node

# while our queue is not empty

## dequeue from front of line, this is our current node
current_node = 'C'

## check if we've visited here yet
### if not, add to visited
### get its neighbours, for each, add to queue
neighbours = set('C', 'D')

# Time complexity?
## visit every vertex once, visit every edge once
## O(n + N)
## O(node + edge)
