import random
from collections import deque
from queue import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0  # current number of users
        self.users = {}  # your users with their attributes
        self.friendships = {}  # adjacency list (smezhnost)

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        '''random.shaffle(x)'''
        for ii in range(0, len(l)):
            random_index = random.randint(ii, len(l) - 1)
            l[random_index], l[ii] = l[ii], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # if 1 is a friend of 2, and 2 is a friend of 1, count as 2 friendships
        total_friendships = avg_friendships * num_users

        #############################################
        frienships_made = 0

        while frienships_made < total_friendships:
            # choose two random user ids
            first_user = random.randint(1, num_users)
            second_user = random.randint(1, num_users)
            # try to make the friendship
            new_friendship = self.add_friendship(first_user, second_user)

            if new_friendship:
                frienships_made += 2

        #############################################
        # create a list with all possible friendship combinations,
        # friendship_combos = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        friendship_combos = []

        for user_id in range(1, num_users + 1):
            # you can avoid this by only creating friendships where user_1 < user_2
            for friend_id in range(user_id + 1, num_users + 1):
                friendship_combos.append((user_id, friend_id))

        # shuffle the list
        self.fisher_yates_shuffle(friendship_combos)

        # then grab the first N elements from the list
        friendships_to_make = friendship_combos[:(total_friendships // 2)]

        for friendship in friendships_to_make:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        BFS approach -- guarantees a shortest path

        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Instead of using a `set` to mark users as visited, you could use a
        # `dictionary`. Similar to sets, checking if something is in a
        # dictionary runs in O(1) time. If the visited user is the key,
        # what would the value be?

        # track the network
        visited = {}  # Note that this is a dictionary, not a set

        # create a starting point
        current_path = [user_id]

        q = deque([current_path])

        while q:
            # return and remove the leftmost item.
            # if no elements are present, raise an IndexError
            current_path = q.popleft()

            # last friend from q
            last_friend_q = current_path[-1]

            # check if it is not in visited
            if last_friend_q not in visited:
                # add last_friend form queue and current path to visited
                visited[last_friend_q] = current_path

                # itirate and add other friends to visited
                for friend in self.friendships[last_friend_q]:

                    # add friend to copy_path, add to the queue
                    copy_path = current_path + [friend]
                    q.append(copy_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)


# def get_all_social_paths(self, user_id):
#     '''
#     "wait wait don't tell me" --> "ah ha!"

#     Choose your fighter: BFS
#     '''
#     q = Queue()
#     # key: user_id, value: path
#     visited = {}  # Note that this is a dictionary, not a set

#     q.enqueue([user_id])

#     while q.size() > 0:
#         # get the next person in line
#         current_path = q.dequeue()
#         current_person = current_path[-1]
#         # check if we've visited them yet
#         if current_person not in visited:
#             # if not, mark as visited
#             # key: user_id, value: path
#             visited[current_person] = current_path
#             # get their friends (visited their edges)
#             friends = self.friendships(current_person)

#             for friend in friends:
#                 friend_path = list(current_path)

#                 friend_path.append(friend)

#                 q.enqueue(friend_path)

#     return visited

# percentage of other users in extended social network
    # number of people we visited / total number of people
    print(len(connections) / num_users)

# avg degree of separation --> average steps we took to visit someone
# just average the length of each path
    total_path_length = 0
    for key, value in connections.items():
        total_path_length += len(value)

    average_path_length = total_path_length / len(connections)
    print(average_path_length)
