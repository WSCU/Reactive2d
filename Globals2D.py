from pythonfrp.Engine import *
from pythonfrp.StaticNumerics import *


#--- all the tings that appear on screen as programs runs, a bunch of lambdas  ---#
screenObjects = []

#---  record start time to subtract from current time  ---#
startTime = [0]

#---  track mouse position as program runs  ---#
mouse_pos = [SP2(0,0)]