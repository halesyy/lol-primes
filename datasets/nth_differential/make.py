
import json
import matplotlib.pyplot as plt
import numpy

get_diff = lambda li: list(numpy.diff(li))

# Load primes.
primes = json.loads(open("../primes_1m_test.json", "r").read())
# primes = json.loads(open("../downloaded/1m_primes.json", "r").read())
# How many differential layers we want to descend.
# nth_diff = 500


nth_diff = 250
subsect_at = 100

# Gather primes, and start diffing.
primes = primes[0:nth_diff]

diffs = [primes] # Abs diffs.
raw_diffs = [primes]
direct = [[]] # 1 or -1.

for x in range(nth_diff-1):
    # Make diff sets.
    diffd = get_diff(diffs[-1]) # Raw set. No abs changes.
    diffr = [abs(d) for d in diffd] # To-add set. Absolute.
    diffs.append(diffr)
    raw_diffs.append(diffd)
    # Make directions.
    tmp_dir = []
    for i, diff in enumerate(diffd):
        if i == 0:
            continue
        last_diff = diffd[i-1]
        # if x == 4 and i < 12:
        #     print(last_diff, "\t", diff)
        dirc = 1 if diff > last_diff else -1
        dirc = 0 if diff == last_diff else dirc
        tmp_dir.append(dirc)
    direct.append(tmp_dir)

print(raw_diffs[4][0:10])
print(diffs[4][0:10])
print(direct[4][0:10])

plt.bar(range(len(diffs[100])), diffs[100])
plt.show()




# y = [d[0] for d in diffs]
# plt.plot(range(len(y)), y)
# plt.show()

# to_plot = []

# for nth_diff in range(1500):
#     nth_diff = nth_diff + 1
#     # primes = primes[0:nth_diff]
#     working_diff = [p for p in primes[0:nth_diff]]
#     # print(nth_diff, len(working_diff))
#     for i in range(nth_diff):
#         # over_2 = True if len([True for p in working_diff if p > 2]) > 0 else False
#         # if over_2:
#         #     print(f"> {i} @ nth_diff {nth_diff} is over 2")
#         over_2 = False
#         if i >= nth_diff-10:
#             print(f"> First 10 diffs at n={i}: {list(working_diff[0:10])} {over_2}")
#         working_diff = numpy.diff(working_diff)
#         working_diff = [abs(p) for p in working_diff]
#         to_plot.append([range(len(working_diff)), working_diff])
#     print()



# Non-up curves differentiate into +infinity as they are given
# nth diff complexities, whereas a positive/basic curve's diffs
# will create a static line (y=x), or devolve to 0 (y=log(x)).

# Big difference between absolute differencing, and normative
# differencing, I'm guessing there's also a random negative flip
# as well in this iteration.

# Given differential, it seems like at a deep derivation, it goes:
# 1, [0/2], and each step is [-/+].
# --
# So, a good example would be:
# 1, 2, 2, 0, 0, 2
# Where all 2's, have a matrix of *1 or *-1.

# to_plot.reverse()
# for x, y in to_plot:
#     plt.plot(x, y)
# plt.show()
