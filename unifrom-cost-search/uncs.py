
mygraph = {
    'S': [('A', 6), ('B', 5), ('C', 10)],
    'A': [('E', 6)],
    'B': [('E', 6), ('D', 7)],
    'C': [ ('D', 6)],
    'D': [ ('F', 6)],
    'E': [('F', 4)],
    'F': [('G', 3)],
}

def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost = total_cost + cost
    return total_cost, path[-1][0]

def myucs(mygraph, start, goal):
    visited = []

    queue = [[(start, 0)]]

    while queue:

        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]

        if node not in visited:
            visited.append(node)


            if node == goal:
                return path, visited
            else:
                neighbour_nodes = mygraph.get(node, [])
                for (node2, cost) in neighbour_nodes:
                    new_path = path.copy()
                    new_path.append((node2, cost))
                    queue.append(new_path)
        else:
            continue

    return None, visited

shortest_path_tuples, expansion_order = myucs(mygraph, "S", "G")

if shortest_path_tuples:

    shortest_path = [node for node, cost in shortest_path_tuples]
    total_cost, _ = path_cost(shortest_path_tuples)

    print("Shortest path:", " -> ".join(shortest_path))
    print("Total path cost:", total_cost)
    print("Order of expansion:", ", ".join(expansion_order))
else:
    print("No path found.")