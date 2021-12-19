
import json

primes = []
dc = [2,3,5,7,11] # Base.

def is_prime(n):
    global divide_checks
    if n == 0 or n == 1:
        return False
    # Quick divide checks.
    qdc = [x for x in dc if x != n]
    for d in qdc:
        if n % d == 0:
            return False
    return True

for i in range(10000):
    if is_prime(i):
        dc.append(i) # Since prime. Divide checks.
        primes.append(i)

open("primes.json", "w").write(json.dumps(primes))