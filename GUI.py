# Java functionality 

#-----  imports  -----#
#from java.awt import Color
import java.awt.Color as JavaColor
from java.awt.event import ActionListener
from java.awt.event import KeyAdapter
from java.awt.event import MouseAdapter
from java.awt.event import MouseMotionAdapter
from java.lang import System
from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import JButton
from javax.swing import Timer
from javax.swing import JSlider
from pythonfrp.Numerics import *
from java.awt import Dimension
from java.awt import GradientPaint
from java.awt import Graphics
from java.awt import Graphics2D
from java.awt.event import WindowAdapter
from java.awt.event import WindowEvent
from java.awt.geom import Ellipse2D
from java.awt.geom import Rectangle2D
from javax.swing import JApplet
from javax.swing import JFrame
from java.awt import BorderLayout

from pythonfrp.Engine import *
from Reactive2D import *
from pythonfrp.Color import *

import random

#-----  declarations  ------#

# ExternalEvents is the event dictionary used by the engine.
externalEvents = {}
balls = []
# LocalTime and World Objects are in Globals




#----------------------------------------------------------------------------------------------------------------------------------------------#    



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
      
         
        
class KA(KeyAdapter):
    def __init__(self, clicker):
        self.clicker = clicker
    def keyTyped(self, event):
#        print("Key Pressed: " + str(event.getKeyCode()) + "| Key Code: " + str(event.getKeyCode()))
        self.clicker(event.getKeyCode())
    def keyPressed(self, event):
        self.clicker(event.getKeyText(event.getKeyCode()))
        #Uncomment if you need to know what a key is being saved as
#        print(event.getKeyText(event.getKeyCode()))

# This is Jython code to interface with a graphics panel
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
        #blueToWhite = GradientPaint(10, 10, JavaColor(0,0,255), 100, 10, JavaColor(255,255,255));
        #g.setColor(JavaColor(255,255,255));
        #g.setPaint(blueToWhite);
        #g.drawOval(10, 10, 100, 100);
        #g.fill(Ellipse2D.Double(10, 10, 100, 100));
        #g.fill(Rectangle2D.Double(5, 150, 200, 30));

 
# This creates the drawing frame (Example is a stupid name ...)
 
class Example(JFrame, ActionListener):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

# Paint all of the objects in screenObjects
    def mypaint(self, g):
        layerArray = [[] for i in range (100)] #Creating a 100-item array for us to work with.
	for object in screenObjects:
            layerIndex = int(min(object._zLayer, 99)) #This specifies the layer that the object will be headed for...
            layerLoc = 0
            myDepth = object._get("zDepth")
            for compObject in layerArray[layerIndex]: #but first, we need to find the right place in that layer to put our object.
                if (myDepth > compObject._get("zDepth")):
                    layerLoc = layerLoc + 1
                else:
                    break
            layerArray[layerIndex].insert(layerLoc ,object)
        newArray = [] #We now want to compress our scattered 2d-array into a 1d-array.
	for subArray in layerArray: #It's called Radix sorting.
            newArray.extend(subArray)
	#screenObjects = newArray #Turns out you can't actually do this, and I have no idea why.
        for object in newArray: #Instead of going through screenObjects, we go through newArray, which is sorted by layer.
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
        self.canvas.setBackground(JavaColor(200, 200, 100))
        self.getContentPane().add(self.canvas)
        self.setTitle("Test")
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.xSize = 500
        self.ySize = 500
        self.setSize(self.xSize, self.ySize)
        self.setLocationRelativeTo(None)
        self.setBackground(JavaColor(255, 255, 255))
        self.setVisible(True)
        
        #self.button = JButton("This is a button")
        #self.add(self.button, BorderLayout.SOUTH)
        #self.button.addActionListener(self)
        
        self.timer=Timer(50, self)
        self.timer.start()

# This is the heartbeat handling code - this is attached to a timer in the frame      

    def actionPerformed(self, e):
        #if(e.getSource() == self.button):
            #self.addSlider()
        #else:
            currentTime=System.currentTimeMillis()
            #if ((currentTime-startTime[0]) % 75 == 0):
            #    balls.append(circle(p2(random.randrange(50,250),270-localTime*100), 10))
            del screenObjects[:]
    #        print(currentTime-startTime[0])
    #        print('Objects: ' + str(Globals.worldObjects))
            heartbeat((currentTime - startTime[0]) / 1000.0, externalEvents)
            externalEvents.clear()
            self.repaint() 
    def addSlider(self): #adds a new slider at the bottom of the window.
        slider = JSlider()
        self.add(slider, BorderLayout.SOUTH) #this is the best way I could find to make sure the slider appears somewhere consistent.
        self.ySize = self.ySize + 20 #the problem, sadly, is that all of the sliders and buttons and stuff appear at the SAME PLACE, overlapping.
        self.setSize(self.xSize, self.ySize)
        
 
mouse = ObserverF(lambda x: mouse_pos[0], type = p2Type)

 # This is the start function that initializes the reactive engine and then starts the animation
def start():
    print("Starting...")
    startTime[0]=System.currentTimeMillis() 
    initialize(0) 
    Example() 
#        print(currentTime-startTime[0])
#        print('Objects: ' + str(Globals.worldObjects))
 
 
