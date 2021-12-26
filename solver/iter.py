
import json
import matplotlib.pyplot as plt
from time import sleep
from py_expression_eval import Parser
from random import randint, choice, random, gauss

primes = json.loads(open("../datasets/primes.json", "r").read())
primes_diff = json.loads(open("../datasets/primes_diff.json", "r").read())
primes_diff_diff = json.loads(open("../datasets/primes_diff_diff.json", "r").read())
primes_diff_diff_diff = json.loads(open("../datasets/primes_diff_diff_diff.json", "r").read())
primes_diff_diff_diff_diff = json.loads(open("../datasets/primes_diff_diff_diff_diff.json", "r").read())

# Current state:
# https://www.quora.com/Could-you-train-a-machine-learner-to-predict-the-next-prime-number-I-know-there-is-no-pattern-to-PNs-I-am-wondering-if-the-ML-would-figure-it-out

# Conceptions:
# - Are primes a graphical pattern?
# - If they follow a pattern, where is it?
# - If they don't follow a pattern, there's no chance.
# - Miller-Rabin primariliy test. Fermat primality test. See what tools they use.
# - Diff between:
#   1. Predicting the next prime.
#   2. Classifying a number as a prime.
# - Regarding dist of primes, for n, the # of primes
#   below it is ~ 1/ln(n), natural log. Eulers number. Interesting.

# Solve for:
# - fx = x first.
# - fx = 2x second.
# - fx = next prime. (lol)

meta = {
    "glue": [
        "+",
        "-",
        "*",
        "*",
        "*",
        "*",
        "*",
        "/",
        "/",
        "/",
        "/",
        "^",
        "%"
    ],

    # make sure:
    # possible to re-involve equation, by
    # placing the equation itself into x, or
    # attaching it
    "attachments": [
        "E",
        "PI",
        "x"
    ],
    "substitutable": [
        "sin(x)",
        "cos(x)",
        "tan(x)",
        "log(x, y)",
        "log(x)",
    ]
}

mp = Parser()

def eval(ex, sub={}):
    try:
        response = mp.parse(ex).evaluate(sub)
        return response
    except:
        return None

def make_strand(length):
    strand = ["a"]
    for _ in range(length):
        last = strand[-1]

        if last == "g":
            # Glue item.
            strand.append(choice(["a", "s", "c"]))
        elif last == "a":
            # Attachment.
            strand.append(choice(["g"]))
        elif last == "s":
            # Substitutable.
            strand.append(choice(["g"]))
        elif last == "c":
            strand.append(choice(["a", "s", "g"]))

    if strand[-1] == "g":
        strand = strand[0:-1]
    return strand

def supplement(strand):
    given_eq = ""
    for i, item in enumerate(strand):
        last = False if i == 0 else strand[i-1]
        if item == "a":
            # Attachments.
            given_eq += choice(meta["attachments"])
        elif item == "g":
            # Glue.
            given_eq += choice(meta["glue"])
        elif item == "s":
            if random() < 0.5 and last != "g":
                # Place the equation in x.
                given_eq += choice(meta["glue"])

                # Place prior given eq as "x" in sub.
                sub = choice(meta["substitutable"])
                sub = sub.replace("x", given_eq)
                given_eq = sub + " "
                # given_eq += choice(meta["glue"])
                # given_eq += choice(meta["attachments"])
            else:
                # Append the substitute itself. Nothing bad.
                given_eq += choice(meta["substitutable"])
        elif item == "c":
            cons = gauss(0, 100) # a = base, b = variance
            # cons = random()*randint(-10000,10000)
            given_eq += str(cons)

        given_eq += " "
    return given_eq

# WE STILL NEED TO ADD RANDOM CONSTANTS!!!!!

def make_eq():
    # make line of aaagaaaga where
    # g can only be between a, like DNA
    # can we have a 4-type? brackets? bo/bc?
    length = randint(1, 100)
    # length = 10
    strand = make_strand(length)
    equation = supplement(strand)
    # Great.
    response = eval(equation, {"x": 1, "y": 2})
    if response == None:
        # print(equation)
        # print()
        return None
    else:
        return equation

best_error = 1000000000

def series_explode(eq):
    global best_error

    # All series to test.
    test_series = [
        primes,
        primes_diff,
        primes_diff,
        primes_diff_diff,
        primes_diff_diff_diff
    ]

    # Iterate.
    for _ in range(4): # 20. Computationally hyper-expensive.
        for sx, series in enumerate(test_series): # do random series 10k times
            # Setting up randoms.
            iter_by = gauss(0, 10) if random() < 0.5 else randint(-50, 50) # 0.zf9q2809as or -50>50
            iter_x = 1
            x = []
            y = []
            # Build XY sequence for comparison to series.
            y_eq_sub = gauss(0, 100)
            for _ in range(len(series)):
                x_val = iter_x*iter_by
                x.append(x_val)
                y_val = eval(eq, {"x": x_val, "y": y_eq_sub})
                if y_val == None:
                    y_val = 0
                y.append(y_val)
                iter_x += 1
            # Compare to series. Use percentage differences.
            error = 0
            # error = []
            for i, created_y_real_y in enumerate(zip(y, series)):
                if i == 0:
                    continue
                # Pack in the last cy, and the cy now. Ry too.
                cy, ry = created_y_real_y
                last_cy, last_ry = y[i-1], series[i-1]
                # Calculate the absolute percentage error.
                try:
                    real_cdiff = (cy/last_cy)-1 # Created.
                    real_rdiff = (ry/last_ry)-1 # Real.
                    perc_err = abs(real_cdiff - real_rdiff)
                    # perc_err = abs((real_cdiff/real_rdiff)-1)
                    # ind_error = abs(cy - ry)
                    # perc_err =
                except:
                    return False
                # error.append(perc_err)
                error += perc_err
            # Check compared.
            # ape_score = sum(error)/len(error)
            ape_score = error
            if ape_score < best_error:
                best_error = ape_score
                print(f"> new b/e: {ape_score}. eq: {eq}, iter_by: {iter_by}, y_eq_sub: {y_eq_sub}, series 0-5: {series[0:5]} ({sx})")

if __name__ == "__main__":

    # eqs = [make_eq() for _ in range(1000)]

    while True:
        eq = make_eq()
        # eq = "PI + x * -77.10565555763374"
        if eq != None:
            series_explode(eq)
    # print(eq)

    # print(sum([True for e in eqs if e == None]))
    #     if eq != None:
    #         print(eq)
            # sleep(0.1)
