
import json
import matplotlib.pyplot as plt

# plot_data = json.loads(open("reports/place_fit_best_2.json", "r").read())
plot_data = json.loads(open("reports/place_fit_best_2_7log.json", "r").read())
plot_data = [p["err_x_y"] for p in plot_data]

# start_from = -1000
start_from = 0

berrs = [p[0] for p in plot_data][start_from:]
xs = [p[1] for p in plot_data][start_from:]
ys = [p[2] for p in plot_data][start_from:]

# plt.plot(range(len(berrs)), berrs, c="orange")
plt.plot(range(len(xs)), xs, c="red")
# plt.plot(range(len(ys)), ys, c="blue")

# same = 0
# for i, y in enumerate(ys):
#     if i == 0:
#         continue
#     ly = ys[i-1]
#     if ly == y:
#         same += 1
#     else:
#         print(ly, same+1)
#         same = 0
# print(y, same)

plt.show()
