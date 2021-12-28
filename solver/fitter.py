
import json
from py_expression_eval import Parser
parser = Parser()

# Given n primes, say, the primes from
# 1-100, we want to figure out what the
# values of X/Y are in order to plot that.
# X, of course, is the iter step we use.
# Y, of course, is the log base we use.

# Then, after we've adjusted for that, we
# wish to deduce from 101-200 the same info,
# so that we can plot the causal changes that
# are to take place over 100 primes step-by-
# step. To do this, we'll have to add a + lp,
# where lp = the last prime in the prior set.

# Long-term goal: once we've got a well-fit
# equation that plots along with primes acceleration,
# we can start to ask deeper questions, such as the
# total # of primes under a given number, and get
# a very high confidence.

def chunk(li, amt=100):
    chunks = []
    for i in range(0, len(li), amt):
        chunks.append(li[i:i+amt])
    return chunks

def eval(eq, sub):
    try:
        return parser.parse(eq).evaluate(sub)
    except:
        return None

def error(series, eq, x, y):
    iter_x = 1
    running_error = 0
    for i, prime in enumerate(series):
        x_val = iter_x * x
        y_val = eval(eq, {"x": x_val, "y": y})
        if y_val == None: return ""
        error = abs(y_val - prime)
        running_error += error
        iter_x += 1
    print(eq, ":", running_error)
    return running_error

# Each x/y is ran through this matrix of addition,
# then the lowest error value is picked.
tests = [
    [0,     0],
    [0,     -0.01],
    [-0.01, 0],
    [0.01,  0],
    [0,     0.01]
]

def fit_for(all_primes, series_x):
    addit = all_primes[series_x-1][-1] if series_x != 0 else 0
    series = all_primes[series_x]
    eq = f"x*log(x,y)+{addit}"
    x, y = 2, 2


    print(error(series, eq, x, y))



# Intake primes.
primes = json.loads(open("../datasets/primes_1m_test.json", "r").read())
print(">", len(primes), "primes")
primes = chunk(primes, 100)

# Step system for figuring out the best. Errors.
fit_for(primes, 1)
