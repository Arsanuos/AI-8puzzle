import unittest
from manhatten import Manhatten
from euclidean import Euclidean
from state import State
from aStar import AStar
class TestAStar(unittest.TestCase):


    def test1(self):
        agent = AStar(Manhatten)
        print(agent.search([1,2,5,3,4,0,6,7,8]))


    def test2(self):
        agent = AStar(Euclidean)
        print(agent.search([1,2,5,3,4,0,6,7,8]))








if __name__ == '__main__':
    unittest.main()