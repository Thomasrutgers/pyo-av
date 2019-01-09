
import oscP5.*;
import netP5.*;
int time;
OscP5 oscP5;
IntList active;
Box[] boxes = new Box[5000]; //seems to be the max!
boolean start =false;
void setup() {
  active = new IntList();
  size(650,650,P3D);
  oscP5 = new OscP5(this,12000);
  for (int i=0;i<5000;i++) {
    boxes[i]= new Box();
  }
  //noLoop();  
  //fill(200,150);
  frameRate(25);
    noStroke();
colorMode(HSB);
rectMode(CENTER);
}


void draw() {
  background(0);
  
  for (int i = 0;i<active.size();i++) {
    boxes[active.get(i)].draw();
  }

  if (start) {
    active.clear();
    start=false;;
  }
}


void oscEvent(OscMessage theOscMessage) {
  if (theOscMessage.addrPattern().equals("/start")) { //normaly all osc messages should arrive together every 1000/44 = 23 ms
    start=true;
  }
  else { //three-part-address
    
    String[] addr = theOscMessage.addrPattern().split("/");
    float val=theOscMessage.get(0).floatValue();
    setVal(int(addr[2]),addr[3],val);
    //println("got ",int(addr[2]),addr[3],val);
  }
}

void setVal(int id,String var,float val) {
   if (active.hasValue(id) == false) {     
     active.append(id);
   }
   boxes[id].set(var,val);
}

class Box {
  float shape,x,y,w,h,hue,sat,lum,alpha,rot; //shape as float for morphing
  int group;
  Box() {
    x=0;y=0;w=0;h=0;
   }
  void set(String var, float val) {
    if (var.equals("shape")) shape=val;
    if (var.equals("x")) x=val;
    if (var.equals("y")) y=val;
    if (var.equals("w")) w=val;
    if (var.equals("h")) h=val;
    if (var.equals("hue")) hue=val;
    if (var.equals("sat")) sat=val;
    if (var.equals("lum")) lum=val;
    if (var.equals("alpha")) alpha=val;
    if (var.equals("rot")) rot=val;
    if (var.equals("group")) group=int(val);
   }
  void draw() {
    fill(hue,sat,lum,alpha);     
    rect(x,y,w,h);
  }
}
