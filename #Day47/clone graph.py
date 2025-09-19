from collections import deque
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        old_to_new = {}

        def dfs(n):
            # If already cloned, return it
            if n in old_to_new:
                return old_to_new[n]

            # Clone current node
            copy = Node(n.val)
            old_to_new[n] = copy

            # Clone neighbors
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)

def build_graph(adjList):
    if not adjList:
        return None
    nodes = [Node(i+1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    return nodes[0]

# Convert graph back to adjacency list for easy verification
def graph_to_adjlist(node):
    if not node:
        return []
    visited = {}
    q = deque([node])
    while q:
        cur = q.popleft()
        if cur.val not in visited:
            visited[cur.val] = [n.val for n in cur.neighbors]
            for nei in cur.neighbors:
                if nei.val not in visited:
                    q.append(nei)
    return [visited[i] for i in range(1, len(visited)+1)]

adjList = [[2,4],[1,3],[2,4],[1,3]]
graph = build_graph(adjList)
cloned = Solution().cloneGraph(graph)
print("Input:", adjList)
print("Cloned Output:", graph_to_adjlist(cloned))

adjList = [[]]
graph = build_graph(adjList)
cloned = Solution().cloneGraph(graph)
print("\nInput:", adjList)
print("Cloned Output:", graph_to_adjlist(cloned))

adjList = []
graph = build_graph(adjList)
cloned = Solution().cloneGraph(graph)
print("\nInput:", adjList)
print("Cloned Output:", graph_to_adjlist(cloned))
