from pythonfrp.Engine import *

#left mouse button event observer
def lbp():
    return eventObserver('LeftMouseButton')

#---  key typed event observer  ---#
#Most keys get identified as Strings
#All the letters are Capital
#Arrow keys are Left, Right, Up, Down respectively
#Keys that dont work are tab
#and things that need to be shifted like # and ^
def kT():
    return eventObserver('KeyTyped')
def kP():
    return eventObserver('KeyPressed')