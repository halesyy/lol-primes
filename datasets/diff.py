import json
import matplotlib.pyplot as plt
primes = json.loads(open("primes.json", "r").read())
diff_set = []
for i, prime in enumerate(primes):
    if i == 0:
        continue
    last_prime = primes[i-1]
    prime_diff = prime - last_prime
    diff_set.append(prime_diff)
plt.plot(range(len(diff_set)), diff_set)
plt.show()
open("primes_diff.json", "w").write(json.dumps(diff_set))
