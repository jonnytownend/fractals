from Tkinter import *
from random import randint
import time
import ttk

root = Tk()

wd=1000
ht=600

title = Label(root, text="DRAGONS")
title.pack()

canvas = Canvas(root, height=ht, width=wd)
canvas.pack()

x = wd/2
y = ht/2
step = 3
amount = 1
i = 0

data = "run: %s, steps: %s, step size: %s" %(i, amount, step)
colours = ["black"]

label = Label(text = data)
label.pack()

colour = colours[randint(0,len(colours)-1)]

for i in range(10000):
	for j in range(amount):
		w = randint(-step,step)
		z = randint(-step,step)
		
		w += x
		z += y

		canvas.create_line(x,y,w,z, fill=colour)
		
		x = w
		y = z
	
	#time.sleep(0.2)
	root.update()
	
	data = "run: %s, steps: %s, step size: %s" %(i, amount, step)
	colour = colours[randint(0,len(colours)-1)]
	label.destroy()
	label = Label(text = data)
	label.pack()
	
	canvas.delete("all")
	amount += 2
	if i%200 == 0:
		step += 1
	x = wd/2
	y = ht/2


root.mainloop()