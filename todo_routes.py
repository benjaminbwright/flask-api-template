from flask import Blueprint, jsonify, request

todo_bp = Blueprint('todo', __name__)

# In-memory data store for todos
todos = []

@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@todo_bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    todo = {
        'id': len(todos) + 1,
        'task': data.get('task'),
        'completed': False
    }
    todos.append(todo)
    return jsonify(todo), 201

@todo_bp.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo)

@todo_bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    data = request.get_json()
    todo['task'] = data.get('task', todo['task'])
    todo['completed'] = data.get('completed', todo['completed'])
    return jsonify(todo)

@todo_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({'message': 'Todo deleted'}) 