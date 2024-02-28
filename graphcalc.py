from graphics import *
# class Stack:
#     def __init__(self):
    
#     def push(self):
        
#     def pop(self):
    

def main():
    win = GraphWin("My Circle", 1000, 1000)
    xlow = -10
    xhigh = 10
    ylow = -10
    yhigh = 10
    win.setCoords(xlow, ylow,xhigh,yhigh)
    res = .1
    x = xlow
    while x < xhigh:
        y = x*x
        x2 = x + res
        y2 = x2 *x2
        l = Line(Point(x,y), Point(x2,y2))
        c = Circle(Point(x,y), 1)
        c.draw(win)
        l.draw(win)
        x +=res

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()