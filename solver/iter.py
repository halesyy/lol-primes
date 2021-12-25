
import json
from py_expression_eval import Parser
from random import randint, choice, random

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
            strand.append(choice(["a", "s"]))
        elif last == "a":
            # Attachment.
            strand.append(choice(["g"]))
        elif last == "s":
            # Substitutable.
            strand.append(choice(["g"]))

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
        return None
    else:
        return equation


if __name__ == "__main__":
    while True:
        eq = make_eq()
        print(eq)
