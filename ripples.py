from Tkinter import *
import ttk

root = Tk()

wd = 600
ht = 600

canvas = Canvas(root, width=wd, height=ht)
canvas.pack()

N = 50
x_pxl = wd/N
y_pxl = ht/N

grid = []
for i in range(N):
	grid.append(N*[0])

def draw():
	canvas.delete("all")
	for y in range(N):
		for x in range(N):
			if grid[y][x] == -1:
				val = "100"
			else:
				val = str(100 - grid[y][x])
			canvas.create_rectangle(x_pxl*x, y_pxl*y, x_pxl*(x+1), y_pxl*(y+1), fill="gray%s" %val, outline="grey%s" %val)
	root.update()

def average():
	global grid
	dum = []
			
	for y in range(N):
		row = []
		for x in range(N):
			row.append(grid[y][x])
		dum.append(row)
		
	for y in range(1, N-1):
		for x in range(1, N-1):
			a = dum[y+1][x]
			b = dum[y-1][x]
			c = dum[y][x+1]
			d = dum[y][x-1]
			e = dum[y+1][x+1]
			f = dum[y+1][x-1]
			g = dum[y-1][x+1]
			h = dum[y-1][x-1]
			
			if dum[y][x] == -1:
				dum[y][x] == -1
			else:
				av = (a+b+c+d+e+f+g+h)/8
				dum[y][x] = av
				
	for y in range(N):
		for x in range(N):
			if dum[y][x] > 0 and dum[y][x] < 30:
				dum[y][x] += 5
			elif dum[y][x] > 30 and dum[y][x] < 90:
				dum[y][x] += 10
	
	for y in range(N):
		for x in range(N):
			grid[y][x] = dum[y][x]
			
grid[25][25] = 100

for i in range(100):
	draw()
	average()

			
			
root.mainloop()