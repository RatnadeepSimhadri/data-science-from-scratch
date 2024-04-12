users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# Empty Dictionary to Track all First Degree Connections for Each User. This dictionary is a graphical 
# representation of Users and connections as an Adjacency List
friendships = { user["id"]:[] for user in users}

for i,j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
    

# Given an User ID Length of an Adjacency List gives Num of Connections for Each User
def num_of_friends(user):
    friends = friendships[user["id"]]
    return len(friends)

total_connections = sum(num_of_friends(user) for user in users)

print("Average Connections is {}".format(total_connections/len(users)))


num_of_friends_by_id = [(user["id"],num_of_friends(user)) for user in users]

# Data Scientists You may know 
# Vanilla Attempt to figuring out friends of friends 
