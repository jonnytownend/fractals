from Tkinter import *
import ttk
from math import sqrt, sin, cos
from random import randint
import time

root = Tk()

wd = 800
ht = 800

canvas = Canvas(root, width=wd, height=ht)
canvas.pack()

def draw_triangle(ax, ay, bx, by, runs):	
	coords = []
	l = sqrt((bx - ax)**2 + (by - ay)**2)
	h = (l/2)*sqrt(3)
	
	x = ax + (bx - ax)/2 - (sqrt(3)/2)*(by - ay)
	y = ay + (by - ay)/2 + (sqrt(3)/2)*(bx - ax)
	
	c1 = [ax + (bx-ax)/3, ay + (by-ay)/3]
	c2 = [ax + 2*(bx-ax)/3, ay + 2*(by-ay)/3]
	c3 = [x + 2*(bx-x)/3, y + 2*(by-y)/3]
	c4 = [x + (bx-x)/3, y + (by-y)/3]
	c5 = [ax + 2*(x - ax)/3, ay + 2*(y-ay)/3]
	c6 = [ax + (x-ax)/3, ay + (y-ay)/3]
	
	coords.append(c1)
	coords.append(c2)
	coords.append(c3)
	coords.append(c4)
	coords.append(c5)
	coords.append(c6)
	
	canvas.create_line(ax, ay, bx, by)
	canvas.create_line(x, y, ax, ay)
	canvas.create_line(bx, by, x, y)
	
	#root.update()
	
	runs.append(coords)
			
def koch(ax, ay, bx, by, steps=1, invert=0):
	runs = []
	
	draw_triangle(ax, ay, bx, by, runs)
	
	for step in range(steps):
		length = len(runs)
		for i in range(length):
			for j in range(6):
				if invert == 0 or invert == 1:
					draw_triangle(runs[i][j][0], runs[i][j][1], runs[i][j-1][0], runs[i][j-1][1], runs)
				if invert == 1 or invert == 2:
					draw_triangle(runs[i][j-1][0], runs[i][j-1][1], runs[i][j][0], runs[i][j][1], runs)
				
		root.update()
	
koch(100,100,500,100,4,1)
#koch(100 + 400/3,100 + 400/3,100 + 2*400/4,100 + 400/3,5,0)

#koch(0.1*wd,ht/4,0.9*wd,ht/4,5)

root.mainloop()