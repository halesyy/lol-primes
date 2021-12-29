
from math import log
from time import time

ts = time()
iter_by = 0.0001
start_at = 1
base = 2

report = ""

for i in range(10_000_000):
    res = log(i+1, base)
    start_at += iter_by
    td = time() - ts
    if i % 100 == 0:
        report += f"{i}\t{res}\t{td}\n"

open("report.txt", "w").write(report)
