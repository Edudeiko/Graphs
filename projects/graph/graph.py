"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

'''
BFS/DFS vs BFT/BFT
When is DFS better?
- might find the longest path
- if the node you're looking for is a leaf
- can also be implemented recusively, or randomly

When is BFS better?
- finds shortest path
'''


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            print(f'Vertex --> {v1} does not exist')
        elif v2 not in self.vertices:
            print(f'Vertex --> {v2} does not exist')
        else:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        uses Queue data structure
        """
        # make a queue
        q = Queue()

        # make a set to track which vertex we have visited
        visited = set()

        # enqueue the starting vertex
        q.enqueue(starting_vertex)

        # loop while the queue isn not empty
        while q.size() > 0:
            # dequeue, this is our current vertex
            current_vertex = q.dequeue()

            # check if we've yet visited
            if current_vertex not in visited:

                # if not, we go to the vertex
                # mark as visited == add to visited set
                visited.add(current_vertex)
                print(current_vertex)

                # assign the neighbours
                neighbors = self.get_neighbors(current_vertex)
                # iterate over the neighbors, enqueue them
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        uses Stack data structure
        """
        # make a stack
        stack = Stack()

        # make a set to track visited
        visited = set()  # O(1)

        # put the start node into the stack
        stack.push(starting_vertex)

        # while the stack is not empty
        while stack.size() > 0:
            # pop off the top of the stack, this is our current vertex
            current_node = stack.pop()

            # check if have visited this vertex yet
            if current_node not in visited:

                # if not, add it to our visited set
                visited.add(current_node)
                print(current_node)

                # and add each of its neighbors to our stack
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, vertex, visited=None):  # visited=set()
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        # need base case

        # needs to call itself
        """
        # can replace it with visited=set() instead of visited=None
        if visited is None:
            visited = set()

        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            neighbors = self.get_neighbors(vertex)
            # if len(neighbors) == 0:
            #     return

            # else:
            for neighbor in neighbors:
                # if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.

        1. stop when we find the target node

        2. return the path we took to get there
        - note, this will automatically be the shortest path

        Enqueue a PATH TO the starting node, instead of just the starting node
        """
        # create Queue
        queue = Queue()
        # enqueue starting node
        queue.enqueue([starting_vertex])

        visited = set()

        # while the path is not Empty
        while queue.size() > 0:
            # dequeue current vertex at the front of line
            current_path = queue.dequeue()

            if current_path[-1] not in visited:

                visited.add(current_path[-1])
                # print(current_path)

                # check if we have found our target node
                if current_path[-1] == destination_vertex:
                    return current_path

                # get the neighbours
                neighbors = self.get_neighbors(current_path[-1])

                # iterate over the neighbors, enqueue the PATH to them
                for neighbor in neighbors:

                    # add to queue
                    new_path = current_path + [neighbor]
                    # new_path = [*current_path, neighbor]
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()

        stack.push([starting_vertex])

        visited = set()

        while stack.size() > 0:

            current_path = stack.pop()

            if current_path[-1] not in visited:
                visited.add(current_path[-1])

            if current_path[-1] == destination_vertex:
                return current_path

            neighbors = self.get_neighbors(current_path[-1])
            for neighbor in neighbors:
                new_path = current_path + [neighbor]
                stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        # def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # stack = Stack()
        # stack.push([starting_vertex])
        # visited = set()

        # while stack.size() > 0:
        #     current_path = stack.pop()
        #     if current_path[-1] not in visited:
        #         visited.add(current_path[-1])

        #     if current_path[-1] == destination_vertex:
        #         return current_path

        #     neighbors = self.get_neighbors(current_path[-1])
        #     for neighbor in neighbors:
        #         new_path = [*current_path, neighbor]
        #         stack.push(new_path)

        if len(path) == 0:
            path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        if starting_vertex not in visited:
            visited.add(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)

            for ii in neighbors:
                final_path = path + [ii]

            # only return if we found the destination_vertex
                result = self.dfs_recursive(ii, destination_vertex, final_path, visited)
                if result is not None:
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
