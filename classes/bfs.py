from agent import Agent
from state import State


class BFS(Agent):

    def __init__(self):
        super().__init__()
        self._optimize_flag = True

    def search(self, initial_state):
        curr_state = State(initial_state, None)
        if not self.check_solvable(curr_state):
            return {'steps': [[-1] * 9], 'cost': -1,
                    'search_depth': -1, 'nodes_expanded': -1}

        frontier = [curr_state]
        while frontier:
            curr_state = frontier.pop(0)
            self.vis.add(curr_state)
            self._explored += 1
            if curr_state.is_goal():
                break
            children = self.expand(curr_state)
            for child in children:
                #if child not in frontier:
                frontier.append(child)

        steps = self.get_steps(curr_state)
        res = {}
        res['steps'] = steps
        res['cost'] = curr_state.cost
        res['search_depth'] = curr_state.cost
        res['nodes_expanded'] = self._explored
        return res
