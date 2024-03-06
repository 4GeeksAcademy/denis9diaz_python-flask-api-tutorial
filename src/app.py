from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "Do homework", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    body = request.json
    todos.append(body)
    print("Incoming request with the following body", body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):
        del todos[position]
        return jsonify(todos)
    else:
        return jsonify({"error": "Invalid position"}), 400

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
