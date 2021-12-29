
import json
import matplotlib.pyplot as plt
from py_expression_eval import Parser

parser = Parser()

def eval(ex, sub={}):
    try:
        response = parser.parse(ex).evaluate(sub)
        return response
    except:
        return None

data = json.loads(open("reports/place_fit_best_2_7log.json", "r").read())

x_sub_eq = "3*log(x,7)"

# Recall: the given eq x*log(x,7) uses + addit
# of the prior primes. This could be a bias that
# we need to start from scratch. Or, it's the bias
# needed to understand the fundamental movements.

# Iter_x at the error count time adds 1 to itself
# each time. Iter_x is just a ledger of primex
# basically.

all_x_sup = []

for i, d in enumerate(data):
    # if i == 10000:
    #     break
    iter_x = (i*2)+1 # Passed into iter.
    err, x, y = d["err_x_y"]
    # print(f"> at iter_x: {iter_x}, x sub is {x}, meaning we run the series:")
    x_sup = [float("{:.5f}".format(i*x)) for i in range(iter_x, iter_x+2)]
    all_x_sup += x_sup
    # print(">", x_sup)
    # print()

all_x_sup = all_x_sup[0:25000]
mimic_x = [eval(x_sub_eq,{"x":i+1}) for i in range(len(all_x_sup))]

open("reports/interpret_x_real_sub.json", "w").write(json.dumps(all_x_sup))

plt.plot(range(len(all_x_sup)), all_x_sup, c="red")
plt.plot(range(len(mimic_x)), mimic_x, c="blue")
plt.show()
