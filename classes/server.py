from flask import Flask, request, jsonify
from bfs import BFS
from dfs import DFS
from manhatten import Manhatten
from euclidean import Euclidean
from aStar import AStar
import timeit

app = Flask(__name__)


@app.route('/solve', methods=['GET'])
def solve():
    """
        Solve the puzzle by getting the required parameters from the request args.
    """
    algorithm = request.args['algorithm']
    arr = list(map(int, request.args['input[]'][1:-1].split(',')))
    print(algorithm)
    agent = None
    if algorithm == "BFS":
        agent = BFS()
    elif algorithm == "DFS":
        agent = DFS()
    elif algorithm == "A start (Euclidean)":
        agent = AStar(Euclidean)
    elif algorithm == "A start (Manhatten)":
        agent = AStar(Manhatten)
    else:
        return arr

    start = timeit.default_timer()
    res = agent.search(arr)
    end = timeit.default_timer()

    res['time'] = end - start

    ret = jsonify(res)
    return ret


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
