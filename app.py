import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

def num_integ(N, lower, upper):
    eps = (upper - lower) / N
    x_values = np.linspace(lower, upper - eps, N)
    rect_values = np.abs(np.sin(x_values)) * eps
    result = np.sum(rect_values)
    return result

def calculate_integral(lower, upper):
    integration_results = {
        N: num_integ(N, lower, upper) for N in [10, 100, 1000, 10000, 100000, 1000000]
    }
    return integration_results

@app.route('/numericalintegralservice', methods=['GET'])
def numerical_integral_service():
    try:
        lower = float(request.args.get('lower', 0.0))
        upper = float(request.args.get('upper', 1.0))

        results = calculate_integral(lower, upper)

        return render_template('index.html', lower=lower, upper=upper, integration_method='Rectangular Rule', results=results)

    except ValueError as e:
        return render_template('error.html', error='Invalid input. Please provide valid numeric values for lower and upper.'), 400
    except Exception as e:
        return render_template('error.html', error='An unexpected error occurred.'), 500

if __name__ == "__main__":
    app.run(debug=True)

