
import json
from time import sleep
from py_expression_eval import Parser
from math import ceil, floor
parser = Parser()
primes = json.loads(open("../datasets/primes_1m_test.json", "r").read())
# primes = json.loads(open("../datasets/primes.json", "r").read())
primes = primes[0:3687]

print(">", len(primes), "total primes")
# exit()

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
eq = "x * log(x, y)"

# Best for first 1,229 primes: 1.8778, 5.9901, err = 23,273.
# Best for first 2,458 primes: 3.0000, 20.250, err = 135,719.
# Best for first 3,687 primes:

def error(eq, x, y):
    # X = iter by. Running * x.
    # Y = y_sub.
    # diffs = ""
    iter_x = 1
    running_error = 0
    for i, prime in enumerate(primes):
        x_val = iter_x * x
        y_val = eval(eq, {"x": x_val, "y": y})
        if y_val == None: return ""
        # y_val = floor(y_val)
        error = abs(y_val - prime)
        running_error += error
        iter_x += 1
    return running_error

# print(error(eq, 1.88, 6))
# exit()

# A generator which can yield parameters,
# for a lower memory footprint.
def make_params_old(dec_div, iter_range):
    iter_by = 1/dec_div
    params = []
    x_plot, y_plot = 0, 0
    for x in range(1, (iter_range*dec_div)+1):
        x = x/dec_div
        for y in range(0, (iter_range*dec_div)+1):
            y = y/dec_div
            yield (x, y, x_plot, y_plot)
            y_plot += 1
        x_plot += 1

#
def make_params(x_root, y_root, spread_by, spread_iters):
    total_distance = spread_by*spread_iters
    running_x = x_root - total_distance
    running_y = y_root - total_distance
    x_plot, y_plot = 0, 0
    for x in range(spread_iters*2+1):
        for y in range(spread_iters*2+1):
            yield (running_x, running_y, x_plot, y_plot)
            running_y += spread_by
            y_plot += 1
        running_x += spread_by
        running_y = y_root - total_distance # Reset.
        x_plot += 1

# for row in make_params(0, 0, 0.1, 10):
#     print(row)
# exit()





p_log = []
# Iterate, and calculate the error.
for i, param in enumerate(make_params(4, 61, 0.1, 5)):
    x_val, y_val, x, y = param
    err = error(eq, x_val, y_val)
    # err = error(eq, x, y)
    p_log.append([x_val, y_val, x, y, err])

# Save param log.
open("reports/params.json", "w").write(json.dumps(p_log, indent=4))

# Convert p_log into the tsv sheet.
report = []
report_x = []
report_y = []
for row in p_log:
    x, y, plot_x, plot_y, err = row
    row_x = plot_x+1
    if len(report) < row_x:
        report.append([])
    report[plot_x].append(str(err))
    x = float("{:.7f}".format(x))
    y = float("{:.7f}".format(y))
    if str(x) not in report_x:
        report_x.append(str(x))
    if str(y) not in report_y:
        report_y.append(str(y))
report = ["\t".join(r) for r in report]
report = "\n".join(report)
report_x = "\n".join(report_x)
report_y = "\t".join(report_y)
open("reports/params.tsv", "w").write(report)
open("reports/params_x.tsv", "w").write(report_x)
open("reports/params_y.tsv", "w").write(report_y)
