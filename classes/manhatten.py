from heuristic import Heuristic


class Manhatten(Heuristic):
    
    def get_heuristic(self, current_state):
        current_arr = current_state.current
        result = 0
        for current_index, true_index in enumerate(current_arr):
            if true_index != current_index:
                result += abs(true_index/3 - current_index/3) + abs(true_index%3 - current_index%3)
        return result
