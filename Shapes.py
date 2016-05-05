 
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
from java.awt.geom import Path2D
from java.awt import RenderingHints
from javax.swing import JApplet
from javax.swing import JFrame
from java.awt import Image
from javax.imageio import *
from java.net import URL
from java.io import *
from java.awt import TexturePaint
from java.awt import Rectangle
from java.awt.image import BufferedImage

from java.awt.geom import AffineTransform


#Circle
#This user level

#Jay stuff...
#gradientInfo is going to be a list of information about a gradient.
#the format will be like so:
#[startP2, startColor, endP2, endColor]
#where startColor and endColor are assumed to be pythonFRP colors.
#If there aren't enough arguments, we skip all the gradient crap and fill it with a solid color.
def circle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, scale = 1, rotation = 0, height = 10, width = 10, 
    gradient = None, duration = 0, center = p2(0.5,0.5)):
    return ScreenObject(types = {}, area = circularea, name = 'Circle',  drawer = drawCircle, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, scale = scale, rotation = rotation, height = height, width = width, 
        gradient = gradient, duration = duration, center = center)


def drawCircle(self, g):
    offset = self._get("center")
    shape = Ellipse2D.Double(-offset.x, -offset.y, 1, 1)
    genericDraw(self, shape, g);
    
def circularea(self, offset):
    return Area(Ellipse2D.Double(-offset.x, -offset.y, 1, 1))
    
    
    
def square(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, scale = 1, rotation = 0, height = 10, width = 10, 
    gradient = None, duration = 0, center = p2(0.5,0.5)):
    return ScreenObject(types = {}, name = 'Square', drawer = drawSquare, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, scale = scale, rotation = rotation, height = height, width = width,  
        gradient = gradient, duration = duration, center = center) 

def drawSquare(self, g):
    offset = self._get("center")
    shape = Rectangle2D.Double(-offset.x, -offset.y, 1, 1)
    #if(self._get("texture") == "None"):
    genericDraw(self, shape, g)
    
    
    
#Triangle
def triangle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, scale = 1, rotation = 0, height = 10, width = 10, 
    gradient = None, tp1 = p2(0,-1), tp2 = p2(1, 1), tp3 = p2(-1, 1), center = p2(0.5,0.5), duration = 0):
    return ScreenObject(types = {},
        name = 'Triangle', drawer = drawTriangle, area = triarea, position = position, zDepth = zDepth, 
        zLayer = zLayer, color = color, scale = scale, rotation = rotation, height = height, width = width, 
        gradient = gradient, tp1 = tp1, tp2 = tp2, tp3 = tp3, center = center, duration = duration)
        
def drawTriangle(self, g):
    offset = self._get("center")
    shape = Path2D.Double()
    first = self._get("tp1")
    second = self._get("tp2")
    third = self._get("tp3")
    shape.moveTo(first.x - offset.x, first.y - offset.y)
    shape.lineTo(second.x - offset.x, second.y - offset.y)
    shape.lineTo(third.x - offset.x, third.y  - offset.y)
    shape.lineTo(first.x - offset.x, first.y  - offset.y)
    genericDraw(self, shape, g);
    
def triarea(self, offset):
    shape = Path2D.Double()
    first = self._get("tp1")
    second = self._get("tp2")
    third = self._get("tp3")
    shape.moveTo(first.x - offset.x, first.y - offset.y)
    shape.lineTo(second.x - offset.x, second.y - offset.y)
    shape.lineTo(third.x - offset.x, third.y  - offset.y)
    shape.lineTo(first.x - offset.x, first.y  - offset.y)
    return Area(shape)
    
#Polygon
def polygon(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, scale = 1, rotation = 0, height = 10, width = 10, 
    gradient = None, center = p2(0.5,0.5), duration = 0, polyPoints = []):
    SO =  ScreenObject(types = {},
        name = 'Polygon', drawer = drawPoly, area = polyarea, position = position, zDepth = zDepth, 
        zLayer = zLayer, color = color, scale = scale, rotation = rotation, height = height, width = width, 
        gradient = gradient, center = center, duration = duration)
    SO._polyPoints = polyPoints
    return SO
        
def drawPoly(self, g):
    if(len(self._polyPoints) > 2):
        points = self._polyPoints
        offset = self._get("center")
        shape = Path2D.Double()
        shape.moveTo(points[0].x - offset.x, points[0].y - offset.y)
        for i in range (len(points)):
            shape.lineTo(points[i].x - offset.x, points[i].y - offset.y)
        genericDraw(self, shape, g);
        
def polyarea(self, offset):
    if(len(self._polyPoints) > 2):
        points = self._polyPoints
        shape = Path2D.Double()
        shape = Path2D.Double()
        shape.moveTo(points[0].x - offset.x, points[0].y - offset.y)
        for i in range (len(points)):
            shape.lineTo(points[i].x - offset.x, points[i].y - offset.y)
        return Area(shape)
    else:
        return squarea(self, offset)



    
def image(texture = "None", position = p2(0,0), zDepth = 0, zLayer = 0, scale = 1, rotation = 0, height = 10, width = 10, duration = 0, center = p2(0.5,0.5)):
    SO = None
    try:
        img = ImageIO.read(File(texture))
        SO = ScreenObject(types = {}, name = 'Image', drawer = drawImage, position = position, 
        zDepth = zDepth, zLayer = zLayer, scale = scale, rotation = rotation, height = height, width = width,  
        texture = texture, duration = duration, center = center)
        SO._img = img;
    except IIOException:
        print "Bad image path!"
        print (texture + " not found! I blame these stupid absolute image paths.")
        SO = ScreenObject(types = {}, name = 'Square', drawer = drawSquare, position = position, 
        zDepth = zDepth, zLayer = zLayer, scale = scale, rotation = rotation, height = height, width = width,  
        texture = texture, duration = duration, center = center)
    return SO

def drawImage(self, g):
    p = self._get("position")
    h = int((self._get("scale") * self._get("height")))
    w = int((self._get("scale") * self._get("width")))
    theta = self._get("rotation")
    oldForm = g.getTransform()
    g.translate(p.x, p.y)
    g.rotate(theta)
    rh = RenderingHints( RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g.setRenderingHints(rh);
    offset = self._get("center")
    g.drawImage(self._img, int(-offset.x * w), int(-offset.y * h), w, h, JavaColor(0,0,0), None)
    g.setTransform(oldForm)
    
 
#A





def genericDraw(self, shape, g):
    p = self._get("position")
    h = int((self._get("scale") * self._get("height")))
    w = int((self._get("scale") * self._get("width")))
    theta = self._get("rotation")
    oldForm = g.getTransform()
    g.translate(p.x, p.y)
    g.rotate(theta)
    g.scale(w, h)
    rh = RenderingHints( RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    g.setRenderingHints(rh);
    gradient = self._gradient
    if type(gradient) is GradientPaint:
        offset = self._get("center")
        p1 = gradient.getPoint1()
        p2 = gradient.getPoint2()
        color = GradientPaint(p1.x - offset.x, p1.y - offset.y, gradient.getColor1(),
                              p2.x - offset.x, p2.y - offset.y, gradient.getColor2())
        g.setPaint(color)
        g.fill(shape);
    else:
        color = self._get("color")
        g.setPaint(toJavaColor(color));
        g.fill(shape);
    g.setTransform(oldForm)

def toJavaColor(c):
    if(type(c) is JavaColor):
        return c
    else:
        r = int(min(max(c.r * 255, 0), 255))
        g = int(min(max(c.g * 255, 0), 255))
        b = int(min(max(c.b * 255, 0), 255))
        return JavaColor(r, g, b)
    