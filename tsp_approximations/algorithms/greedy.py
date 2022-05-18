import random


def greedy(graph):
    """
    Use greedy approach to approximate the solution to the Travelling salesman problem.

    Args:
        graph (networkx.classes.graph.Graph): graph representing the problem instance

    Returns:
        (tuple): solution and its cost
    """

    # Initialize list for TSP path.
    solution_path = []

    # Initialize set for visited nodes.
    visited = set()

    # Initialize cost.
    cost = 0.0

    # Set random node as starting point.
    node_start = random.choice(list(graph.nodes()))
    visited.add(node_start)

    # Set current node to be the starting node and add it to solution path.
    node_current = node_start
    solution_path.append(node_start)

    # Perform greedy search.
    while len(visited) < graph.number_of_nodes() > 1:
        # Find nearest unvisited node.
        _, node_nxt, cost_nxt = min(filter(lambda x: x[1] not in visited, graph.edges(node_current, data=True)), key=lambda x: x[2]['weight'])
        # Add found node to solution path and add distance to total cost.
        solution_path.append(node_nxt)
        visited.add(node_nxt)
        cost += cost_nxt['weight']

        # Set current node to be the found closest node.
        node_current = node_nxt

    # Add cost of last edge to total cost.
    cost += graph.get_edge_data(solution_path[-1], solution_path[0])['weight']
    solution_path.append(solution_path[0])

    # Return found solution path and its cost
    return solution_path, cost
