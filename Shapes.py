 
#from pythonfrp.Numerics import *
#from Globals import *
from Proxy2D import *
import java.awt.Color as JavaColor
#import math.pi as pi
    


#Circle
#This user level
<<<<<<< Updated upstream
def circle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
    return ScreenObject(types = {}, name = 'Circle',  drawer = drawCircle, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture)
    

=======
def circle(position, radius = 20):
    return ScreenObject(updater = circleUpdate, types = {"position": p2Type,
        "radius": numType}, name = 'Circle', init = circleInit, drawer = drawCircle, position = position,  
        radius = radius)
 
#Reactive Stuff
def circleInit(so, params):
    so.position = params["position"]
    so.radius = params["radius"]

#Gets the things that are requried to draw a circle
def circleUpdate(self):
 
    screenObjects.append(self)
    


#Circle Drawing code
>>>>>>> Stashed changes
 
def drawCircle(self, g):
    g.setColor(JavaColor(255,0,0))
    p = self._get("position")
    r = self._get("size")
    g.fillOval(int(p.x-r), int(p.y-r), int(2*r), int(2*r))

#Square


<<<<<<< Updated upstream
def square(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
    
    return ScreenObject(types = {}, name = 'Square', 
        drawer = drawSquare, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture) 

 
  
=======
def square(position, height = 20, width = 40):
 
    return ScreenObject(updater = squareUpdater, types = {"position": p2Type,
        "width": numType, "height": numType}, name = 'Square', init = squareInit,
        drawer = drawSquare, position = position, width = width, height = height) 

 
def squareInit(so, params):
    so.position = params["position"]
    so.width = params["width"]
    so.height = params["height"]
   
 
def squareUpdater(self):
    screenObjects.append(self)
    
     
>>>>>>> Stashed changes
def drawSquare(self, g):
    #print("Inside drawSquare")
    g.setColor(JavaColor(0,255,0))
    p = self._get("position")
    w = self._get("size")
    h = self._get("size")
    g.fillRect(int(p.x-(w/2)), int(p.y-(h/2)), w, h) 
 
    
#Triangle
<<<<<<< Updated upstream
def triangle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
    return ScreenObject(types = {},
        name = 'Triangle', drawer = drawTriangle, position = position, zDepth = zDepth, 
        zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture)
        
=======
def triangle(position):
    return ScreenObject(updater = triangleUpdater, types = {"position": p2Type},
        name = 'Triangle', init = triangleInit, drawer = drawTriangle, position = position)

def triangleInit(so, params):
    so.position = params["position"]

def triangleUpdater(self):
    screenObjects.append(self)
>>>>>>> Stashed changes
 
def drawTriangle(self, g):
    #print("Inside drawTriangle")
    g.setColor(JavaColor(0,0,255))
    r = self._get("size");
    p = self._get("position")
    xs = array([int(p.x), int(p.x-Math.sqrt((r*r)/2)), int(p.x+Math.sqrt((r*r)/2))], 'i')
    ys = array([int(p.y-25), int(p.y+Math.sqrt((r*r)/2)), int(p.y+Math.sqrt((r*r)/2))], 'i')
    g.fillPolygon(xs, ys, 3)