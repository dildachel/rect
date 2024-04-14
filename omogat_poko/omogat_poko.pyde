x=0
y=0
t=600
r=600
h=400
g=400

def setup():
    size(1000,1000)
    frameRate(60)
def draw():
    global x,y,t,r,h,g
    background(0)
    rectMode(CENTER)
    fill(172,250,230)
    rect (x,y,250,250)
    x=x+1
    y=y+1
    if x>998:
        x=0
    if y>998:
         y=0
    fill(229,245,116)
    rect (t,r,250,250)
    t=t+1
    r=r+1
    if t>998:
        t=0
    if r>998:
         r=0
    fill(240,154,250)
    rect (h,g,250,250)
    h=h+1
    g=g+1
    if h>998:
        h=0
    if g>998:
         g=0
    fill(250,66,72)
    rect (x,y,250,250)
