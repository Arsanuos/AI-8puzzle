from dfs import DFS
from bfs import BFS


def print_steps(steps_sol):
    for s in steps_sol:
        print("================================")
        for i in range(0, 9, 3):
            print(s[i:i + 3])


agent = DFS()
steps = agent.search([1, 2, 5, 3, 4, 0, 6, 7, 8])
print_steps(steps)

agent = BFS()
steps = agent.search([1, 2, 0, 3, 4, 5, 6, 7, 8])
print_steps(steps)
