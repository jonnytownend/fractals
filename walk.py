from Tkinter import *
import ttk
from random import randint

root = Tk()

ht = 600
wd = 600
step = 3
canvas = Canvas(root, height=ht, width=wd)
canvas.pack()

x = wd/2
y = ht/2

for i in range(10000):
	w = randint(-1,1)
	z = randint(-1,1)
	
	w = w*step + x
	z = z*step + y
	
	canvas.create_line(x,y,w,z)
	root.update()
	
	x = w
	y = z
	
root.mainloop()