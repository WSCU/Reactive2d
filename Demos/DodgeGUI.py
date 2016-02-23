#-----  imports  -----#
from java.awt import Color
from java.awt.event import ActionListener
from java.awt.event import KeyAdapter
from java.awt.event import MouseAdapter
from java.awt.event import MouseMotionAdapter
from java.lang import System
from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import Timer

from pythonfrp.Engine import *
from Reactive2D import *

import random

#-----  declarations  ------#

# ExternalEvents is the event dictionary used by the engine.
externalEvents = {}

# This is Jython code to interface with mouse events
class MA(MouseAdapter):
    def __init__(self, clicker):
        self.clicker = clicker
    
    def mouseClicked(self, event):
        self.clicker(event.getX(), event.getY())
 
class MLA(MouseMotionAdapter):
    def __init__(self, mover):
        self.mover = mover
         
    def mouseMoved(self, e):
        self.mover(e.getX(), e.getY())
        
# Key Events
class KA(KeyAdapter):
    def __init__(self, clicker):
        self.clicker = clicker
    #keyPressed it needed for arrowKeys
    def keyPressed(self, event):
        self.clicker(event.getKeyText(event.getKeyCode()))
        
class Canvas(JPanel):
    def __init__(self, drawer, click, move):
        super(Canvas, self).__init__()
        self.drawer = drawer
        self.click = click
        self.move = move
#        self.key = key
        self.addMouseListener(MA(lambda x, y: self.click(x, y)))
        self.addMouseMotionListener(MLA(lambda x, y: self.move(x, y)))

    def paint(self, g):
        JPanel.paint(self, g)
        self.drawer(g)
        
class Example(JFrame, ActionListener):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
# Paint all of the objects in screenObjects
    def mypaint(self, g):
        for object in screenObjects:
            object._draw(g) #Now calls a _draw method on each object, instead of just having a bunch of lambdas in screenObjects.
            
# Add an external event on a mouse click
    def myclick(self, x, y):
        externalEvents['LeftMouseButton'] = SP2(x, y)   #SP2 inherited from pythonfrp StaticNumerics.py 
    
    def mykey(self, k):
        externalEvents['KeyTyped']=string(k)
#        print("Key Pressed: " + string(k))

    def my_move(self, x, y):
        mouse_pos[0]= SP2(x,y)

    def initUI(self):
        self.addKeyListener(KA(lambda k: self.mykey(k)))
        self.xp=0
        self.yp=0
        self.canvas=Canvas(lambda g:self.mypaint(g), lambda x, y: self.myclick(x, y), lambda x, y: self.my_move(x, y))
        self.canvas.setBackground(Color(200, 200, 200))
        self.getContentPane().add(self.canvas)
        self.setTitle("Test")
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setSize(500, 500)
        self.setLocationRelativeTo(None)
        self.setBackground(Color(255, 255, 255))
        self.setVisible(True)
        self.timer=Timer(50, self)
        self.timer.start()

# This is the heartbeat handling code - this is attached to a timer in the frame      

    def actionPerformed(self, e):
        currentTime=System.currentTimeMillis()
        rSide = random.randrange(0,4)
        if ((currentTime-startTime[0]) % 5 == 0):
            if (rSide == 0):
                (circle(p2(random.randrange(50,450),-30+localTime*100), 10))
            elif (rSide == 1):
                (circle(p2(500-localTime*100, random.randrange(50,450)), 10))
            elif (rSide == 2):
                (circle(p2(random.randrange(50,450),500-localTime*100), 10))
            else:
                (circle(p2(-30+localTime*100,random.randrange(50,450)), 10))
        del screenObjects[:]
#        print(currentTime-startTime[0])
#        print('Objects: ' + str(Globals.worldObjects))
        heartbeat((currentTime - startTime[0]) / 1000.0, externalEvents)
        externalEvents.clear()
        self.repaint()
        
def startGame():
    print("Starting...")
    startTime[0]=System.currentTimeMillis() 
    initialize(0) 
    Example() 