from Tkinter import *
from math import sqrt, sin, cos, pi
import time
from random import randint

root = Tk()

wt = 800
ht = 800

canvas = Canvas(root, height=ht, width=wt)
canvas.pack()

def step(points, height=1):
	to_insert = []
	
	for i in range(len(points)-1):
		mid_points = []
		
		a = points[i][0]
		b = points[i][1]
		c = points[i+1][0]
		d = points[i+1][1]
		
		h = height
		
		L = sqrt((c - a)**2 + (d - b)**2)
		
		l = (h*sqrt(2)/(2+3*h*sqrt(2)))*L
		
		A_x = a + ((c-a)*l/L)
		A_y = b + ((d-b)*l/L)
		
		D_x = c - ((c-a)*l/L)
		D_y = d - ((d-b)*l/L)
		
		B_x = A_x + (l/(L*h*sqrt(2)))*(c-a-d+b)
		B_y = A_y + (l/(L*h*sqrt(2)))*(c-a+d-b)
		
		C_x = B_x + ((c-a)*l/L)
		C_y = B_y + ((d-b)*l/L)
		
		mid_points.append([A_x, A_y])
		mid_points.append([B_x, B_y])
		mid_points.append([C_x, C_y])
		mid_points.append([D_x, D_y])
		
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

def draw(points, fill=0, colour=0):
	for i in range(len(points)-1):
		if fill == 1:
			canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill="red")
		elif colour != 0:
			canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill=colour)
		elif colour == 0:
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

def draw_koch_tri(a, b, c, d, it=4, watch=0, height=0, side=0, colour=0):
	l = sqrt((d - b)**2 + (c - a)**2)
	h = (l/2)*sqrt(3)
	
	x = a + (c - a)/2 - (sqrt(3)/2)*(d - b)
	y = b + (d - b)/2 + (sqrt(3)/2)*(c - a)
	
	points = [[a,b], [x,y], [c,d], [a,b]]
	if side == 1:
		points = points[::-1]
	draw(iterate(points, it, watch, height), fill=0, colour=colour)
	
def shape(x, y, sides, length):
	theta = 2*pi/sides
	
	points = []
	for i in range(sides+1):
		x += length*cos(theta)
		y += length*sin(theta)
		points.append([x,y])
		theta += 2*pi/sides
		
	return points


k = 5
dir = -1
for i in range(100000):
	if k <= 1 or k >= 20:
		dir *= -1
		
	draw(iterate(shape(400,200,5,300)[::-1],height=k, steps=2, watch=0))
	draw(iterate(shape(400,200,6,300),height=k, steps=2, watch=0))
	root.update()
	canvas.delete("all")
	
	k += dir*0.5

root.mainloop()