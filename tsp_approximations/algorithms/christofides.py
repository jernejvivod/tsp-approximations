import networkx as nx


def christofides(graph):
    """
    Use Christofides approach to approximate the solution to the Travelling salesman problem.

    Args:
        graph (networkx.classes.graph.Graph): graph representing the problem instance

    Returns:
        (tuple): solution and its cost
    """

    # Compute minimum spanning tree.
    mst = nx.minimum_spanning_tree(graph, weight='weight')

    # Get induced subgraph given by nodes with odd degree.
    nodes_odd_degree = [el[0] for el in mst.degree if el[1] % 2 == 1]
    graph_odd = graph.subgraph(nodes_odd_degree)

    # Find minimum complete matching in the induced subgraph.

    # Negate weights to reduce to maximum weight complete matching.
    attr_ds = []
    for _, _, d in graph_odd.edges(data=True):
        attr_ds.append(d)
        d['weight'] *= -1
    min_matching = nx.algorithms.matching.max_weight_matching(graph_odd, maxcardinality=True, weight='weight')

    # Undo negation of weights.
    for d in attr_ds:
        d['weight'] *= -1

    # Add edges from matching to MST.
    mst_mult = nx.MultiGraph(mst)
    for e in min_matching:
        mst_mult.add_edge(e[0], e[1], weight=graph.get_edge_data(*e)['weight'])

    # Compute Eulerian circuit.
    eul_circ = map(lambda x: x[0], nx.algorithms.eulerian_circuit(mst_mult))

    # Convert to Hamiltonian circuit (to get solution) by skipping repeated nodes.
    seen = set()
    solution_path = []
    for n in eul_circ:
        if n not in seen:
            solution_path.append(n)
            seen.add(n)

    solution_path.append(solution_path[0])

    # Compute cost of found path.
    cost = sum(graph.get_edge_data(solution_path[idx], solution_path[idx + 1])['weight'] for idx in range(len(solution_path) - 1))

    # Return found solution path and its cost.
    return solution_path, cost
