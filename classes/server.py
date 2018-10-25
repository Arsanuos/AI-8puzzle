from flask import Flask, abort, request 
import json

app = Flask(__name__)


@app.route('/solve', methods=['GET'])
def solve():
    algorithm = request.args['algorithm']
    arr = request.args['input[]']
    if algorithm == "BFS":
        
    elif algorithm == "DFS":
    elif algorithm == "A start (Euclidean)":
    elif algorithm == "A start (Manhatten)"
    return "helloworld"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)