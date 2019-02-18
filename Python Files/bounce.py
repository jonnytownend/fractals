from Tkinter import *
import ttk
import time

root = Tk()

wd = 500
ht = 500

canvas = Canvas(root, width=wd, height=ht)
canvas.pack()

def draw_ball(x, y):
	canvas.delete("ball")
	canvas.create_oval(x-20,y-20,x+20,y+20, tags="ball")

def drop_ball(x, y, length=100, strength=0.005):
	for t in range(length):
		draw_ball(x, y)
		y += strength * t*t
		root.update()
		time.sleep(0.01)
		
def bounce_ball(x, y, z, length=100, strength=0.005):
	canvas.create_line(x - 50, z, x + 50, z)
	dir = 1
	for t in range(length):
		if y > z:
			dir *= -1
			y = z
		else:
			draw_ball(x, y)
			y += (strength * t*t) * dir
			root.update()
			time.sleep(0.01)
			t += 1
	
		
bounce_ball(50,50,500)

root.mainloop()