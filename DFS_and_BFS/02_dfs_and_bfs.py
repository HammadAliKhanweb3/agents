graph = {
    "A": ["B", "D"],
    "B": ["C", "G"],
    "C": ["D"],
    "D": ["A"],
    "E": ["A", "H"],
    "F": ["G"],
    "G": ["F"],
    "H": ["F"]
}

start = input("Enter start node: ").strip().upper()   # A
goal  = input("Enter goal node:  ").strip().upper()   # G

# ---------- BFS with path ----------
def bfs_path(graph, start, goal):
    visited = [start]
    queue   = [[start]]          # queue of paths
    print("BFS traversal: ", end="")
    while queue:
        path = queue.pop(0)
        node = path[-1]
        print(node, end=" ")
        if node == goal:
            print("\nGoal reached!")
            print("BFS Path:", " -> ".join(path))
            return
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(path + [neighbour])
    print("\nGoal not found.")

# ---------- DFS with path ----------
def dfs_path(graph, node, goal, visited, path):
    visited.append(node)
    path.append(node)
    print(node, end=" ")
    if node == goal:
        print("\nGoal reached!")
        print("DFS Path:", " -> ".join(path))
        return True
    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs_path(graph, neighbour, goal, visited, path):
                return True
    path.pop()   # backtrack
    return False

print("\n=== Task 2 ===")
bfs_path(graph, start, goal)

print("\nDFS traversal: ", end="")
dfs_path(graph, start, goal, [], [])