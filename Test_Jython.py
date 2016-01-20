# Java functionality 
from java.awt import Color
from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import Timer
from java.awt.event import ActionListener
from java.awt.event import MouseAdapter
from java.lang import System

# Use from for user-level stuff and import for engine level stuff
from pythonfrp.Engine import *
from pythonfrp.StaticNumerics import *
import pythonfrp.Proxy as Proxy
from pythonfrp.Functions import *
from pythonfrp.Numerics import *
import pythonfrp.Globals as Globals
from pythonfrp.Factory import eventObserver

# Globals that define the state of the world.  Screen objects are all of the drawable objects and externalEvents is the event
# dictionary used by the engine.
screenObjects = []
externalEvents = {}
# This is the time at which the engine starts.  The [] is to make it mutable.
startTime = [0]


# This is Jython code to interface with mouse events
class MA(MouseAdapter):
    def __init__(self, clicker):
        self.clicker = clicker
    def mouseClicked(self, event):
        self.clicker(event.getX(), event.getY())

# This is Jython code to interface with a graphics panel
class Canvas(JPanel):
    def __init__(self, drawer, click):
        super(Canvas, self).__init__()
        self.drawer = drawer
        self.click = click
        self.addMouseListener(MA(lambda x, y: self.click(x,y)))

    def paint(self, g):
        JPanel.paint(self, g)
        self.drawer(g)

# This creates the drawing frame (Example is a stupid name ...)
class Example(JFrame, ActionListener):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

# Paint all of the objects in screenObjects
    def mypaint(self, g):
        for object in screenObjects:
            object(g)
            
# Add an external event on a mouse click
    def myclick(self, x, y):
        externalEvents['LeftMouseButton'] = SP2(x,y)

    def initUI(self):
        self.xp = 0
        self.yp = 0
        self.canvas = Canvas(lambda g:self.mypaint(g), lambda x,y: self.myclick(x,y))
        self.canvas.setBackground(Color(200,200,100))
        self.getContentPane().add(self.canvas)
        self.setTitle("Ball")
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setSize(300, 300)
        self.setLocationRelativeTo(None)
        self.setBackground(Color(255,255,255))
        self.setVisible(True)
        
        self.timer = Timer(50, self)
        self.timer.start()

 # This is the heartbeat handling code - this is attached to a timer in the frame      
    def actionPerformed(self, e):
        currentTime = System.currentTimeMillis()
        del screenObjects[:]
#        print(currentTime-startTime[0])
#        print('Objects: ' + str(Globals.worldObjects))
        heartbeat((currentTime - startTime[0])/1000.0, externalEvents)
        externalEvents.clear()
        self.repaint()


# This is the code that creates an arbitrary screen object (a reactive object visible on the screen).  Right now
# used to draw a circle.
        
class ScreenObject(Proxy.Proxy):
        def __init__ (self, position):
            Proxy.Proxy.__init__(self, name = 'Circle', updater = circleUpdate,
                             types = {"position": p2Type})
            self.position = position
#            print('created circle')

# This is the updater that is called by the 
def circleUpdate(self):
    positionNow = self._get("position")
#    print('Positiong Now:' + str(positionNow))
# This is what makes the circle visible.  The draw code (a function that takes a graphics object) is placed
# in the screenObjects list
    screenObjects.append(lambda g: drawCircle(g, positionNow))

# The draw code for a circle
def drawCircle(g, p):
    g.setColor(Color(255,0,0))
    g.fillOval(int(p.x), int(p.y), 20, 20)

# This is the start function that initializes the reactive engine and then starts the animation
def start():
    print("Starting...")
    startTime[0] = System.currentTimeMillis()
    initialize(0)
    Example()
    
# A user-level function to create a reactive circle.  x is the position of the circle
def circle(x):
    return ScreenObject(x)

# This is an event observer for the left mouse button
def lbp():
    return eventObserver('LeftMouseButton')

# From here on this is user code - create a moving circle on each mouse click that starts from the position of the click

def makeCircle(m,v):
    circle(p2(localTime*50+v.x,localTime*50+v.y))

# React to each mouse press by creating a new circle
react(lbp(),makeCircle)

# Start!
start()