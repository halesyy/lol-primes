
import json
from py_expression_eval import Parser
from random import randint, choice

primes = json.loads(open("../datasets/primes.json", "r").read())

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
        "/",
        "^",
        "%"
    ],
    "attachments": [
        "sin(x)",
        "cos(x)",
        "tan(x)",
        "log(x, y)",
        "log(x)",
        "e",
        "pi"
    ]
}

mp = Parser()
eval = lambda ex, sub={}: mp.parse(ex).evaluate(sub)

v1 = eval("5*2*x", {"x": 5})

def make_strand(length):
    strand = ["a"]
    for _ in range(length):
        allow_g = strand[-1] == "a"
        if allow_g:
            strand.append(choice(["a", "g"]))
        else:
            strand.append("a")
    if strand[-1] == "g":
        strand = strand[0:-1]
    return strand


def make_eq():
    # make line of aaagaaaga where
    # g can only be between a, like DNA
    # can we have a 4-type? brackets? bo/bc?
    length = randint(1, 100)
    strand = make_strand(length)


make_eq()
