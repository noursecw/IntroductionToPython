"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Charles Nourse.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

steven = rg.SimpleTurtle('turtle')
steven.pen = rg.Pen('green', .11)
steven.speed = 30
steven.left(90)

geoff = rg.SimpleTurtle()
geoff.pen = rg.Pen('orange', .7)
geoff.speed = 12
geoff.right(90)

for k in range(173):
    steven.draw_circle((k * 30) - k)
    geoff.draw_circle((k * 30) + k)
    steven.pen = rg.Pen('orange', .11 * k)
    geoff.pen = rg.Pen('green', .7 * k)
    steven.forward(k)
    geoff.forward(k)

window.close_on_mouse_click()
