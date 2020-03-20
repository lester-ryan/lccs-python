# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of turtle graphics
from turtle import *

# set the appearance of the turtle
def setAppearance():
    hideturtle()
    color('red')
    pensize(5)

# Draw angle #1
def drawAngle(size, arm1Len, arm2Len):
    backward(arm1Len)
    left(size)
    forward(arm2Len)


# Position the pen
def setPenPosition():
    penup()
    setpos(200, 0)
    setheading(0)
    pendown()


# Main program starts here
# Main program starts here
setAppearance()
drawAngle(30, 50, 50)
setPenPosition()
drawAngle(60, 100, 200)