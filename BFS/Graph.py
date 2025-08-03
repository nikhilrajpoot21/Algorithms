'''Breadth-First Search (BFS) is a fundamental graph traversal algorithm used to explore nodes and edges of a graph in a breadthward motion(Explore all neighbour first).

What Is BFS?
BFS starts from a selected node (often called the "source") and explores all its neighbors before moving on to their neighbors. It uses a queue to keep track of the next node to visit, ensuring a level-by-level traversal.

BFS Algorithm Steps
Initialize:

Create a queue and a visited set.

Enqueue the starting node and mark it as visited.

Traverse:

While the queue is not empty:

Dequeue the front node.

Visit all its unvisited neighbors:

Mark them as visited.

Enqueue them. '''

from collections import deque
class Edge:
    def __init__(self,s,d):
        self.src = s
        self.dest = d
'''
       1--------3 ----5 -----6
     / |      / |    /
    0  |    /   |   /
     \ |  /     |  /
       2--------4 /
'''    
def createGraph():
    v = 7
    graph = [[]for _ in range(v)]

    graph[0].append(Edge(0,1))
    graph[0].append(Edge(0,2))
    graph[1].append(Edge(1,0))
    graph[1].append(Edge(1,2))                                                            
    graph[1].append(Edge(1,3))
    graph[2].append(Edge(2,0))
    graph[2].append(Edge(2,1))
    graph[2].append(Edge(2,3))
    graph[2].append(Edge(2,4))
    graph[3].append(Edge(3,4))
    graph[3].append(Edge(3,1))
    graph[3].append(Edge(3,2))
    graph[4].append(Edge(4,2))
    graph[4].append(Edge(4,3))
    graph[4].append(Edge(4,5))
    graph[5].append(Edge(5,3))
    graph[5].append(Edge(5,6))
    graph[5].append(Edge(6,5))

    return graph

def bfs(graph,V):
    visited = [False]*V
    q = deque()
    q.append(0)

    while q:
        curr = q.popleft()
        if not visited[curr]:
            print(curr,end=" ")
            visited[curr] = True

            for edge in graph[curr]:
                q.append(edge.dest)

graph = createGraph()
bfs(graph,7)
