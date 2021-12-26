import json
data = str(open("primes1.txt", "r").read()).strip()
data = data.split("\n")
data = [[int(c) for c in r.split(" ") if c != ""] for r in data]
primes = []
for r in data:
    primes += r
open("1m_primes.json", "w").write(json.dumps(primes))
