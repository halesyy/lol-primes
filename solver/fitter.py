
import json
from py_expression_eval import Parser
from random import randint, gauss
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

def error(series, eq, x, y, iter_x=1):
    iter_x = iter_x
    running_error = 0
    for i, prime in enumerate(series):
        x_val = iter_x * x
        y_val = eval(eq, {"x": x_val, "y": y})
        if y_val == None: return 1000000000
        error = abs(y_val - prime)
        running_error += error
        iter_x += 1
    # print(eq, ":", running_error)
    return running_error

# Each x/y is ran through this matrix of addition,
# then the lowest error value is picked.
all_tests = [
    # [
    #     [0,     0],
    #     [0,     -10000],
    #     [-10000, 0],
    #     [10000,  0],
    #     [0,     10000]
    # ],
    # [
    #     [0,     0],
    #     [0,     -1000],
    #     [-1000, 0],
    #     [1000,  0],
    #     [0,     1000]
    # ],
    # [
    #     [0,     0],
    #     [0,     -100],
    #     [-100, 0],
    #     [100,  0],
    #     [0,     100]
    # ],
    # [
    #     [0,     0],
    #     [0,     -10],
    #     [-10, 0],
    #     [10,  0],
    #     [0,     10]
    # ],
    [
        [0,     0],
        [0,     -1],
        [-1, 0],
        [1,  0],
        [0,     1]
    ],
    [
        [0, 0],
        [0, -0.1],
        [-0.1, 0],
        [0.1, 0],
        [0, 0.1]
    ],
    # [
    #     [1, 1],
    #     [1, -1.1],
    #     [-1.1, 1],
    #     [1.1, 1],
    #     [0, 0.1]
    # ],
    [
        [0,     0],
        [0,     -0.01],
        [-0.01, 0],
        [0.01,  0],
        [0,     0.01]
    ],
    [
        [0,     0],
        [0,     -0.001],
        [-0.001, 0],
        [0.001,  0],
        [0,     0.001]
    ],
    # [ # A multiplier.
    #     [1,     1],
    #     [1,     0.999],
    #     [0.999, 1],
    #     [1.001,  1],
    #     [1,     1.001]
    # ],
    [
        [0,     0],
        [0,     -0.0001],
        [-0.0001, 0],
        [0.0001,  0],
        [0,     0.0001]
    ],
    [
        [0,     0],
        [0,     -0.00001],
        [-0.00001, 0],
        [0.00001,  0],
        [0,     0.00001]
    ],
    [
        # [0,     0],
        [0,     -0.000001],
        [-0.000001, 0],
        [0.000001,  0],
        [0,     0.000001]
    ],
    [
        # [0,     0],
        [0,     -0.0000001],
        [-0.0000001, 0],
        [0.0000001,  0],
        [0,     0.0000001]
    ],
    [
        # [0,     0],
        [0,     -0.00000001],
        [-0.00000001, 0],
        [0.00000001,  0],
        [0,     0.00000001]
    ],
    [
        # [0,     0],
        [0,     -0.000000001],
        [-0.000000001, 0],
        [0.000000001,  0],
        [0,     0.000000001]
    ]
]


def fit_for(all_primes, series_x, last_x=False, last_y=False):
    addit = all_primes[series_x-1][-1] if series_x != 0 else 0
    iter_x = (series_x*GROUP_PRIMES)+1
    # addit = all_primes[series_x][0] if series_x != 0 else 0

    # series = all_primes[0:series_x+1]
    series = all_primes[series_x]
    # full_series = []
    # for s in series:
    #     full_series += s
    # series = full_series

    eq = f"x*log(x,y)+{addit}" # Fix to prior y-plane.
    # eq = "x*log(x,y)"

    # x, y = 2, 6.6
    # x, y = 1, 1
    x = last_x if last_x != False else 1
    y = last_y if last_y != False else 1

    best_error_all = float("inf") # Everything is < than.
    # for i in range(10000):
    for tests in all_tests:
        hit_same = 0
        # print(">", tests)
        while True:
            subbed_tests = [[x+test[0], y+test[1]] for test in tests]
            test_errors = [error(series, eq, x=xy[0], y=xy[1], iter_x=iter_x) for xy in subbed_tests]
            best_index = test_errors.index(min(test_errors))
            best_error = min(test_errors)
            x, y = subbed_tests[best_index] # Replace x/y.
            x, y = float("{:.11f}".format(x)), float("{:.11f}".format(y))
            best_error = int(best_error)
            if best_error == best_error_all:
                hit_same += 1
            else:
                hit_same = 0
            if best_error < best_error_all:
                best_error_all = best_error
            if hit_same == 2:
                break
            # print(x, y, best_error)
            # print(best_error, best_error_all)
            # print(best_error_all, x, y)
    return best_error_all, x, y




if __name__ == "__main__":
    GROUP_PRIMES = 2

    from concurrent.futures import ThreadPoolExecutor

    # Intake primes.
    # primes = json.loads(open("../datasets/primes_1m_test.json", "r").read())
    primes = json.loads(open("../datasets/downloaded/1m_primes.json", "r").read())
    print(">", len(primes), "primes")
    primes = chunk(primes, GROUP_PRIMES)

    # Iter_x is hard-coded in fit-for.
    # for _ in range(100):
    #     rx, ry = randint(1, 10000), randint(1, 10000)
    #     rx, ry = abs(gauss(1, 10000)), abs(gauss(1, 10000))
    #     print(fit_for(primes, 52, last_x=rx, last_y=ry))
    # exit()

    # Step system for figuring out the best. Errors.
    results = []
    # results = json.loads(open("reports/place_fit_best_2.json", "r").read())

    is_done = [r["for"] for r in results]
    last_x, last_y = 1, 1
    for i in range(len(primes)):
        if i in is_done:
            # print("> skipping", i)
            continue
        # print("> starting", i, "/", len(primes))
        set_data = fit_for(primes, i, last_x=last_x, last_y=last_y)
        last_x, last_y = set_data[1:]
        results.append({"for": i, "err_x_y": set_data})
        print("> finished", i, "/", len(primes), "d:", set_data)

        if i % 100 == 0:
            open("reports/place_fit_best_2.json", "w").write(json.dumps(results, indent=4))
    open("reports/place_fit_best_2.json", "w").write(json.dumps(results, indent=4))
