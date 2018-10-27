from agent import Agent
from state import State


class DFS(Agent):

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

            neighbours = self.expand(state)
            for neighbour in neighbours:
                #if neighbour not in frontier:
                frontier.append(neighbour)

        steps = self.get_steps(final_state)
        res['steps'] = steps
        res['cost'] = final_state.cost
        res['search_depth'] = final_state.cost
        res['nodes_expanded'] = len(self.vis)
        return res
