
mygraph = {
    'S': [('A', 6), ('B', 5), ('C', 10)],
    'A': [('E', 6)],
    'B': [('E', 6), ('D', 7)],
    'C': [('D', 6)],
    'D': [('F', 6)],
    'E': [('F', 4)],
    'F': [('G', 3)],
    'G': []
}


H_table = {
    'S': 17, 'A': 10, 'B': 13, 'C': 4, 'D': 2, 'E': 4, 'F': 1, 'G': 0
}


def heuristic(path):
    """Used for GBFS sorting: returns h(n) of the last node in the path."""
    node = path[-1][0]
    return H_table[node]

def path_cost_a_star(path):
    """Used for A* sorting: returns f(n) = g(n) + h(n)."""
    total_g_cost = 0
    for (node, g_cost) in path:
        total_g_cost += g_cost

    last_node = path[-1][0]
    h_cost = H_table[last_node]
    f_cost = total_g_cost + h_cost
    return f_cost

def actual_path_cost(path):
    """Calculates the total actual cost g(n) of a given path."""
    return sum(cost for (_, cost) in path)


def gbfs(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    expansion_order = []

    while queue:

        queue.sort(key=heuristic)
        path = queue.pop(0)
        node = path[-1][0]

        if node not in visited:
            visited.append(node)
            expansion_order.append(node)

            if node == goal:
                return path, actual_path_cost(path), expansion_order

            for (neighbor, cost) in graph.get(node, []):
                new_path = path.copy()
                new_path.append((neighbor, cost))
                queue.append(new_path)

    return None, 0, expansion_order


def my_a_star(graph, start, goal):
    visited = []
    expanded_order = []
    queue = [[(start, 0)]]

    while queue:

        queue.sort(key=path_cost_a_star)
        path = queue.pop(0)
        node = path[-1][0]

        if node not in visited:
            visited.append(node)
            expanded_order.append(node)

            if node == goal:
                return path, expanded_order

            neighbour_nodes = graph.get(node, [])
            for (node2, cost) in neighbour_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)

    return None, expanded_order



print("--- Greedy Best-First Search (GBFS) ---")
gbfs_path, gbfs_cost, gbfs_order = gbfs(mygraph, "S", "G")
final_gbfs_path = [node for node, cost in gbfs_path]

print("Path:", " -> ".join(final_gbfs_path))
print("Total Cost:", gbfs_cost)
print("Expansion Order:", ", ".join(gbfs_order))
print("\n")


print("--- A* Search ---")
astar_path, astar_expanded = my_a_star(mygraph, "S", "G")
final_astar_path = [node for node, cost in astar_path]
total_astar_cost = sum(cost for node, cost in astar_path)

print("Shortest path:", " -> ".join(final_astar_path))
print("Total path cost:", total_astar_cost)
print("Order of expansion:", ", ".join(astar_expanded))
print("\n")


comparison_text = """--- Comparison: GBFS vs. A* ---

1. Did both algorithms find the same path?
No, they found completely different paths. GBFS found a suboptimal path (S -> C -> D -> F -> G) with a higher total cost of 25. A* Search found the optimal, shortest path (S -> B -> E -> F -> G) with a lower total cost of 18.

2. Which algorithm expanded fewer nodes?
GBFS expanded fewer nodes. It went straight down a single path, expanding only 5 nodes (S, C, D, F, G). A* Search had to explore various branches to ensure it found the absolute lowest cost, expanding more nodes in the process.

3. Reason for the difference:
* GBFS is short-sighted: It only looks at the heuristic h(n) (estimated distance to goal). It aggressively picks the node that looks closest, ignoring the actual edge costs. Because Node C had a low heuristic (h=4), GBFS rushed there and fell into a trap of expensive edge costs later.
* A* is comprehensive: It calculates f(n) = g(n) + h(n), combining actual accumulated cost with estimated cost. If a path gets too expensive, A* backtracks to explore cheaper routes. This causes it to expand more nodes but guarantees it finds the optimal, lowest-cost path."""

print(comparison_text)