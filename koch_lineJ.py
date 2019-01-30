from Tkinter import *
from math import sqrt, sin, cos
import time
from random import randint

root = Tk()

wt = 800
ht = 800

canvas = Canvas(root, height=ht, width=wt)
canvas.pack()

def step(points, height=0):
	to_insert = []
	
	for i in range(len(points)-1):
		mid_points = []
		
		a = points[i][0]
		b = points[i][1]
		c = points[i+1][0]
		d = points[i+1][1]
		
		l = sqrt((c - a)**2 + (d - b)**2)
		if height == 0:
			h = (l/(2*3))*sqrt(3)
		else:
			h = height*(l/(2*3))*sqrt(3)
		
		midA_x = a + (c-a)/3
		midA_y = b + (d-b)/3
		
		midB_x = a + 2*(c-a)/3
		midB_y = b + 2*(d-b)/3
		
		peak_x = a + (c-a)/1 - h*(d-b)/l
		peak_y = b + (d-b)/1 + h*(c-a)/l
		
		mid_points.append([midA_x, midA_y])
		mid_points.append([peak_x, peak_y])
		mid_points.append([midB_x, midB_y])
		
		to_insert.append(mid_points)
	
	new_points = []
	for i in range(len(points)-1):
		new_points.append(points[i])
		for point in to_insert[i]:
			new_points.append(point)
	new_points.append(points[-1])
	
	points = []
	for i in new_points:
		points.append(i)
		
	return points

def draw(points, fill=0):
	for i in range(len(points)-1):
		if fill == 1:
			canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill="red")
		else:
			canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
		
def iterate(points, steps=4, watch=0, height=0):
	for i in range(steps):
		if watch==1:
			canvas.delete("all")
			draw(points)
			root.update()
			time.sleep(1)
		points = step(points, height)
		
	return points

def draw_koch_tri(a, b, c, d, it=4, watch=0, height=0, side=0):
	l = sqrt((d - b)**2 + (c - a)**2)
	h = (l/2)*sqrt(3)
	
	x = a + (c - a)/2 - (sqrt(3)/2)*(d - b)
	y = b + (d - b)/2 + (sqrt(3)/2)*(c - a)
	
	points = [[a,b], [x,y], [c,d], [a,b]]
	if side == 1:
		points = points[::-1]
	draw(iterate(points, it, watch, height))

points = [[100,100], [500,100], [500,200], [400,200], [400,400], [300, 500], [200,500], [100, 400], [100,300], [200,300], [200,400], [300,400], [300, 200], [100, 200], [100, 100]]

'''
k = 0.2
dir = 1
for i in range(1000):
	k += 0.1*dir
	if k > 1 or k < -0.5:
		dir *= -1
	draw(iterate(points[::-1], height=k))
	root.update()
'''


draw(iterate(points[::-1], height=0.2, watch=1, steps=5))


root.mainloop()