from init import *
def priserka1(x,y):
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
  
def priserka2(x,y):
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
  
def raketka(x,y):
  c.create_rectangle(x,y-20,x+10,y-10,fill='white', outline='white', tags='raketa')
  c.create_rectangle(x-20,y-10,x+30,y+10,fill='white', outline='white', tags='raketa')
  c.create_rectangle(x-30,y+10,x+40,y+20,fill='white', outline='white', tags='raketa')
  
'''c.create_oval(10,10,50,50, tags = 'ujco')
c.create_oval(20,20,25,25, tags = 'ujco')
c.create_oval(35,20,40,25, tags = 'ujco')
c.create_line(20,40,40,40, tags = 'ujco')'''
