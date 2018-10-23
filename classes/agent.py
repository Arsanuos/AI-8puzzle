from abc import ABC, abstractmethod
from copy import copy


class Agent(ABC):

    def __init__(self):
        self.__vis = set()

    def expand(self, current_state):
        current_arr = current_state.current
        empty_index = (current_arr.index(0)/3, current_arr.index(0)%3)

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for x, y in zip(dx, dy):
            if 0 <= (empty_index[0] + x) <= 2 and 0 <= (empty_index[1] + y) <= 2:
                new_arr = copy(current_state.current)
                old_place, new_place = new_place, old_place
                new_arr[(empty_index[0] * 3 + empty_index[1])], \
                new_arr[(empty_index[0] + x) * 3 + (empty_index[1] + y)] = \
                new_arr[(empty_index[0] + x) * 3 + (empty_index[1] + y)], \
                new_arr[(empty_index[0] * 3 + empty_index[1])]
