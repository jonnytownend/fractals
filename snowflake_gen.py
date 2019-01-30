from Tkinter import *
import ttk
from random import randint
from math import pi, sin, cos, sqrt
import time

root = Tk()

wt = 500
ht = 500

canvas = Canvas(root, height=ht, width=wt)
canvas.pack()

def make_branch(scale):
	length = randint(2,10)
	length *= scale
	points = []
	for i in range(randint(3,4)):
		points.append([0, randint(1,length)])
		
	branch = [length, points]
	print length, points
	return branch
	
def draw_branch(branch, a, b, scale = 0.3, theta=pi/4, steps=4):
	length = branch[0]
	points = branch[1]
	
	canvas.create_line(a, b, a, b+length)
	
	for step in range(1, steps):
		angle = step*theta
		length *= scale
		
		for i in range(len(points)):
			a2 = a + points[i][0]
			b2 = b + points[i][1]
			
			c2 = a2 + length*sin(angle)
			d2 = b2 + length*cos(angle)
			
			canvas.create_line(a2, b2, c2, d2)
			
			l = sqrt(points[i][0]**2 + points[i][1]**2)
			
		root.update()
		time.sleep(1)
	
branch = make_branch(60)
draw_branch(branch, 200, 200)

root.mainloop()