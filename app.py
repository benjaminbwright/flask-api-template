from flask import Flask, jsonify
from todo_routes import todo_bp  # Import the blueprint

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(todo_bp, url_prefix='/api')

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)