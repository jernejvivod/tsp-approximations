import argparse
import time
from enum import Enum

from tsp_approximations.algorithms.christofides import christofides
from tsp_approximations.algorithms.exhaustive import exhaustive_search
from tsp_approximations.algorithms.greedy import greedy
from tsp_approximations.algorithms.two_apx import two_apx
from tsp_approximations.util.parse_graph import parse_graph


# available algorithms
class Algorithm(Enum):
    EXHAUSTIVE = 'exhaustive'
    GREEDY = 'greedy'
    TWO_APX = 'two_apx'
    CHRISTOFIDES = 'christofides'


# available distance functions
class DistFunc(Enum):
    L1 = 'l1'
    L2 = 'l2'


def main(**kwargs):
    # Parse graph.
    graph = parse_graph(kwargs['dataset-path'], kwargs['dist_func'])

    print('Computing solution for the TSP problem for the graph specified in {0} using \'{1}\'.'
          .format(kwargs['dataset-path'], kwargs['algorithm']))

    # Compute solution and cost of solution.
    start_time = time.time()
    if kwargs['algorithm'] == Algorithm.EXHAUSTIVE.value:
        solution, cost = exhaustive_search(graph)
    elif kwargs['algorithm'] == Algorithm.GREEDY.value:
        solution, cost = greedy(graph)
    elif kwargs['algorithm'] == Algorithm.TWO_APX.value:
        solution, cost = two_apx(graph)
    elif kwargs['algorithm'] == Algorithm.CHRISTOFIDES.value:
        solution, cost = christofides(graph)
    else:
        raise ValueError('unknown algorithm specified: {0}'.format(kwargs['algorithm']))
    running_time = time.time() - start_time

    # Print results.
    print('Solution: {0}'.format(solution))
    print('Cost: {0}'.format(round(cost, 3)))
    print('Running time: {0} ms'.format(round(running_time * 1000, 3)))


if __name__ == '__main__':
    # Parse configuration.
    parser = argparse.ArgumentParser(prog='tsp-approximations')
    parser.add_argument('dataset-path', type=str, help='path to file specifying the graph')
    parser.add_argument('--dist-func', type=str, choices=[d.value for d in DistFunc], default=DistFunc.L2.value, help='distance function to use')
    parser.add_argument('--algorithm', type=str, choices=[a.value for a in Algorithm], default=Algorithm.GREEDY.value, help='path to file specifying the graph')

    # Run.
    args = parser.parse_args()
    main(**vars(args))
