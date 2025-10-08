from flask import Flask, jsonify

app = Flask(__name__)

# Calculator functions
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Routes
@app.route('/')
def home():
    return jsonify({'message': 'Calculator API is running!', 'status': 200})

@app.route('/add/<a>/<b>')
def add_route(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify({'status': 400, 'result': 'Invalid numbers'})
    return jsonify({'status': 200, 'result': add(a, b)})

@app.route('/minus/<a>/<b>')
def minus_route(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify({'status': 400, 'result': 'Invalid numbers'})
    return jsonify({'status': 200, 'result': minus(a, b)})

@app.route('/multiply/<a>/<b>')
def multiply_route(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify({'status': 400, 'result': 'Invalid numbers'})
    return jsonify({'status': 200, 'result': multiply(a, b)})

@app.route('/divide/<a>/<b>')
def divide_route(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify({'status': 400, 'result': 'Invalid numbers'})
    if b == 0:
        return jsonify({'status': 400, 'result': 'Division by zero'})
    return jsonify({'status': 200, 'result': divide(a, b)})

# Export the Flask app for Vercel
if __name__ == '__main__':
    app.run(debug=True)
