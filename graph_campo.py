"""Assessment 3.3 - Diagram 2: Graph (CAMPO)
Algorithm 3: BFS (queue + visited)    Algorithm 4: DFS (recursion + visited)

Edges: C-A, C-M, A-P, M-O, P-O
"""
from collections import deque

graph = {
    "C": ["A", "M"],
    "A": ["C", "P"],
    "M": ["C", "O"],
    "P": ["A", "O"],
    "O": ["M", "P"],
}


def bfs(graph, start):
    visited = {start}                      # step 3
    q = deque([start])
    result = []
    while q:                               # step 4                         
        current = q.popleft()              # step 5
        result.append(current)             # step 6
        for neighbor in graph[current]:    # step 7
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return result


def dfs(graph, vertex, visited=None, result=None):
    if visited is None:
        visited, result = set(), []
    visited.add(vertex)                    # step 4
    result.append(vertex)
    for neighbor in graph[vertex]:         # step 5
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    return result                          # step 6 (backtrack)


if __name__ == "__main__":
    print("BFS (Graph):", " - ".join(bfs(graph, "C")))
    print("DFS (Graph):", " - ".join(dfs(graph, "C")))
