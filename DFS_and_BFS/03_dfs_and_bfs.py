graph = {
    "Sara":   ["Amina"],
    "Amina":  ["Sara", "Razi"],
    "Razi":   ["Amina", "Ali", "Ahmed"],
    "Ali":    ["Razi"],
    "Ahmed":  ["Razi", "Amina", "Ahsan"],
    "Ahsan":  ["Ahmed", "Uzma"],
    "Uzma":   ["Ahsan", "Taha"],
    "Taha":   ["Uzma", "Rida", "Hassan"],
    "Rida":   ["Taha"],
    "Hassan": ["Taha"]
}

start = "Sara"
goal  = "Hassan"

# ---------- BFS ----------
def bfs_path(graph, start, goal):
    visited = [start]
    queue   = [[start]]
    print("BFS order visited: ", end="")
    while queue:
        path = queue.pop(0)
        node = path[-1]
        print(node, end=" ")
        if node == goal:
            print("\nBFS Path:", " -> ".join(path))
            return
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(path + [neighbour])

# ---------- DFS ----------
def dfs_path(graph, node, goal, visited, path):
    visited.append(node)
    path.append(node)
    print(node, end=" ")
    if node == goal:
        print("\nDFS Path:", " -> ".join(path))
        return True
    for neighbour in graph[node]:
        if neighbour not in visited:
            if dfs_path(graph, neighbour, goal, visited, path):
                return True
    path.pop()
    return False

print("=== Task 3 ===")
bfs_path(graph, start, goal)

print("\nDFS order visited: ", end="")
dfs_path(graph, start, goal, [], [])