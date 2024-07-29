from graphics import *

#draws an egg

#
## Functions
#

def draw_egg(win, center, width, height):
    # Draw the outer ellipse (egg shape)
    egg = Oval(Point(center.getX() - width / 2, center.getY() - height / 2), 
               Point(center.getX() + width / 2, center.getY() + height / 2))
    #color the egg in white
    egg.setFill('white')
    #set border to white
    egg.setOutline('white')
    #draws the egg in the window i define later
    egg.draw(win)

#
## Rendering
#

# Create a window
win = GraphWin("This is an egg", 400, 500)
win.setBackground("blue")

# Set the center point, width, and height of the egg
center = Point(200, 200)
width = 200
height = 300

# Draw the egg
draw_egg(win, center, width, height)

# Wait for a mouse click to close the window
win.getMouse()# Pause to view result  
win.close()# Close window when done