lass Node:
def __init__(self, v, weight):
self.v=v
self.weight=weight
class pathNode:
def __init__(self, node, parent):
self.node=node
self.parent=parent
def addEdge(u, v, weight):
adj[u].append(Node(v, weight))
adj = []
13
def GBFS(h, V, src, dest):
openList = []
closeList = []
openList.append(pathNode(src, None))
while (openList):
currentNode = openList[0]
currentIndex = 0
for i in range(len(openList)):
if(h[openList[i].node] < h[currentNode.node]):
currentNode = openList[i]
currentIndex = i
openList.pop(currentIndex)
closeList.append(currentNode)
if(currentNode.node == dest):
path = []
cur = currentNode
while(cur != None):
path.append(cur.node)
cur = cur.parent
path.reverse()
return path
for node in adj[currentNode.node]:
for x in openList:
if(x.node == node.v):
continue
for x in closeList:
if(x.node == node.v):
continue
openList.append(pathNode(node.v, currentNode))
return []
""" Making the following graph
src = 0
/ | \
/ | \
1 2 3
/\ | /\
/ \ | / \
4 5 6 7 8
/
/
dest = 9
"""
V = 10
for i in range(V):
adj.append([])
addEdge(0, 1, 2)
addEdge(0, 2, 1)
addEdge(0, 3, 10)
14
addEdge(1, 4, 3)
addEdge(1, 5, 2)
addEdge(2, 6, 9)
addEdge(3, 7, 5)
addEdge(3, 8, 2)
addEdge(7, 9, 5)
h = [20, 22, 21, 10, 25, 24, 30, 5, 12, 0]
path = GBFS(h, V, 0, 9)
for i in range(len(path) - 1):
print(path[i], end = " -> ")
print(path[(len(path)-1)])
2. A* Algorithm:-
def aStarAlgo(start_node, stop_node):
open_set = set(start_node)
closed_set = set()
g = {}
parents = {}
g[start_node] = 0
parents[start_node] = start_node
while len(open_set) > 0:
n = None
for v in open_set:
if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
n = v
if n == stop_node or Graph_nodes[n] == None:
pass
else:
for (m, weight) in get_neighbors(n):
if m not in open_set and m not in closed_set:
open_set.add(m)
parents[m] = n
g[m] = g[n] + weight
else:
if g[m] > g[n] + weight:
g[m] = g[n] + weight
parents[m] = n
if m in closed_set:
closed_set.remove(m)
open_set.add(m)
if n == None:
print('Path does not exist!')
return None
15
if n == stop_node:
path = []
while parents[n] != n:
path.append(n)
n = parents[n]
path.append(start_node)
path.reverse()
print('Path found: {}'.format(path))
return path
open_set.remove(n)
closed_set.add(n)
print('Path does not exist!')
return None
def get_neighbors(v):
if v in Graph_nodes:
return Graph_nodes[v]
else:
return None
def heuristic(n):
H_dist = {
'A': 11,
'B': 6,
'C': 99,
'D': 1,
'E': 7,
'G': 0,
}
return H_dist[n]
Graph_nodes = {
'A': [('B', 2), ('E', 3)],
'B': [('C', 1),('G', 9)],
'C': None,
'E': [('D', 6)],
'D': [('G', 1)],
}
aStarAlgo('A', 'G')