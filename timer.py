def create(obj):
  if obj==1:
    priserka1(100,100)
  elif obj==2:
    priserka2(200,200)
    
t = Timer(30 , create) #timer ktory vykonava funkciu create kazdých 30 sekund
t.start() #spustenie timera
t.cancel() #ukonceine timera
