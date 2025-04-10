from collections import defaultdict
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)

        def dfs(i):
            if i == destination:
                return True
            for nei_node in graph[i]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    if dfs(nei_node):
                        return True

            return False

        return dfs(source)


s = Solution()
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
print("Test: ", s.validPath(n=n, edges=edges, source=source, destination=destination))
