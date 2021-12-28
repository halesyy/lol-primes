
import json

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

# Intake primes.
primes = json.loads(open("../datasets/primes_1m_test.json", "r").read())
primes = chunk(primes, 100)
print(">", len(primes), "primes")

# Step system for figuring out the best. Errors.
