'''
Describe the problem in graphs terms
- Ehat are our nodes?
- What aer our edges? aka when are two nodes connected?

-- Is this a directed or undirected graph? cyclic or acyclic?

DAG: directed acycling graph, from parent to child or from child to parent

2. Build our graph, or write getNeighbor

3. Choose your fighter, which algorithm to use?
- any traversal, depth or breadth
'''


def earliest_ancestor(ancestors, starting_node):
    # create dict to store the result
    parent_child_dict = dict()
    # parent_child_dict = {} same as the above

    # iterate through the ancestors
    for v1_parent, v2_child in ancestors:  # for ii in ancestors:

        if v2_child not in parent_child_dict:  # child = ii[1]

            parent_child_dict[v2_child] = set([v1_parent])  # {ii[0]} parent = ii[0]
        else:

            parent_child_dict[v2_child].add(v1_parent)

    stack = []
    parents = []

    stack.append([starting_node])

    while len(stack) > 0:
        current_path = stack.pop()

        if current_path[-1] not in parent_child_dict:

            if len(current_path) > len(parents):
                parents = current_path
            continue

        for ii in parent_child_dict[current_path[-1]]:
            path = (current_path + [ii])
            stack.append(path)

    if parents[-1] == starting_node:
        return -1

    return parents[-1]


def earliest_ancestor_recursive(ancestors, starting_node):
    # loop through parent&child pair in the ancestor tree
    for parent, child in ancestors:

        # if the starting_node is the current child
        if child == starting_node:

            # find the earliest ancestor of it's parent
            earliest_ancestor = earliest_ancestor_recursive(ancestors, parent)

            # if the parent has no ancestors
            if earliest_ancestor == -1:

                # return the parent
                return parent

            # or return earliest_ancestor
            return earliest_ancestor

    # return -1 if child has no ancestors
    return -1

# write a getNeighbors function
# iterate over the pairs of nodes
# find those that are direct parents of this node

# run a standard DFT, but recurse with distance to track the earliest ancestor found
'''
def dft(ancestors, node, distance)
​
    parents = getNeighbors(node)
​
    if len(parents) == 0:
        return (node, distance)
​
    ancient_one = (node, distance)
    for parent in parents:
        node_pair = dft(ancestors, parent, distance + 1)
​
        if node_pair[1] > distance:
            ancient_one = node_pair
        if node_pair[1] == ancient_one[1] and node_pair[0] < ancient_one[0]:
            ancient_one = node_pair
​
    return ancient_one
​
def earliest_ancestor(ancestors, starting_node):
    # call BFT or DFT
    ancient_one = dft(ancestors, starting_node, 0)
​
    # if the earliest ancestor returned is the same as the starting node, return -1
'''
