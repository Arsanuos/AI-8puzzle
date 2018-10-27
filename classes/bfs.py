from agent import Agent
from state import State


class BFS(Agent):

    def __init__(self):
        super().__init__()
        self.__optimize_flag = True

    def search(self, initial_state):
        curr_state = State(initial_state, None)
        frontier = [curr_state]
        while frontier:
            curr_state = frontier.pop(0)
            self.vis.add(curr_state)
            if curr_state.is_goal():
                break
            children = self.expand(curr_state, self.__optimize_flag)
            for child in children:
                #if child not in frontier:
                frontier.append(child)

        steps = self.get_steps(curr_state)
        res = {}
        res['steps'] = steps
        res['cost'] = curr_state.cost
        res['search_depth'] = curr_state.cost
        res['nodes_expanded'] = len([node for node in vis if node not in frontier])
        return steps
