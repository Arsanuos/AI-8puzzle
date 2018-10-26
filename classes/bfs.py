from agent import Agent
from state import State


class BFS(Agent):

    def search(self, initial_state):
        curr_state = State(initial_state, None)
        frontier = [curr_state]
        while frontier:
            curr_state = frontier.pop(0)
            self.vis.add(curr_state)
            if curr_state.is_goal():
                break
            children = self.expand(curr_state)
            for child in children:
                #if child not in frontier:
                frontier.append(child)

        steps = self.get_steps(curr_state)
        return steps
