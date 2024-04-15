from flask import Flask, request, jsonify
from flask_cors import CORS
from solver import solve_clingo_program

app = Flask(__name__)
CORS(app)

@app.route('/ground', methods=['POST'])
def ground_clingo():
    # Receive Clingo code from the request body
    clingo_code = request.json.get('clingo_code')

    # Solve the clingo code
    grounded_code = solve_clingo_program(clingo_code)

    response = jsonify({'grounded_code': grounded_code})

    response.headers.add('Access-Control-Allow-Origin', '*')

    # Return the grounded code
    return response

if __name__ == '__main__':
    app.run(debug=True)
