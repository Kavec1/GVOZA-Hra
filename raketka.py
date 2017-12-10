import tkinter
c=tkinter.Canvas()
c.pack()

##raketka
c.create_rectangle(x,y-20,x+10,y-10,fill='white', outline='white')
c.create_rectangle(x-20,y-10,x+30,y+10,fill='white', outline='white')
c.create_rectangle(x-30,y+10,x+40,y+20,fill='white', outline='white')
