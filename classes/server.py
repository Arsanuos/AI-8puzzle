from flask import Flask, request, jsonify
from bfs import BFS
from dfs import DFS
from manhatten import Manhatten
from euclidean import Euclidean
from aStar import AStar
import json

app = Flask(__name__)


@app.route('/solve', methods=['GET'])
def solve():
    algorithm = request.args['algorithm']
    arr = list(map(int, request.args['input[]'][1:-1].split(',')))
    if algorithm == "BFS":
        bfs = BFS()
        output = bfs.search(arr)
        print(output)
        return jsonify({'steps': output})
    elif algorithm == "DFS":
        dfs = DFS()
        return jsonify({'steps': dfs.search(arr)})
    elif algorithm == "A start (Euclidean)":
        agent = AStar(Euclidean)
        return jsonify({'steps': agent.search(arr)})
    elif algorithm == "A start (Manhatten)":
        agent = AStar(Manhatten)
        return jsonify({'steps': agent.search(arr)})
    return arr


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)