# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from Reactive2D  import *
from DodgeGUI import startGame

paddle = [p2(150,150)]
square(paddle[0],20,20)

def keyPressed(self, k):
    if (k == "Left"):
        if (paddle[0].x > 20):
            paddle[0].x -= 5
    if (k == "Right"):
        if (paddle[0].x < 465):
            paddle[0].x += 5
    if (k == "Up"):
        if (paddle[0].y > 20):
            paddle[0].y -= 5
    if (k == "Down"):
        if (paddle[0].y < 440):
            paddle[0].y += 5
 
react(kT(), keyPressed)

startGame()