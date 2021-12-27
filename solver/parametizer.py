
import json
from time import sleep
from py_expression_eval import Parser
parser = Parser()
primes = json.loads(open("../datasets/primes.json", "r").read())
def eval(eq, sub):
    try:
        return parser.parse(eq).evaluate(sub)
    except:
        return None

"""
Job: given an eq, test out all x/y
combinations/parameters, then compare
with an error function to a given series.
Then, plot the results.
"""

# Equation used.
eq = "E + x * log(x, y)"

def error(eq, x, y):
    # X = iter by. Running * x.
    # Y = y_sub.
    iter_x = 1
    running_error = 0
    for i, prime in enumerate(primes):
        x_val = iter_x * x
        y_val = eval(eq, {"x": x_val, "y": y})
        if y_val == None: return 1000000000
        error = abs(y_val - prime)
        running_error += error
        iter_x += 1
    return running_error

# A generator which can yield parameters,
# for a lower memory footprint.
def make_params(dec_div, iter_range):
    iter_by = 1/dec_div
    params = []
    for x in range(1, (iter_range*dec_div)+1):
        x_val = x/dec_div
        for y in range(0, (iter_range*dec_div)+1):
            y_val = y/dec_div
            yield (x_val, y_val, x, y)

p_log = []
# Iterate, and calculate the error.
for i, param in enumerate(make_params(10, 10)):
    x_val, y_val, x, y = param
    err = error(eq, x, y)
    p_log.append([x_val, y_val, x, y])

# Save param log.
open("reports/params.json", "w").write(json.dumps(p_log, indent=4))
