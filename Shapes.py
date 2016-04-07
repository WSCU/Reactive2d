 
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
from java.awt import RenderingHints
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
def circle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None", useGrad = False, gradp1 = p2(0,0), gradp2 = p2(0,0), gradc1 = red, gradc2 = red, duration = 0):
    return ScreenObject(types = {}, name = 'Circle',  drawer = drawCircle, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, 
        texture = texture, useGrad = useGrad, gradp1 = gradp1, gradp2 = gradp2, gradc1 = gradc1, gradc2 = gradc2, duration = duration)

def drawCircle(self, g):
    
    p = self._get("position")
    h = int((self._get("size") * self._get("skew")))
    w = self._get("size")
    theta = self._get("rotation")
    useGrad = self._get("useGrad")
    oldForm = g.getTransform()
    g.translate(p.x, p.y)
    g.rotate(theta)
    g.scale(w/2, h/2)
    
    rh = RenderingHints( RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g.setRenderingHints(rh);
    
    
#    if(theta != 0):
#        r = sqrt((p.x * p.x) + (p.y * p.y))
#        oldTheta = atan2(p.y, p.x)
#        newTheta = oldTheta - theta
#        x = r * cos(newTheta)
#        y = r * sin(newTheta)
#    else:
#        x = p.x
#        y = p.y
        
    shape = Ellipse2D.Double(-1, -1, 2, 2)
    if not useGrad:
        g.setPaint(toJavaColor(self._get("color")))
        g.fill(shape);
    else:
        rGradx1 = self._get("gradp1").x
        rGradx2 = self._get("gradp2").x
        rGrady1 = self._get("gradp1").y
        rGrady2 = self._get("gradp2").y 
        gradc1 = self._get("gradc1")
        gradc2 = self._get("gradc2")
        theGradient = GradientPaint(rGradx1, rGrady1, toJavaColor(gradc1), rGradx2, rGrady2, toJavaColor(gradc2));
        g.setPaint(theGradient);
        g.fill(shape);
    g.setTransform(oldForm)
    
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
def square(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None", useGrad = False, gradp1 = p2(0,0), gradp2 = p2(0,0), gradc1 = red, gradc2 = red, duration = 0):

    return ScreenObject(types = {}, name = 'Square', drawer = drawSquare, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, 
        texture = texture, useGrad = useGrad, gradp1 = gradp1, gradp2 = gradp2, gradc1 = gradc1, gradc2 = gradc2, duration = duration) 

def drawSquare(self, g):
    h = int((self._get("size") * self._get("skew")))
    p = self._get("position")
    w = self._get("size")
    theta = self._get("rotation")
    useGrad = self._get("useGrad")
    oldForm = g.getTransform()
    g.translate(p.x, p.y)
    g.rotate(theta)
    g.scale(w/2, h/2)
    
    rh = RenderingHints( RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g.setRenderingHints(rh);
    
    
#    if(theta != 0):
#        r = sqrt((p.x * p.x) + (p.y * p.y))
#        oldTheta = atan2(p.y, p.x)
#        newTheta = oldTheta - theta
#        x = r * cos(newTheta)
#        y = r * sin(newTheta)
#    else:
#        x = p.x
#        y = p.y
        
    shape = Rectangle2D.Double(-1, -1, 2, 2)
    if not useGrad:
        g.setPaint(toJavaColor(self._get("color")))
        g.fill(shape);
    else:
        rGradx1 = self._get("gradp1").x
        rGradx2 = self._get("gradp2").x
        rGrady1 = self._get("gradp1").y
        rGrady2 = self._get("gradp2").y 
        gradc1 = self._get("gradc1")
        gradc2 = self._get("gradc2")
        theGradient = GradientPaint(rGradx1, rGrady1, toJavaColor(gradc1), rGradx2, rGrady2, toJavaColor(gradc2));
        g.setPaint(theGradient);
        g.fill(shape);
    g.setTransform(oldForm)
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
def triangle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None", useGrad = False, gradp1 = p2(0,0), gradp2 = p2(0,0), gradc1 = red, gradc2 = red):
    return ScreenObject(types = {},
        name = 'Triangle', drawer = drawTriangle, position = position, zDepth = zDepth, 
        zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, 
        texture = texture, useGrad = useGrad, gradp1 = gradp1, gradp2 = gradp2, gradc1 = gradc1, gradc2 = gradc2)
        
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
    