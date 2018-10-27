from agent import Agent
from state import State


class DFS(Agent):

    def __init__(self):
        super().__init__()
        self._optimize_flag = True

    def search(self, initial_state):
        res = {}
        start = State(initial_state, None)
        if not self.check_solvable(start):
            return {'steps': [[-1] * 9], 'cost': -1,
                    'search_depth': -1, 'nodes_expanded': -1}

        frontier = [start]
        final_state = None
        while frontier:
            state = frontier.pop()
            self.vis.add(state)
            self._explored += 1
            if state.is_goal():
                final_state = state
                break
            neighbours = self.expand(state)
            for neighbour in neighbours:
                #if neighbour not in frontier:
                frontier.append(neighbour)

        steps = self.get_steps(final_state)
        res['steps'] = steps
        res['cost'] = final_state.cost
        res['search_depth'] = final_state.cost
        res['nodes_expanded'] = self._explored
        return res
