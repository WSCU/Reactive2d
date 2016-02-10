# Java functionality 

#-----  imports  -----#
from java.awt import Color
from java.awt.event import ActionListener
from java.awt.event import KeyAdapter
from java.awt.event import MouseAdapter
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
from java.awt.event import MouseMotionAdapter
=======
>>>>>>> 16b3d35c35e5e93a522da9ed93bcd79ef2685acf
>>>>>>> Stashed changes
from java.lang import System
from javax.swing import JFrame
from javax.swing import JPanel
from javax.swing import Timer
from pythonfrp.Engine import *
from reactive2D import *

#-----  declarations  ------#

# ExternalEvents is the event dictionary used by the engine.
externalEvents = {}
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
         
    def mouse_moved(self, e):
        self.mover(e.getX(), e.getY())
         
        
class KA(KeyAdapter):
    def __init__(self, clicker):
        self.clicker = clicker
    def keyTyped(self, event):
        print("Key Pressed: " + str(event.getKeyChar()))
        self.clicker(event.getKeyChar())

# This is Jython code to interface with a graphics panel
class Canvas(JPanel):
    def __init__(self, drawer, click, move):
        super(Canvas, self).__init__()
        self.drawer = drawer
        self.click = click
        self.move = move
#        self.key = key
<<<<<<< Updated upstream
    self.addMouseListener(MA(lambda x, y: self.click(x, y)))
=======
<<<<<<< HEAD
        self.addMouseListener(MA(lambda x, y: self.click(x, y)))
        self.addMouseMotionListener(MLA(lambda x, y: self.move(x, y)))
=======
    self.addMouseListener(MA(lambda x, y: self.click(x, y)))
>>>>>>> 16b3d35c35e5e93a522da9ed93bcd79ef2685acf
>>>>>>> Stashed changes

def paint(self, g):
    JPanel.paint(self, g)
    self.drawer(g)

<<<<<<< Updated upstream
# This creates the drawing frame (Example is a stupid name ...)
=======
                                # This creates the drawing frame (Example is a stupid name ...)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        externalEvents['LeftMouseButton'] = SP2(x, y)   #SP2 inherited from pythonfrp StaticNumerics.py
=======
<<<<<<< HEAD
        externalEvents['LeftMouseButton']=SP2(x, y)
=======
        externalEvents['LeftMouseButton'] = SP2(x, y)   #SP2 inherited from pythonfrp StaticNumerics.py
>>>>>>> 16b3d35c35e5e93a522da9ed93bcd79ef2685acf
>>>>>>> Stashed changes
    def mykey(self, k):
        externalEvents['KeyTyped']=string(k)

    def my_move(self, x, y):
        mouse_pos[0]=(x, y)

    def initUI(self):
        self.addKeyListener(KA(lambda k: k))
<<<<<<< HEAD
        self.xp=0
        self.yp=0
        self.canvas=Canvas(lambda g:self.mypaint(g), lambda x, y: self.myclick(x, y), lambda x, y: my_move(x, y))
=======
        self.xp = 0
        self.yp = 0
        self.canvas = Canvas(lambda g:self.mypaint(g), lambda x, y: self.myclick(x, y))
<<<<<<< Updated upstream
=======
>>>>>>> 16b3d35c35e5e93a522da9ed93bcd79ef2685acf
>>>>>>> Stashed changes
        self.canvas.setBackground(Color(200, 200, 100))
        self.getContentPane().add(self.canvas)
        self.setTitle("Test")
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setSize(300, 300)
        self.setLocationRelativeTo(None)
        self.setBackground(Color(255, 255, 255))
        self.setVisible(True)
        self.timer=Timer(50, self)
        self.timer.start()

<<<<<<< Updated upstream
# This is the heartbeat handling code - this is attached to a timer in the frame      
=======
<<<<<<< HEAD
                                # This is the heartbeat handling code - this is attached to a timer in the frame      
=======
# This is the heartbeat handling code - this is attached to a timer in the frame      
>>>>>>> 16b3d35c35e5e93a522da9ed93bcd79ef2685acf
>>>>>>> Stashed changes
    def actionPerformed(self, e):
        currentTime=System.currentTimeMillis()
        del screenObjects[:]
<<<<<<< Updated upstream
#        print(currentTime-startTime[0])
#        print('Objects: ' + str(Globals.worldObjects))
    heartbeat((currentTime - startTime[0]) / 1000.0, externalEvents)
    externalEvents.clear()
    self.repaint()
=======
<<<<<<< HEAD
                                #        print(currentTime-startTime[0])
                                #        print('Objects: ' + str(Globals.worldObjects))
        heartbeat((currentTime - startTime[0]) / 1000.0, externalEvents)
        externalEvents.clear()
        self.repaint()
>>>>>>> Stashed changes

                                # This is the start function that initializes the reactive engine and then starts the animation
    def start():
        print("Starting...")
        startTime[0]=System.currentTimeMillis()
        initialize(0)
        Example()
        
=======
#        print(currentTime-startTime[0])
#        print('Objects: ' + str(Globals.worldObjects))
    heartbeat((currentTime - startTime[0]) / 1000.0, externalEvents)
    externalEvents.clear()
    self.repaint()

# This is the start function that initializes the reactive engine and then starts the animation
def start():
    print("Starting...")
    startTime[0] = System.currentTimeMillis()
    initialize(0)
    Example()

# From here on this is user code - create a moving circle on each mouse click that starts from the position of the click

def makeCircle(m, v):
    circle(p2(localTime * 50 + v.x, localTime * 50 + v.y)) #localtime inherited from pythonfrp functions.py 183

def makeSquare(m, v):
    square(p2(localTime * 50 + v.x, localTime * 50 + v.y)) #localtime inherited from pythonfrp functions.py 183
    
def makeTriangle(m, v):
    triangle(p2(localTime * 50 + v.x, localTime * 50 + v.y)) #localtime inherited from pythonfrp functions.py 183
    
def typeKey(m, v):
    print(string(v.k))

<<<<<<< Updated upstream

    
#def checkValidKey(s):
#    if s in keyRenamings:
#        return keyRenamings[s]
#    if type(s) is type("s"):
#        if len(s) == 1 or s in allKeyNames:      CODE FROM REACTIVEPANDA EXTERNALS.PY
#            return s
#    Errors.badKeyName(s)
#allKeyNames = ["escape", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "space"]
#
#keyRenamings = {"upArrow": "arrow_up", "downArrow": "arrow_down",
#    "leftArrow": "arrow_left", "rightArrow": "arrow_right"}  





# These methods handle signals from the GUI
    # Cache keypress events so there's no duplication of key events - not
    # sure this is useful but it can't hurt.  Probably not a good idea to
    # have multiple accepts for the same event.
  

# React to each mouse press by creating a new shape
react(lbp(), makeSquare)    #inherited from reactive2d Events2D 
react(kT(), typeKey)    #inherited from reactive2d Events2D 
=======
>>>>>>> Stashed changes

    
#def checkValidKey(s):
#    if s in keyRenamings:
#        return keyRenamings[s]
#    if type(s) is type("s"):
#        if len(s) == 1 or s in allKeyNames:      CODE FROM REACTIVEPANDA EXTERNALS.PY
#            return s
#    Errors.badKeyName(s)
#allKeyNames = ["escape", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "space"]
#
#keyRenamings = {"upArrow": "arrow_up", "downArrow": "arrow_down",
#    "leftArrow": "arrow_left", "rightArrow": "arrow_right"}  





# These methods handle signals from the GUI
    # Cache keypress events so there's no duplication of key events - not
    # sure this is useful but it can't hurt.  Probably not a good idea to
    # have multiple accepts for the same event.
  

# React to each mouse press by creating a new shape
react(lbp(), makeSquare)    #inherited from reactive2d Events2D 
react(kT(), typeKey)    #inherited from reactive2d Events2D 
>>>>>>> 16b3d35c35e5e93a522da9ed93bcd79ef2685acf

                                # From here on this is user code - create a moving circle on each mouse click that starts from the position of the click
                                #move to different file
                                #def makeCircle(m,v):
                                #    circle(p2(localTime*50+v.x,localTime*50+v.y))

                                #def makeSquare(m, v):
                                #    square(p2(localTime*50+v.x,localTime*50+v.y))
                                #    print""
                                #    
                                #def makeTriangle(m, v):
                                #    triangle(p2(localTime*50+v.x,localTime*50+v.y))
                                #    
                                #def typeKey(m, v):
                                #    print(string(v.k))

                                # React to each mouse press by creating a new circle
                                #react(lbp(),makeTriangle)
                                #react(lbp(), makeCircle)
                                #react(lbp(),makeSquare)

                                #react(kT(),typeKey)

                                # Start!
start()