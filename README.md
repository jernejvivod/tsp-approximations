# Travelling Salesman Problem Solution Approximations

This project contains four implementations of algorithms for computing solutions to the Travelling salesman problem.

## How to Run

run `pip -r requirements.txt` to install the requirements.

Running `python3 tsp-approximations --help` prints the instructions on how to customize the execution parameters:

```
usage: tsp-approximations [-h] [--dist-func {l1,l2}] [--algorithm {exhaustive,greedy,two_apx,christofides}] dataset-path

positional arguments:
  dataset-path          path to file specifying the graph

optional arguments:
  -h, --help            show this help message and exit
  --dist-func {l1,l2}   distance function to use
  --algorithm {exhaustive,greedy,two_apx,christofides}
                        path to file specifying the graph
```
