from dfs import DFS

agent = DFS()

steps = agent.search([1, 2, 5, 3, 4, 0, 6, 7, 8])


def print_util(arr):
    print("================================")
    for i in range(0, 9, 3):
        print(arr[i:i + 3])


for s in steps:
    print_util(s.current)
