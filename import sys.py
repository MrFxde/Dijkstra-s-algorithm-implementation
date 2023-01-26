import sys

#A dictionary data structure will be used to store the 
# information of all vertices and edges
graph = {}

#function to add a vertex
def add_vertex(vertex):
    graph[vertex] = {}
    

#function to add an edge
def add_edge(vertex, dest, weight):
    graph[vertex].update({dest:weight})
    graph[dest].update({vertex:weight})

#Dijsktra's Algorithm
def algorithm(graph, start, goal):
    #Stores shortest distance from A (or starting vertex)
    shortest_distance = {}
    #Stores previous vertex values
    track_predecessor = {}
    #Stores all vertices, this is our unvisited list
    unseenNodes = graph
    #very big number
    infinity = sys.maxsize
    #Will be used to store the shortest path
    track_path = []

    #Assigns starting vertex cost to 0, and the rest infinity
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    #while the visited list still has vertices
    while unseenNodes:

        #initially there won't be a current vertex assigned
        min_distance_node = None
        for node in unseenNodes:
            if min_distance_node is None: 
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        #For the current vertex, store its neightbors
        path_options = graph[min_distance_node].items()

        #Then calculate the distance of each adjacent vertex from the start vertex
        for child_node, weight in path_options:
            #If the calculated distance of a vertex is less than the know distance,
            # update the shortest distance and update the previous vertex
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                #updates the previous vertex
                track_predecessor[child_node] = min_distance_node
         #Remove the vertex from the list of unvisited vertices 
        unseenNodes.pop(min_distance_node)
    
    #set the current node to the vertex that is the goal to reach
    currentNode = goal

    #this code will trace back from the destination, back to the starting vertex
    while currentNode != start:
        #
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        #handles scenarios that aren't connected
        except KeyError:
            print('Path is not reachable')
            break
    track_path.insert(0,start)

    if shortest_distance[goal] != infinity:
        print("Shortest distance is " + str(shortest_distance[goal]))
        print("Optimal path is " + str(track_path))

#Adding vertices and edges
add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
add_vertex('E')
add_edge('A','B',6)
add_edge('A','D',1)
add_edge('B','D',2)
add_edge('B','E',2)
add_edge('B','C',7)
add_edge('C','E',4)
add_edge('D','E',1)
algorithm(graph,'A','C')
