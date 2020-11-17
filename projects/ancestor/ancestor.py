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
