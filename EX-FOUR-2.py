Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Exercise 4 'FLOWER DRAWING'
>>> import turtle
>>> def petal(t,r,angle):
	for i in range (2):
		t.circle(r,angle)
		t.left(180-angle)

		
>>> def flower(t,n,r,angle):
	for i in range(n):
		petal(t,r,angle)
		t.left(360.0/n)

		
>>> def move (t,length):
	window = turtle.Screen()
	t.pu()
	t.fd(length)
	t.pd()

	
>>> task = turtle.Turtle()
>>> task.speed(8)
>>> task.color('red')
>>> task.shape('turtle')
>>> move(task, -150)
>>> task.begin_fill()
>>> flower(task,7,60.0,60.0)
>>> task.end_fill()
>>> 
>>> task.color('black')
>>> move(task,150)
>>> flower(task,14,70.0,50.0)
