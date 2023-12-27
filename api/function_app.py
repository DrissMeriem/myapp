import azure.functions as func
import numpy as np
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="numericalintegralservice")
def numerical_integral_service(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        lower = float(req.params.get('lower'))
        upper = float(req.params.get('upper'))
    except ValueError:
        return func.HttpResponse("Invalid input. Please provide valid 'lower' and 'upper' parameters.", status_code=400)

    results = {}

    for N in [10, 100, 1000, 10000, 100000, 1000000]:
        results[N] = num_integ(N, lower, upper)

    return func.HttpResponse(
        body=json.dumps(results),
        mimetype="application/json",
        status_code=200
    )

def num_integ(N, lower, upper):
    eps = (upper - lower) / N
    x_values = np.linspace(lower, upper - eps, N)
    rect_values = np.abs(np.sin(x_values)) * eps
    result = np.sum(rect_values)
    return result
