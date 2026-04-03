graph = {
    1:  [2, 3, 4],
    2:  [5, 6],
    3:  [],
    4:  [7, 8],
    5:  [9, 10],
    6:  [],
    7:  [11, 12],
    8:  [],
    9:  [],
    10: [],
    11: [],
    12: []
}

start = 1
goal  = 11

# ---------- BFS ----------
def bfs(graph, start, goal):
    visited = []
    queue   = [start]
    visited.append(start)
    print("BFS traversal: ", end="")
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        if node == goal:
            print("\nGoal", goal, "reached!")
            return
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# ---------- DFS ----------
def dfs(graph, visited, node, goal):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")
        if node == goal:
            print("\nGoal", goal, "reached!")
            return True
        for neighbour in graph[node]:
            if dfs(graph, visited, neighbour, goal):
                return True
    return False

print("=== Task 1 ===")
bfs(graph, start, goal)

print("DFS traversal: ", end="")
dfs(graph, [], start, goal)