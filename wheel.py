from math import sin, cos
from matplotlib import pyplot as plt

R = 10
r = 20
N = 500

x_vals = []
y_vals = []

for i in range(N):
	#r -= 0.02
	theta = float(i)/float(R)
	y = r*cos(theta)
	x = r*sin(theta) + i
	
	x_vals.append(x)
	y_vals.append(y)

plt.plot(x_vals, y_vals)
plt.show()