from pyo import *
class Av:
    idCounter=0;
    def __init__(self,audio=Sine(440),shape=0,x=0,y=0,w=100,h=100,hue=255,sat=255,lum=255,alpha=255,rot=0,group=0):
        self.nr = Av.idCounter
        Av.idCounter += 1
        self.attr=dict()
        self.osc=dict()
        self.playing = False
        self.oscDataSender  = OscDataSend("f",12000,'/init')

        #properties
        self.audio=audio
        self.shape=shape
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.hue=hue
        self.sat=sat
        self.lum=lum
        self.alpha=alpha
        self.rot=rot
        self.group=group

        self.start()

    def set(self,key,val):
        address = '/obj/'+str(self.nr)+'/'+key
        self.attr[key]=val
        if isinstance(val,(int,float)):#might also use: is not PyoObject
            #stop running osc signals
            if key in self.osc:
                self.osc[key].stop()
            #send single osc message
            self.oscDataSender.addAddress("f",12000,address)#handles duplicates sp we dpont't have to worry about that
            self.oscDataSender.send([val],address)
        else:#PyoObject
            if key == 'audio':#use INputFade instead? seperate funciton?
                self.attr['audio'].stop()
                if self.playing:
                    self.attr['audio'].out()
            else:
                if not key in self.osc:
                    self.osc[key] = OscSend(val,12000,address).stop()
                    if self.playing:
                        self.osc[key].play()
                else:
                    self.osc[key].setInput(val)
    def stop(self):
        self.playing=False
        for k,v in self.osc.items():
            v.stop()
        self.attr['audio'].stop()
    def start(self):
        self.playing =True
        for k,v in self.osc.items():
            v.play()
        self.attr['audio'].out()
    def setBufferRate(self,x):
        for k, v in self.osc.items():
            v.setBufferRate(x)

    @property
    def audio(self):
        return self.attr['audio']
    @audio.setter
    def audio(self,val):
        self.set('audio',val)

    @property
    def shape(self):
        return self.attr['shape']
    @shape.setter
    def shape(self,val):
        self.set('shape',val)

    @property
    def x(self):
        return self.attr['x']
    @x.setter
    def x(self,val):
        self.set('x',val)

    @property
    def y(self):
        return self.attr['y']
    @y.setter
    def y(self,val):
        self.set('y',val)

    @property
    def w(self):
        return self.attr['w']
    @w.setter
    def w(self,val):
        self.set('w',val)

    @property
    def h(self):
        return self.attr['h']
    @h.setter
    def h(self,val):
        self.set('h',val)

    @property
    def hue(self):
        return self.attr['hue']
    @hue.setter
    def hue(self,val):
        self.set('hue',val)

    @property
    def sat(self):
        return self.attr['sat']
    @sat.setter
    def sat(self,val):
        self.set('sat',val)

    @property
    def lum(self):
        return self.attr['lum']
    @lum.setter
    def lum(self,val):
        self.set('lum',val)

    @property
    def alpha(self):
        return self.attr['alpha']
    @alpha.setter
    def alpha(self,val):
        self.set('alpha',val)

    @property
    def rot(self):
        return self.attr['rot']
    @rot.setter
    def rot(self,val):
        self.set('rot',val)

    @property
    def group(self):
        return self.attr['group']
    @group.setter
    def group(self,val):
        self.set('group',val)
