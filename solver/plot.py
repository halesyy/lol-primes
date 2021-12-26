
import matplotlib.pyplot as plt
import json
from py_expression_eval import Parser

mp = Parser()

def eval(ex, sub={}):
    try:
        response = mp.parse(ex).evaluate(sub)
        return response
    except:
        return None

# Data iq for iteration.
primes = json.loads(open("../datasets/primes_test.json", "r").read())
print(">", len(primes), "total primes")
# eq = "E + x * log(x, y)"
eq = "E ^ cos(x) + E * x"
# eq = "x / PI - 15.915067868739133 * cos(x) / 178.76112787388675"
# eq = "x + E"

# Equation setup.
iter_by = -3.0880716533709633
# iter_by = 1.4
iter_x = 1
# y_eq_sub = 1.4
y_eq_sub = -0.4211548856081214

# Setup
iterations = len(primes)
primes = primes[0:iterations]
created_primes = []

# Create copy dataset.
for _ in range(iterations):
    x_val = iter_x*iter_by
    y_val = eval(eq, {"x": x_val, "y": y_eq_sub})
    y_val *= -1
    created_primes.append(y_val)
    iter_x += 1 # +Inc.

plt.plot(range(len(primes)), primes, c="red")
plt.plot(range(len(created_primes)), created_primes, c="blue")
plt.show()
