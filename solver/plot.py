
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
primes = json.loads(open("../datasets/primes.json", "r").read())
eq = "E + x * log(x, y)"

# Equation setup.
iter_by = 0.8323181983046214
iter_x = 1
y_eq_sub = 2.0223733769290027

# Setup
iterations = 1000
primes = primes[0:iterations]
created_primes = []

# Create copy dataset.
for _ in range(iterations):
    x_val = iter_x*iter_by
    y_val = eval(eq, {"x": x_val, "y": y_eq_sub})
    created_primes.append(y_val)
    iter_x += 1 # +Inc.

plt.plot(range(len(primes)), primes, c="red")
plt.plot(range(len(created_primes)), created_primes, c="blue")
plt.show()
