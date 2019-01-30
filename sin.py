from Tkinter import *
from math import sin, cos,pi

root = Tk()

canvas = Canvas(root, height=500, width=500)
canvas.pack()

x = 100
y = 100
dir = 1
for i in range(1,100000):
	k = 1*i
	if i%50 == 0:
		dir *= -1
	for j in range(2):
		x2 = x + 10*sin(k)
		y2 = y + 10*sin(k+pi/2)
		canvas.create_line(x,y,x2,y2)
		root.update()
		#canvas.delete("all")
		x = x2 + dir*10*pi/2	
		y = y2

root.mainloop()