from agent import Agent
from state import State


class DFS(Agent):

    def __init__(self):
        super().__init__()
        self.__optimize_flag = True

    def search(self, initial_state):
        res = {}
        start = State(initial_state, None)
        frontier = [start]
        final_state = None
        while frontier:
            state = frontier.pop()
            self.vis.add(state)
            if state.is_goal():
                final_state = state
                break
            neighbours = self.expand(state, self.__optimize_flag)
            for neighbour in neighbours:
                #if neighbour not in frontier:
                frontier.append(neighbour)

        steps = self.get_steps(final_state)
        res['steps'] = steps
        res['cost'] = final_state.cost
        res['search_depth'] = final_state.cost
        res['nodes_expanded'] = len([node for node in vis if node not in frontier])
        return res
