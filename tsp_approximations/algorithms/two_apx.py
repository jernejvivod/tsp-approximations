import random

import networkx as nx


def two_apx(graph):
    """
    Use 2-APX approach to solve the Travelling salesman problem.

    Args:
        graph (networkx.classes.graph.Graph): graph representing the problem instance

    Returns:
        (tuple): solution and its cost
    """

    # Compute minimum spanning tree.
    mst = nx.minimum_spanning_tree(graph, weight='weight')

    # Select starting node and list nodes using preorder DFS.
    node_start = random.choice(list(graph.nodes()))
    solution_path = list(nx.dfs_preorder_nodes(mst, source=node_start))
    solution_path.append(solution_path[0])

    # Compute cost of found path.
    cost = sum(graph.get_edge_data(solution_path[idx], solution_path[idx+1])['weight'] for idx in range(len(solution_path)-1))

    # Return found solution path and its cost
    return solution_path, cost
