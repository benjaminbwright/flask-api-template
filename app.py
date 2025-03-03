from flask import Flask, jsonify
from todo_routes import todo_bp  # Import the blueprint for todo routes

# Create a Flask application instance
app = Flask(__name__)

# Register the todo blueprint with a URL prefix
# This means all routes in todo_routes.py will be prefixed with /api
app.register_blueprint(todo_bp, url_prefix='/api')

@app.route('/')
def index():
    """
    Define the root route of the application.
    This route returns a simple JSON message.
    """
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    # Run the Flask application in debug mode
    # Debug mode allows for automatic reloading and better error messages
    app.run(debug=True)