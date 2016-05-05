
from Reactive2D  import *
from pythonfrp import *
from pythonfrp.Numerics import *
from pythonfrp.Color import *
 
def nullPrint(x, y):
    print("boopity")
    return None

paddle = square(position = p2(getX(mouse),450), width = 50, height = 20, color = black)
paddle2 = square(position = p2(100,400))
pauly = polygon(position = p2(50,50), width = 50, height = 50)
pauly2 = polygon(position = p2(100,100), width = 50, height = 50, polyPoints = [p2(-3,-3), p2(50, 0), p2(0, 30)])


#hit(c1, s1, exitScene)

def keyPressed(self, k):
    if (k == "Left"):
        #print "Going left!"
        pos = now(paddle2.position)
        if (getX(pos) > 20):
            paddle2.position = p2(getX(pos) - 5, 400)
    if (k == "Right"):
        pos = now(paddle2.position)
        if (getX(pos) < 480):
            paddle2.position = p2(getX(pos) + 5, 400)
 
 #react(kT,typeKey)
 
react(kT(), keyPressed)

start()