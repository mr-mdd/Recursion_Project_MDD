# Recursion_Project_MDD

INTRODUCTION:
The Recursion_Project_MDD.py project aims to implement the Floyd-Warshall algorithm for finding shortest paths in a weighted graph with positive or negative edge weights using recursion. This approach offers both theoretical elegance and computational efficiency. It blends academic rigor with practical relevance, making it valuable for scholars studying graph theory or computer science and professionals dealing with network routing and other relevant applications.

DEPENDENCIES:
To execute this project, you will require the following Python libraries:

numpy
unittest

INSTALLATION:
To install the necessary dependencies, execute the following command:

pip install numpy

RUNNING THE TESTS:
To execute the unit tests for this project, navigate to the project directory and run:

python -m unittest

USAGE:
To run the main script and see the Floyd-Warshall algorithm in action, navigate to the project directory and execute:

python Recursion_Project_MDD.py

EXAMPLE AND EXPLANATION:
The project provides an implementation of the Floyd-Warshall algorithm to find the shortest paths in a weighted graph represented as an adjacency matrix. For instance, consider the adjacency matrix:

[
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

Running the algorithm will update this matrix to indicate the shortest paths between each pair of vertices:

[
    [0, 5, 8, 9],
    [INF, 0, 3, 4],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

TESTING:
Unit tests are included in the script, making use of the unittest framework. These tests cover both functionality and performance, thereby ensuring that the implementation is not only correct but also efficient.

CONTRIBUTING:
Contributions are welcome. To contribute, kindly follow the standard Fork & Pull Request process.

LICENSE:
This project is licensed under the MIT License. See the LICENSE.md file for details.