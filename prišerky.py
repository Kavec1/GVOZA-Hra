import tkinter
c=tkinter.Canvas()
c.pack()

x=100
y=100

##priserka1
c.create_rectangle(x-10,y-20,x+10,y-15, fill='blue', outline='blue')
c.create_rectangle(x-20,y-15,x+20,y-10, fill='blue', outline='blue')
c.create_rectangle(x-25,y-10,x+25,y+5, fill='blue', outline='blue')
c.create_rectangle(x-20,y-5,x-10,y,fill='black', outline='blue')
c.create_rectangle(x+10,y-5,x+20,y, fill='black', outline='blue')
c.create_rectangle(x-15,y+5,x-10,y+10, fill='blue', outline='blue')
c.create_rectangle(x+10,y+5,x+15,y+10, fill='blue', outline='blue')
c.create_rectangle(x-20,y+10,x-15,y+15, fill='blue', outline='blue')
c.create_rectangle(x-10,y+10,x+10,y+15, fill='blue', outline='blue')
c.create_rectangle(x+15,y+10,x+20,y+15, fill='blue', outline='blue')
c.create_rectangle(x-25,y+15,x-20,y+20, fill='blue', outline='blue')
c.create_rectangle(x+20,y+15,x+25,y+20, fill='blue', outline='blue')

x=200
y=100

##priserka2
c.create_rectangle(x-5,y-20,x+5,y-15, fill='green', outline='green')
c.create_rectangle(x-10,y-15,x+10,y-10, fill='green', outline='green')
c.create_rectangle(x-15,y-10,x+15,y-5, fill='green', outline='green')
c.create_rectangle(x-20,y-5,x+20,y+5, fill='green', outline='green')
c.create_rectangle(x-10,y-5,x-5,y, fill='black', outline='green')
c.create_rectangle(x+5,y-5,x+10,y, fill='black', outline='green')
c.create_rectangle(x-10,y+5,x-5,y+10, fill='green', outline='green')
c.create_rectangle(x+5,y+5,x+10,y+10, fill='green', outline='green')
c.create_rectangle(x-15,y+10,x-10,y+15, fill='green', outline='green')
c.create_rectangle(x-5,y+10,x+5,y+15, fill='green', outline='green')
c.create_rectangle(x+10,y+10,x+15,y+15, fill='green', outline='green')
c.create_rectangle(x-20,y+15,x-15,y+20, fill='green', outline='green')
c.create_rectangle(x-10,y+15,x-5,y+20, fill='green', outline='green')
c.create_rectangle(x+5,y+15,x+10,y+20, fill='green', outline='green')
c.create_rectangle(x+15,y+15,x+20,y+20, fill='green', outline='green')







