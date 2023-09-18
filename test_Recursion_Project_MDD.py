import unittest
import numpy as np
import time
from Recursion_Project_MDD import floyd_warshall_recursive, INF  # Importing from the project file

class TestFloydWarshall(unittest.TestCase):

    def setUp(self):
        self.graph = [
            [0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ]
        self.vertex_count = len(self.graph)

    def tearDown(self):
        del self.graph
        del self.vertex_count

    def test_shortest_path(self):
        for i in range(self.vertex_count):
            for j in range(self.vertex_count):
                floyd_warshall_recursive(self.graph, i, j, self.vertex_count - 1)

        expected = [
            [0, 5, 8, 9],
            [INF, 0, 3, 4],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ]

        self.assertEqual(self.graph, expected)

    def test_performance(self):
        vertex_count = 10
        graph = np.random.randint(0, 100, (vertex_count, vertex_count))

        start_time = time.time()

        for i in range(vertex_count):
            for j in range(vertex_count):
                floyd_warshall_recursive(graph, i, j, vertex_count - 1)

        end_time = time.time()
        self.assertLess(end_time - start_time, 2)

if __name__ == "__main__":
    unittest.main()
