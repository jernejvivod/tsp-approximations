import itertools
from typing import Iterable

import networkx as nx
import numpy as np


def exhaustive_search(graph: nx.Graph):
    """
    Use exhaustive approach to solve the Travelling salesman problem.

    Args:
        graph (networkx.classes.graph.Graph): graph representing the problem instance

    Returns:
        (tuple): solution and its cost
    """

    # generator of candidate TSP paths
    def candidate_path_gen(nodes: Iterable):
        for perm in itertools.permutations(nodes):
            yield perm + (perm[0],)

    # Exhaustively search all candidate TSP paths to find path with minimal cost.
    min_cost = np.inf
    sol = None
    for candidate_path in candidate_path_gen(graph.nodes()):
        cost_candidate = sum(graph.get_edge_data(candidate_path[idx], candidate_path[idx + 1])['weight'] for idx in range(len(candidate_path) - 1))
        if cost_candidate < min_cost:
            min_cost = cost_candidate
            sol = candidate_path

    # Return found solution path and its cost
    return sol, min_cost
