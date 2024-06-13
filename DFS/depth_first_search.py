class DepthFirstSearch:
    def __init__(self) -> None:
        pass
    
    def dfs(self, graph, start, visited=None):
        if visited is None:
            visited =set()
        visited.add(start)
        print(start, end="")

        for neighbor in graph[start]:
            if neighbor not in visited:
                self.dfs(graph, neighbor, visited)

test = DepthFirstSearch()
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS traversal starting from 'A':")
test.dfs(graph, 'A')

# Output

# DFS traversal starting from 'A':
# A B D E F C 
