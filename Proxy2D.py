# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from java.awt import Color
from java.lang import Math

from pythonfrp.Engine import *
from Globals2D import *
from Shapes import *
from pythonfrp.Numerics import *
from pythonfrp.Color import *
from java.awt import Graphics
from java.awt import Graphics2D
from java.awt.geom import Area
from java.awt.geom import Ellipse2D
from java.awt.geom import Rectangle2D
from java.awt.geom import AffineTransform

from jarray import array

class ScreenObject(Proxy.Proxy):
#    def __init__ (self, updater=None, types={}, name='', init=None, ** params):
#        Proxy.Proxy.__init__(self, name=name, updater=updater, types=types)
#        init(self, params)
        
    #Jay's part  
    def __init__ (self, updater = (lambda self: screenObjects.append(self)), types={}, name='',
    drawer = None, position = p2(0,0), zDepth = 0, zLayer = 0, color = red, scale = 1, height = 10, 
    width = 10, rotation = 0, texture = "None", useGrad = False, gradp1 = p2(0,0), gradp2 = p2(0,0), 
    gradc1 = red, gradc2 = red, duration = 0, center = p2(0.5,0.5),
    tp1 = p2(0, -1), tp2 = p2(1,1), tp3 = p2(-1, 1), ** params):
        Proxy.Proxy.__init__(self, name=name, updater=updater, types=types)
        self._drawer = drawer
        self.position = position
        self._zLayer = zLayer
        self.zDepth = zDepth
        self.color = color
        self.scale = scale
        self.height = height
        self.width = width
        self.rotation = rotation
        self.texture = texture
        self.useGrad = useGrad
        self.gradp1 = gradp1
        self.gradp2 = gradp2
        self.gradc1 = gradc1
        self.gradc2 = gradc2
        self.duration = duration
        self.center = center
        self.tp1 = tp1
        self.tp2 = tp2
        self.tp3 = tp3
        if duration > 0:
            react(self, delay(duration), exitScene)
        #self.gradientInfo = gradientInfo
        #print "Hello world!"
        
    def _draw(self, g):
        self._drawer(self, g)
        
    def getCollisionVector(self, object):
        pass #To be dicided by its subclasses
    
    def _applyTexture(self, method):
        pass #A placeholder pass.  I'm not sure if the method could be generizable or if it will have to be handled by each shape individually.
    #A crop won't, but if we want to stretch/compress the image to fit...we may.
    
    def update(self):
        print("UPDOOT")
        screenObjects.append(self);
        if self.duration > 0:
            print("REMOFE")
            react(self, delay(duration), exitScene)
            
    def _getArea(self):
        h = int((self._get("scale") * self._get("height")))
        w = int((self._get("scale") * self._get("width")))
        p = self._get("position")
        center = self._get("center")
        theta = self._get("rotation")
        ar = Area(Rectangle2D.Double(center.x - 1, center.y - 1, 1, 1))
        g = AffineTransform()
        g.translate(p.x, p.y)
        g.rotate(theta)
        g.scale(w, h)
        ar.transform(g)
        return ar
    def _touches(self, testObj, trace = False):
        if(trace):
            print("pos = " + self._get("position"))
        if(self._alive and testObj._alive):
            ar1 = self._getArea()
            ar2 = testObj._getArea()
            return ar1.intersects(ar2.getBounds2D())
        return False;

def _distance(o1, o2):
        return Math.sqrt(Math.pow(o2.x - o1.x,2) + Math.pow(o2.y - o1.y, 2))
        
        
def _collides(obj1, obj2):
    r1 = obj1.getCollisionVector(obj2) 
    r2 = obj2.getCollisionVector(obj1)
    #we know now where one object is relative to the other and now want to know when these points cross
    return distance(obj1.postion + r1 , obj2.postition + r2) <= 0

        
    #def _collision(self, p2):
        
        
        
        #bounding_box(self)
        
    #    self.params = params[BoundingBox((p2(self.params[x,y]), p2(self.params[x,y]), p2(self.params[x,y]), self.params[x,y]))]
        
#        self.params = params[BoundingBox(p2(params["position"]-params["width"]/2, params["position"]-params["height"]/2),p2(params["position"]+params["width"]/2, params["position"]-params["height"]/2),p2(params["position"]+params["width"]/2, params["position"]+params["height"]/2),p2(params["position"]-params["width"]/2, params["position"]-params["height"]/2))]
        
  
        
#        bottomLeft = p2(params["position"]-params["width"]/2, params["position"]-params["height"]/2)
#        bottomRight = p2(params["position"]+params["width"]/2, params["position"]-params["height"]/2)
#        topRight = p2(params["position"]+params["width"]/2, params["position"]+params["height"]/2)
#        topLeft = p2(params["position"]-params["width"]/2, params["position"]-params["height"]/2)
   #     width =  self._get("width")
   #     height = self._get("height")
   #     center = p2(self._get("position"))
        
 #       print "bottom left:  " + str(bottomLeft) + "    bottom right:  " + str(bottomRight) + "top left:  " + str(topLeft) + "top right:  " + str(topRight)
 #       print "position:  " + str(position)
  

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #    if(self.name == "square"):
            
        #    self.box = [p2(self._get("position")/2-self._get("width"), self._get("position")/2-self._get("height")), p2(self._get("position")/2-self._get("width"), self._get("position")/2+self._get("height"),p2(self._get("position")/2+self._get("width"), self._get("position")/2-self._get("height")),p2(self._get("position")/2+self._get("width"), self._get("position")/2+self._get("height")))]
     #       print "----------" + str(self.box)
        
#        print('Created Object')


    #---  touch logic for Shapes  ---#

#    def bound_square(object):
        

#    def _touches(self, handle, trace=False):
            
            #---  trace is for debugging not sure of the how, when, what or why  ---#
#            if trace:
 #               print("Touch: " + repr(self) + " " + repr(handle))
#            #print (repr(self._cRadius))
#            #print (repr(self.get("scale")))
#            
#            #---  catches zombies  ???  (other objects rely on deleted objects so they cant be deleted permanently)---#
 #           if not self._alive or not handle._alive:
 #               return False
#            
#            #---  me vs you position  ---#
#            mr = self._cRadius * self._get("scale")
#            mp = self._get("position") + p3(0, 0, 0)
#            yr = handle._cRadius * handle._get("scale")
#            yp = handle._get("position") + p3(0, 0, 0)
        
        #-----  Circle Handling  -----#    
 #           if self._name == "Circle":
#                obj_radius = self._get("radius")
#                obj_pos = self._get("position")
#                obj2_radius = self._get("radius")
#                obj2_pos = self._get("position")

            #---  determine if objects overlap  ---#
 #           dist = absP2(subP2(P2(obj_pos.x, obj_pos.y), P2(obj2_pos.x, obj2_pos.y)))
            
 #           if(dist > obj_radius + obj2_radius):
 #               return False
            
          #  else:
                
            
            
            
 #           if d > mr + yr:
 #                        return False
 #                    else:
 #                        cb = yp.z + handle._get("scale") * handle._cFloor
 #                        ct = yp.z + handle._get("scale") * handle._cTop
 #                        sb = mp.z-mr
 #                        st = mp.z + mr
 #                        # print str(cb) + " " + str(ct) + " " + str(sb) + " " + str(st)
 #                        if ct > sb and cb < st:
 #                            return True
 #                        else:
 #                            return False
            
        #-----  Square Handling  -----#     
 #           elif self._name == "Square":
 #               obj_pos = self._get("position")
 #               obj_width = self._get("width")
 #               obj_height = self._get("height")
                
        #-----  Triangle Handling  -----# 
#            elif self._name == "Triangle":
#                obj_pos = self._get("position")
                
                
#            if trace:
#                print (repr(mp) + " [" + repr(mr) + "] " + repr(yp) + " [" + repr(yr) + "]")
#
#            if self._cType == "sphere":
#            
#                if handle._cType == "sphere":
#                    return absP3(subP3(mp, yp)) < mr + yr
#        
#                elif handle._cType == "cyl": # Test if the x,y points are close enough. This treats the sphere as a cylinder
#                    d = absP2(subP2(P2(mp.x, mp.y), P2(yp.x, yp.y)))
#            
#                    if d > mr + yr:
#                        return False
#                    else:
#                        cb = yp.z + handle._get("scale") * handle._cFloor
#                        ct = yp.z + handle._get("scale") * handle._cTop
#                        sb = mp.z-mr
#                        st = mp.z + mr
#                        # print str(cb) + " " + str(ct) + " " + str(sb) + " " + str(st)
#                        if ct > sb and cb < st:
#                            return True
#                        else:
#                            return False
#            elif self._cType == "cyl":
#            
#                if handle._cType == "sphere":
#                    d = absP2(subP2(P2(mp.x, mp.y), P2(yp.x, yp.y)))
#                    # print "c to s (dist = " + str(d) + ")"
#            
#                    if d > mr + yr:
#                        return False
#                    else:
#                        cb = mp.z + self._get("scale") * self._cFloor
#                        ct = mp.z + self._get("scale") * self._cTop
#                        sb = yp.z-yr
#                        st = yp.z + yr
#                        # print str(cb) + " " + str(ct) + " " + str(sb) + " " + str(st)
#                        return ct > sb and cb < st
#                elif handle._cType == "cyl":
#                    # print str(mp.x) + " , " + str(mp.y)
#                    d = absP2(subP2(P2(mp.x, mp.y), P2(yp.x, yp.y)))
#                
#                    if trace:
#                        print ("c to c (dist = " + str(d) + ") " + str(mr + yr))
#                
#                    if d > mr + yr:
#                        return False
#                
#                    else:
#                        res = self._cTop + mp.z > handle._cFloor + yp.z and self._cFloor + mp.z < handle._cTop + yp.z
#                        if trace:
#                            print("Result: " + str(res) + " " + str((self._cTop, mp.z, handle._cFloor, yp.z, self._cFloor, handle._cTop)))
                        #print ("*****"+repr(res))
                   #     return res
