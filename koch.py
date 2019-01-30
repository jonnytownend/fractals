from Tkinter import *
import ttk
from math import sqrt, sin, cos
from random import randint
import time

root = Tk()

wd = 500
ht = 500

line_coords = []

canvas = Canvas(root, width=wd, height=ht)
canvas.pack()

def draw_triangle(ax, ay, bx, by):
	
	l = sqrt((bx - ax)**2 + (by - ay)**2)
	h = (l/2)*sqrt(3)
	
	x = ax + (bx - ax)/2 - (sqrt(3)/2)*(by - ay)
	y = ay + (by - ay)/2 + (sqrt(3)/2)*(bx - ax)
	
	
	canvas.create_line(ax, ay, bx, by)
	canvas.create_line(x, y, ax, ay)
	canvas.create_line(bx, by, x, y)

def draw_next(ax, ay, bx, by):
	ax2 = ax + (bx-ax)/3
	ay2 = ay + (by-ay)/3
	
	bx2 = bx - (bx-ax)/3
	by2 = by - (by-ay)/3
	
	draw_triangle(bx2, by2, ax2, ay2)
	line_coords.append([bx2, by2, ax2, ay2])
	
def draw_set(ax, ay, bx, by):
	draw_triangle(ax, ay, bx, by)
	
	l = sqrt((bx - ax)**2 + (by - ay)**2)
	h = (l/2)*sqrt(3)
	
	x = ax + (bx - ax)/2 - (sqrt(3)/2)*(by - ay)
	y = ay + (by - ay)/2 + (sqrt(3)/2)*(bx - ax)
	
	
	draw_next(ax, ay, bx, by)
	draw_next(x, y, ax, ay)
	draw_next(bx, by, x, y)

def koch(it, ax, ay, bx, by, delay=0.5):
	draw_triangle(ax, ay, bx, by)
	root.update()
	time.sleep(delay)
	
	draw_set(ax,ay,bx,by)
	root.update()
	time.sleep(delay)
	
	for j in range(it):
		length = len(line_coords)
		for i in range(length):
			draw_set(line_coords[i][0], line_coords[i][1], line_coords[i][2], line_coords[i][3])
		root.update()
		time.sleep(delay)

koch(3, 100, 100, 300, 300, delay=0.5)

root.mainloop()