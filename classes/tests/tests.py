import unittest
from manhatten import Manhatten
from euclidean import Euclidean
from aStar import AStar
from bfs import BFS
from dfs import DFS

class TestAlgorithms(unittest.TestCase):
    def test_AStar_Manhatten(self):
        agent = AStar(Manhatten)
        steps = agent.search([1, 2, 5, 3, 4, 0, 6, 7, 8])
        print("Solved in {} steps".format(len(steps)))
        print(steps)

    def test_AStar_Euclidean(self):
        agent = AStar(Euclidean)
        steps = agent.search([1, 2, 5, 3, 4, 0, 6, 7, 8])
        print("Solved in {} steps".format(len(steps)))
        print(steps)

    def test_dfs(self):
        agent = DFS()
        steps = agent.search([1, 2, 5, 3, 4, 0, 6, 7, 8])
        print("Solved in {} steps".format(len(steps)))
        print(steps)

    def test_bfs(self):
        agent = BFS()
        steps = agent.search([1, 2, 5, 3, 4, 0, 6, 7, 8])
        print("Solved in {} steps".format(len(steps)))
        print(steps)


if __name__ == '__main__':
    unittest.main()
