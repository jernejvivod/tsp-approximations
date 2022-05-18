import math
import re

import networkx as nx


def parse_graph(path: str, dist_func: str) -> nx.Graph:
    """Parse graph from file in specified format

    Args:
        path (str): path to file containing the graph specification
        dist_func (str): distance function to use ('l1' for L1 distance or 'l2' for L2 distance)

    Returns:
        (networkx.classes.graph.Graph): specified graph represented as a networkx Graph instance
    """

    # distance functions
    def l1(node1, node2):
        return abs(node1['x'] - node2['x']) + abs(node1['y'] - node2['y'])

    def l2(node1, node2):
        return math.sqrt((node1['x'] - node2['x']) ** 2 + (node1['y'] - node2['y']) ** 2)

    # Initialize networkx Graph.
    graph = nx.Graph()

    # Initialize regex for matching lines
    node_coordinate_spec_patt_str = '[+-]?([0-9]*[.])?[0-9]+'
    node_spec_patt = re.compile('^' + ' '.join([node_coordinate_spec_patt_str] * 3) + '$')
    num_nodes_spec_patt = re.compile('^[1-9]+[0-9]*$')
    comment_spec_patt = re.compile('^%.*')

    # parse graph
    found_num_nodes_spec = False
    with open(path, 'r') as f:
        for idx_line, line in enumerate(f):
            stripped_line = line.strip()
            if comment_spec_patt.match(stripped_line):  # comment
                pass
            elif num_nodes_spec_patt.match(stripped_line):  # number of nodes specification
                if found_num_nodes_spec:
                    raise ValueError('graph specification is not properly formatted (line {0})'.format(idx_line))
                found_num_nodes_spec = True
            elif node_spec_patt.match(stripped_line):  # node specification
                if not found_num_nodes_spec:
                    raise ValueError('graph specification is not properly formatted (line {0})'.format(idx_line))
                i, (x, y) = int(stripped_line.split()[0]), tuple(map(float, stripped_line.split()[1:]))
                graph.add_node(i, x=x, y=y)

    # compute distances between nodes
    nodes = list(graph.nodes())
    for node1_idx in range(len(graph.nodes) - 1):
        for node2_idx in range(node1_idx + 1, len(graph.nodes)):
            if dist_func == 'l2':
                dist = l2(graph.nodes()[nodes[node1_idx]], graph.nodes()[nodes[node2_idx]])
            elif dist_func == 'l1':
                dist = l1(graph.nodes()[nodes[node1_idx]], graph.nodes()[nodes[node2_idx]])
            else:
                raise ValueError('Invalid distance function specifier "{0}".'.format(dist_func))
            graph.add_edge(nodes[node1_idx], nodes[node2_idx], weight=dist)

    return graph
