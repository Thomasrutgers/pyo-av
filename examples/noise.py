from pyo import *
s = Server(buffersize=1024).boot()
s.start()
from av import *
o=OscDataSend("f",12000,'/start')
o.send([0])
from random import *

class A: pass
aa = [A() for i in range(1,40)]

for n,a in enumerate(aa):
    a.freq=(n+4)*100
    a.noise = Noise(0.3)
    a.filter = ButBP(a.noise,a.freq,40)
    a.env=Abs(Sine((n+20)/10,mul=0.4))
    a.sound=a.filter*a.env
    a.av=Av(a.sound,x=n*40,y=100,w=30,h=700)
    a.av.lum=a.env*255*2
y=Sine(0.05,mul=100,add=50)
for a in aa:
    a.av.w=a.env*80
    a.av.hue=y
for a in aa: a.av.stop()
for a in aa: a.av.start()
