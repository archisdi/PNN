from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
file = open("data/train.txt","r")

mark = {
    '0': ['r', 'o'],
    '1': ['b', '^'],
    '2': ['g', '.'],
}

points = []
for line in file:
    points.append(line.rstrip().split('\t'))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for x, y ,z ,cluster in points:
    ax.scatter(float(x), float(y), float(z), c=mark[cluster][0], marker=mark[cluster][1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
