
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
# primes = json.loads(open("../datasets/primes.json", "r").read())
primes = json.loads(open("../datasets/primes_test.json", "r").read())
# primes = primes[0:1000]
# primes = json.loads(open("../datasets/primes_1m_test.json", "r").read())
# primes = json.loads(open("../datasets/downloaded/1m_primes.json", "r").read())
print(">", len(primes), "total primes")

# The equation itself, woo!
eq = "x*log(x, 7)"
eq = "x*log(3*log(x, 7), 7)"

iter_by = 7
iter_x = 1
y_eq_sub = 7

# Setup
iterations = len(primes)
primes = primes[0:iterations]
created_primes = []

# Create copy dataset.
diffs = ""
diffs_to_plot = []
err_set = 0
for i, ypm in zip(range(iterations), primes):
    x_val = iter_x*iter_by
    y_val = eval(eq, {"x": x_val, "y": y_eq_sub})
    # y_val = round(y_val) # test this
    diff = abs(y_val - ypm)
    plt_diff = y_val - ypm
    err_set += diff
    # if i % 30 == 0:
    diffs += f"{i}\t{plt_diff}\n"
    diffs_to_plot.append(plt_diff)
    # y_val *= -1
    created_primes.append(y_val)
    iter_x += 1 # +Inc.

print("> err:", err_set)
open("diffs.txt", "w").write(diffs)

plt.plot(range(len(primes)), primes, c="red")
plt.plot(range(len(created_primes)), created_primes, c="blue")
plt.show()

# plt.plot(range(len(diffs_to_plot)), diffs_to_plot)
# plt.show()
