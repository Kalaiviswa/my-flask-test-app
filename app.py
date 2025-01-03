from flask import Flask, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# Data storage (in-memory list for simplicity)
data = []

# GET route to retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": data})

# POST route to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    item = request.json  # Expecting JSON input
    if not item or 'name' not in item:
        return jsonify({"error": "Invalid input, 'name' field is required"}), 400
    data.append(item)
    return jsonify({"message": "Item added", "item": item}), 201

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
