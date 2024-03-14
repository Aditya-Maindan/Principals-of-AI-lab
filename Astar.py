def aStarAlgo(start_node, stop_node):
    """
    A* algorithm for finding the shortest path between two nodes in a graph.

    Args:
        start_node: The starting node.
        stop_node: The ending node.

    Returns:
        A list of nodes representing the shortest path from start_node to stop_node,
        or None if no path exists.
    """

    open_set = set([start_node])
    closed_set = set()
    g = {}  # Store distance from starting node
    parents = {}  # Parents contains an adjacency map of all nodes

    # Distance of starting node from itself is zero
    g[start_node] = 0

    # Start_node is root node i.e it has no parent nodes
    # So start_node is set to its own parent node
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # Node with lowest f() is found
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # Nodes 'm' not in first and last set are added to first
                # n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # For each node m, compare its distance from start i.e g(m) to the
                # From start through n node
                else:
                    if g[m] > g[n] + weight:
                        # Update g(m)
                        g[m] = g[n] + weight
                        # Change parent of m to n
                        parents[m] = n
                        # If m in closed set, remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n is None:
            print("Path does not exist!")
            return None

        # If the current node is the stop_node
        # Then we begin reconstructing the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()
            print("Path found:", path)
            return path

        # Remove n from the open_list, and add it to closed_list
        # Because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)


def get_neighbors(v):
    """
    Returns the neighbors of a node in the graph.

    Args:
        v: The node.

    Returns:
        A list of tuples, where each tuple contains a neighbor and its distance
        from the node.
    """

    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


def heuristic(n):
    """
    Returns the heuristic distance of a node from the goal node.

    Args:
        n: The node.

    Returns:
        The heuristic distance of the node from the goal node.
    """

    H_dist = {
        "A": 11,
        "B": 6,
        "C": 99,
        "D": 1,
        "E": 7,
        "G": 0,
    }
    return H_dist[n]


# Describe your graph here
Graph_nodes = {
    "A": [("B", 2), ("E", 3)],
    "B": [("C", 1), ("G", 9)],
    "C": None,
    "E": [("D", 6)],
    "D": [("G", 1)],
}

aStarAlgo("A", "G")
