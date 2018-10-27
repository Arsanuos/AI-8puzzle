from agent import Agent
from state import State
from heapq import heappush, heappop, nsmallest

class AStar(Agent):

    def __init__(self, heuristic):
        self.__heuristic = heuristic
        super().__init__()

    def search(self, initial_arr):
        """

        :param initial_arr: inital array of the board.
        :return: dictionary of steps, cost of path, search depth and number of nodes expanded.
        """
        self.__initial_state = State(initial_arr, None, self.__heuristic)
        if not self.check_solvable(self.__initial_state):
            return {'steps': [[-1] * 9], 'cost': -1,
                    'search_depth': -1, 'nodes_expanded': -1}

        states_heap = []
        heappush(states_heap, self.__initial_state)
        end = None
        while len(states_heap):
            # break tie by FIFO criteria
            current_explored_state = heappop(states_heap)
            if current_explored_state.is_goal():
                end = current_explored_state
                break

            if current_explored_state not in self.vis:
                self._explored += 1
                self.vis.add(current_explored_state)
                child_states = self.expand(current_explored_state)
                for child in child_states:
                    heappush(states_heap, child)

        res = {}
        res['steps'] = self.get_steps(end)
        res['cost'] = end.cost
        res['search_depth'] = end.cost
        res['nodes_expanded'] = self._explored
        return res
