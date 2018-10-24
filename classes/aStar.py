from agent import Agent
from state import State
from manhatten import Manhatten
from euclidean import Euclidean
from agent import Agent
from state import State
from heapq import heappush, heappop, nsmallest

class AStar(Agent):

    def __init__(self, initial_arr, heuristic):
        self.__initial_state = State(initial_arr, None, heuristic)
        super().__init__()

    def search(self):
        states_heap = []
        heappush(states_heap, self.__initial_state)
        end = None
        while len(states_heap):
            # break tie by FIFO criteria
            current_explored_state = heappop(states_heap)
            if current_explored_state.is_goal():
                print(current_explored_state.current)
                end = current_explored_state
                break

            if current_explored_state not in self.vis:
                self.vis.add(current_explored_state)
                child_states = self.expand(current_explored_state)
                for child in child_states:
                    heappush(states_heap, child)

        self.print_util(self.get_path(end))
        return self.get_path(end)


    def print_util(self, states):
        print(len(states))
        print("================================")
        for state in states:
            for i in range(0, 9, 3):
                print(state.current[i:i + 3])
            print("================================")