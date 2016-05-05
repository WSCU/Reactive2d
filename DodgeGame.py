
from Reactive2D  import *
from pythonfrp import *
from pythonfrp.Numerics import *
from pythonfrp.Color import *
import random


count = var(0)
paddle = square(position = p2(getX(mouse),450), width = 50, height = 20, color = black)
def nullPrint(x, y):
    print("boopity")
    return None
def hitEnemy(en, me):
    count.add(1)
    print "Ouch!"
    print str(now(count))
    positionScrambler(en, me)
    return None
def positionScrambler(en, me):
    #exit(en)
    thing = square(position = p2(random.randint(0, 500), localTime * 100))
    hit(thing, paddle, hitEnemy)

enemy = square()
positionScrambler(enemy, paddle)
hit(enemy, paddle, hitEnemy)

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