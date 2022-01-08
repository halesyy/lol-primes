
import json
import matplotlib.pyplot as plt
import numpy

# Load primes.
primes = json.loads(open("../primes_1m_test.json", "r").read())
# primes = json.loads(open("../downloaded/1m_primes.json", "r").read())


# How many differential layers we want to descend.
# nth_diff = 500

to_plot = []

for nth_diff in range(1500):
    nth_diff = nth_diff + 1
    # primes = primes[0:nth_diff]
    working_diff = [p for p in primes[0:nth_diff]]
    # print(nth_diff, len(working_diff))
    for i in range(nth_diff):
        # over_2 = True if len([True for p in working_diff if p > 2]) > 0 else False
        # if over_2:
        #     print(f"> {i} @ nth_diff {nth_diff} is over 2")
        over_2 = False
        if i >= nth_diff-10:
            print(f"> First 10 diffs at n={i}: {list(working_diff[0:10])} {over_2}")
        working_diff = numpy.diff(working_diff)
        working_diff = [abs(p) for p in working_diff]
        to_plot.append([range(len(working_diff)), working_diff])
    print()

# Non-up curves differentiate into +infinity as they are given
# nth diff complexities, whereas a positive/basic curve's diffs
# will create a static line (y=x), or devolve to 0 (y=log(x)).

# Big difference between absolute differencing, and normative
# differencing, I'm guessing there's also a random negative flip
# as well in this iteration.

# to_plot.reverse()
# for x, y in to_plot:
#     plt.plot(x, y)
# plt.show()
