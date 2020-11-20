from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"  # BFT find shortest path

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())

world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# n,n,s,s,s,s,n,n,e,e,w,w,w,w
traversal_path = []
moves = []
visited = set()

graph = {
    0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}

vice_versa = {
    'n': 's',
    'e': 'w',
    's': 'n',
    'w': 'e'
}


while len(graph) < 500:
    '''
    You know you are done when you have exactly 500 entries
    (0-499) in your graph
    '''

    exits = player.current_room.get_exits()

    if len(traversal_path) == 0:
        direction = exits[random.randint(0, len(exits) - 1)]

    else:
        while True:
            direction = exits[random.randint(0, len(exits) - 1)]

            # if not direction not in vice_versa and not visited
            if direction != vice_versa[traversal_path[-1]]:
                break

    # previous room
    prev_room = player.current_room.id

    # add to traversal_path, moves, visited
    traversal_path.append(direction)
    moves.append(direction)
    visited.add(player.current_room.id)

    # Player moves
    print(f'move: {direction}')
    player.travel(direction)

    # current room
    current_room = player.current_room.id

    graph[prev_room][direction] = player.current_room.id
    # check if room has been visited
    if current_room not in visited:
        exits = player.current_room.get_exits()
        graph[current_room] = {}
        '''
        Instead of searching for a target vertex,
        you are searching for an exit with a `'?'` as the value
        '''
        for ii in exits:
            graph[current_room][ii] = '?'

    graph[current_room][vice_versa[direction]] = prev_room
    print(f'room: {current_room}')
    print(graph[current_room])









# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")


################
# {0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
# 1: [(3, 6), {'s': 0, 'n': 2}],
# 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}]}  
# what does the first elements of the array mean? (3, 5)
# -- This is a coordinate for the room used when building the graph, which functions as an ID
# -- It is entirely useless to you and you can ignore it

# Dijkstra's Algorithm
# - can we run BFS on a weighted graph?
# -- what if we convert each mile to a node? now the graph is unweighted
# -- that will work but your graph now consumes huge amounts of memory
# - greedy algorithm
# - take the next shortest overall step
# - uses a heap to make finding next shortest step faster

# A*
# - finding directions
# - includes heuristics aka tricks to get around obstacles
# "intuition" "explanation" "intuitive approach"
# Arrays, hash tables, trees
# How to randomly choose the next step? Something like this maybe:
# {
#   0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
#   5: {'n': 0, 's': '?', 'e': '?'}
# }
# choices = []
# for key, value in my_graph[0].items():
#   if value == '?':
#       choices.append(key)
# random.choice(choices)
# # maybe list comprehension?? Will this comprehension work? idk I haven't tested it
# choices = [value for key, value in my_graph.items() if value == '?']
###################
