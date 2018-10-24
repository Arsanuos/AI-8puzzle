import unittest
from manhatten import Manhatten
from euclidean import Euclidean
from state import State
from aStar import AStar
class TestAStar(unittest.TestCase):


    def test1(self):
        agent = AStar([1,2,5,3,4,0,6,7,8], Manhatten)
        print(agent.search())


    def test2(self):
        return
        agent = AStar([1,2,5,3,4,0,6,7,8], Euclidean)
        print(agent.search())








if __name__ == '__main__':
    unittest.main()