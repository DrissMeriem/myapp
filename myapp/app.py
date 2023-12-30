import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

def num_integ(N, lower, upper):
    eps = (upper - lower) / N
    x_values = np.linspace(lower, upper - eps, N)
    rect_values = np.abs(np.sin(x_values)) * eps
    result = np.sum(rect_values)
    return result

@app.route('/numericalintegralservice', methods=['GET'])
def numerical_integral_service():
    lower = float(request.args.get('lower'))
    upper = float(request.args.get('upper'))

    results = {}
    
    for N in [10, 100, 1000, 10000, 100000, 1000000]:
        results[N] = num_integ(N, lower, upper)

    return jsonify(results)

if __name__ == "__main__":
    app.run()
