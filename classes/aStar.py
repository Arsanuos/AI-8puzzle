from agent import Agent
from state import State
from heapq import heappush, heappop, nsmallest

class AStar(Agent):

    def __init__(self, heuristic):
        self.__heuristic = heuristic
        super().__init__()

    def search(self, initial_arr):
        self.__initial_state = State(initial_arr, None, self.__heuristic)
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
                self.vis.add(current_explored_state)
                child_states = self.expand(current_explored_state)
                for child in child_states:
                    heappush(states_heap, child)

        return self.get_steps(end)

    def print_util(self, states):
        print(len(states))
        print("================================")
        for state in states:
            for i in range(0, 9, 3):
                print(state.current[i:i + 3])
            print("================================")