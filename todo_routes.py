from flask import Blueprint, jsonify, request

# Create a Blueprint for the todo routes
# This allows for modular routing in the Flask application
todo_bp = Blueprint('todo', __name__)

# In-memory data store for todos
# This is a simple list to store todo items temporarily
todos = []

@todo_bp.route('/todos', methods=['GET'])
def get_todos():
    """
    Retrieve all todo items.
    Returns a JSON list of all todos.
    """
    return jsonify(todos)

@todo_bp.route('/todos', methods=['POST'])
def create_todo():
    """
    Create a new todo item.
    Expects a JSON payload with a 'task' field.
    Returns the created todo item with a unique ID.
    """
    data = request.get_json()
    todo = {
        'id': len(todos) + 1,  # Assign a new ID based on the current list length
        'task': data.get('task'),  # Get the task description from the request
        'completed': False  # Default the completed status to False
    }
    todos.append(todo)  # Add the new todo to the list
    return jsonify(todo), 201  # Return the created todo with a 201 status code

@todo_bp.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """
    Retrieve a specific todo item by its ID.
    Returns the todo item if found, otherwise a 404 error.
    """
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo)

@todo_bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    Update a specific todo item by its ID.
    Expects a JSON payload with optional 'task' and 'completed' fields.
    Returns the updated todo item if found, otherwise a 404 error.
    """
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    data = request.get_json()
    todo['task'] = data.get('task', todo['task'])  # Update the task if provided
    todo['completed'] = data.get('completed', todo['completed'])  # Update the completed status if provided
    return jsonify(todo)

@todo_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """
    Delete a specific todo item by its ID.
    Returns a success message if the todo was deleted.
    """
    global todos
    todos = [t for t in todos if t['id'] != todo_id]  # Remove the todo from the list
    return jsonify({'message': 'Todo deleted'}) 