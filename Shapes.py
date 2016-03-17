 
#from pythonfrp.Numerics import *
#from Globals import *
from Proxy2D import *
from pythonfrp.Color import *
import java.awt.Color as JavaColor
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
    


#Circle
#This user level

#Jay stuff...
#gradientInfo is going to be a list of information about a gradient.
#the format will be like so:
#[startP2, startColor, endP2, endColor]
#where startColor and endColor are assumed to be pythonFRP colors.
#If there aren't enough arguments, we skip all the gradient crap and fill it with a solid color.
def circle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None", gradientInfo = []):
    return ScreenObject(types = {}, name = 'Circle',  drawer = drawCircle, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture, gradientInfo = gradientInfo)

def drawCircle(self, g):
    
    p = self._get("position")
    h = int((self._get("size") * self._get("skew")))
    w = self._get("size")
    grad = self._get("gradientInfo")
    shape = Ellipse2D.Double(int(p.x-(w/2)), int(p.y-(h/2)), w, h)
    g.rotate(self._get("rotation"))
    if len(grad) != 4:
        g.setPaint(toJavaColor(self._get("color")))
        g.fill(shape);
    else:
        theGradient = GradientPaint(grad[0].x, grad[0].y, toJavaColor(grad[1]), grad[2].x, grad[2].y, toJavaColor(grad[3]));
        g.setPaint(theGradient);
        g.fill(shape);
    
#A
class Circle(ScreenObject):
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * radius
        return collisionVector




#Square

#J
def square(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None", gradientInfo = []):

    return ScreenObject(types = {}, name = 'Square', drawer = drawSquare, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture, gradientInfo = gradientInfo) 

def drawSquare(self, g):
    h = int((self._get("size") * self._get("skew")))
    p = self._get("position")
    w = self._get("size")
    grad = self._get("gradientInfo")
    shape = Rectangle2D.Double(int(p.x-(w/2)), int(p.y-(h/2)), w, h)
    g.rotate(self._get("rotation"))
    if len(grad) != 4:
        g.setPaint(toJavaColor(self._get("color")))
        g.fill(shape);
    else:
        theGradient = GradientPaint(grad[0].x, grad[0].y, toJavaColor(grad[1]), grad[2].x, grad[2].y, toJavaColor(grad[3]));
        g.setPaint(theGradient);
        g.fill(shape);
#A
class Square(ScreenObject):
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * height
        return collisionVector
    
 
  
  
#Triangle

#J
def triangle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None", gradientInfo = []):
    return ScreenObject(types = {},
        name = 'Triangle', drawer = drawTriangle, position = position, zDepth = zDepth, 
        zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture, gradientInfo = gradientInfo)
        
def drawTriangle(self, g):
    #print("Inside drawTriangle")
    g.setColor(JavaColor(0,0,255))
    r = self._get("size");
    p = self._get("position")
    xs = array([int(p.x), int(p.x-Math.sqrt((r*r)/2)), int(p.x+Math.sqrt((r*r)/2))], 'i')
    ys = array([int(p.y-25), int(p.y+Math.sqrt((r*r)/2)), int(p.y+Math.sqrt((r*r)/2))], 'i')
    g.fillPolygon(xs, ys, 3)
 
#A
class Triangle(ScreenObject):
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * 15
        return collisionVector

def toJavaColor(c):
    if(type(c) is JavaColor):
        return c
    else:
        r = int(min(max(c.r * 255, 0), 255))
        g = int(min(max(c.g * 255, 0), 255))
        b = int(min(max(c.b * 255, 0), 255))
        return JavaColor(r, g, b)
    