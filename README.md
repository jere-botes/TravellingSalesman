# TravellingSalesman
The Travelling Salesman Problem (often called TSP) is a classic algorithmic problem in the field of computer science and operations research. It is focused on optimization. In this context better solution often means a solution that is cheaper. TSP is a mathematical problem. It is most easily expressed as a graph describing the locations of a set of nodes.
In simple terms, the travelling salesman problem asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?"

The travelling salesman problem is regarded as difficult to solve. If there is a way to break this problem into smaller component problems, the components will be at least as complex as the original one. This is what computer scientists call NP-hard problems.
Many people have studied this problem. The easiest (and most expensive solution) is to simply try all possibilities. The problem with this is that for N cities you have (N-1) factorial possibilities. This means that for only 10 cities there are over 360,000 permutations to try (since the start city is defined, there can be permutations on the remaining nine).
With just 15 cities (nodes), the possible permutations are more than 87 Billion!

Heuristics approaches use a set of guiding rules for selection of the next node. But since heuristics result in approximations, they will not always give the optimal solution, although high quality admissible heuristics can find a useful solution in a fraction of the time required for a full brute force of the problem.

TSP Algorithms:
SA - Simulated Annealing algorithm
GA - Genetic algorithms
Monte Carlo algorithms
