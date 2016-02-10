# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from java.awt import Color
from java.lang import Math

import pythonfrp.Proxy as Proxy
from pythonfrp.Numerics import *
from Globals2D import *

from jarray import array

class ScreenObject(Proxy.Proxy):
    def __init__ (self, updater=None, types={}, name='', init=None, ** params):
        Proxy.Proxy.__init__(self, name=name, updater=updater, types=types)
        init(self, params)
#        print('Created Object')


    #---  touch logic for Shapes  ---#
#    def _touches(self, handle, trace=False):
            
            #---  trace is for debugging not sure of the how, when, what or why  ---#
##            if trace:
 #               print("Touch: " + repr(self) + " " + repr(handle))
#            #print (repr(self._cRadius))
#            #print (repr(self.get("size")))
#            
#            #---  catches zombies  ???  (other objects rely on deleted objects so they cant be deleted permanently)---#
 #           if not self._alive or not handle._alive:
 #               return False
#            
#            #---  me vs you position  ---#
#            mr = self._cRadius * self._get("size")
#            mp = self._get("position") + p3(0, 0, 0)
#            yr = handle._cRadius * handle._get("size")
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
 #                        cb = yp.z + handle._get("size") * handle._cFloor
 #                        ct = yp.z + handle._get("size") * handle._cTop
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
#                        cb = yp.z + handle._get("size") * handle._cFloor
#                        ct = yp.z + handle._get("size") * handle._cTop
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
#                        cb = mp.z + self._get("size") * self._cFloor
#                        ct = mp.z + self._get("size") * self._cTop
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