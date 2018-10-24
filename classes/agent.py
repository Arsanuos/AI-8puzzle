from abc import ABC, abstractmethod
from copy import deepcopy
from state import State


class Agent(ABC):

    def __init__(self):
        # vis is set of states not arrays
        self.__vis = set()

    def expand(self, current_state, heuristic=None):
        child_states = []

        current_arr = current_state.current
        empty_index = (current_arr.index(0)/3, current_arr.index(0)%3)

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for x, y in zip(dx, dy):
            if 0 <= (empty_index[0] + x) <= 2 and 0 <= (empty_index[1] + y) <= 2:
                new_arr = deepcopy(current_state.current)
                old_index = new_arr.index(0)
                new_index = (empty_index[0] + x) * 3 + (empty_index[1] + y)
                new_arr[old_index], new_arr[new_index] = new_arr[new_index], new_arr[old_index]
                child_state = State(new_arr, current_state, heuristic)
                if child_state not in self.vis:
                    child_states.append(child_state)

        return child_states

    @property
    def vis(self):
        return self.__vis

    @abstractmethod
    def search(self, initial_state):
        pass

