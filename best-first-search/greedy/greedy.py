mygraph = {
     'S': [('A',5), ('B',9), ('D',6)],
    'A': [('B',3), ('G1',9)],
    'B': [('C',1),('A',2)],
    'C': [('S',6), ('F',7), ('G2',5)],
    'D': [('E',2),('C',2)],
    'E': [('G3',7)],
    'F': [('D',2), ('G3',8)],
    'G1': [],
    'G2': [],
    'G3': []
}

H_table = {
    "S": 10,
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 3,
    "E": 6,
    "F": 3,
    "G1": 0,
    "G2": 0,
    "G3": 0
}

goals = ["G1", "G2", "G3"]


def path_cost_a_star(path):
    total_g_cost = 0
    for (node, g_cost) in path:
        total_g_cost += g_cost

    last_node = path[-1][0]
    h_cost = H_table[last_node]
    f_cost = total_g_cost + h_cost
    return f_cost

def my_a_star(mygraph, start, goals):
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

            if node in goals:
                return path, expanded_order

            neighbour_nodes = mygraph.get(node, [])
            for (node2, cost) in neighbour_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)

    return None, expanded_order


answer_path, expanded = my_a_star(mygraph, "S", goals)

final_path = [node for node, cost in answer_path]


total_cost = sum(cost for node, cost in answer_path)

print("Shortest path:", " -> ".join(final_path))
print("Total path cost:", total_cost)
print("Order of expansion:", expanded)
