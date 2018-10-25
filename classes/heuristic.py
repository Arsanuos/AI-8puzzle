from abc import ABC, abstractmethod


class Heuristic(ABC):

    @abstractmethod
    def get_heuristic(self, current):
        """
            Calculate and returns the heuristic cost of the given current state.
        :param current: State object, which we want to calculate its heuristic cost.
        :return: heuristic cost of the current given state.
        """
        pass

