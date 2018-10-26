from heuristic import Heuristic


class Manhatten(Heuristic):
    
    def get_heuristic(self, current_state):
        """
            Calculate the heuristic cost for the current state from the goal based on Manhatten distance.
        :param current: State object, which we want to calculate its heuristic cost.
        :return: heuristic cost of the current given state.
        """
        current_arr = current_state.current
        result = 0
        for current_index, true_index in enumerate(current_arr):
            if true_index != current_index:
                result += abs(true_index/3 - current_index/3) + abs(true_index%3 - current_index%3)
        return result
