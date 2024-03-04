from graphics import *
# class Stack:
#     def __init__(self):
    
#     def push(self):
        
#     def pop(self):

def infixToPostfix(infix):
# infix and postfix are strings
# postfix does not need parenthesis
# all operators get pushed onto the stack
# new pushes to the stack go on top of stack
# if new push is lower or equal priority by pemdas then it pops of whats under it unless protected by left paren
# numbers go straight to postfix
# once characters are all on postfix, pop things from stack to postfix
# "3*4 + 5*6" at infix becomes "3 4 * 5 6 +" at postfix
# "3+4/2-5" at infix becomes "342/+5-" 
# "x*x/(x-3)" to "xx*x3-/"
# "1+2/(3*4-(5+6/7)+8)-9" to "1234*567/+-8+/+9-"
# 
    return postfix

def evaluatePostfix(postfix, x):
    # "342/+5-"
    # numbers go to stack
    # divide here does last two on stack, lower operator upper format
    return

def main():
    infix = input("infix? ")
    postfix = infixToPostfix(infix)
    win = GraphWin("My Circle", 1000, 1000)
    xlow = -10
    xhigh = 10
    ylow = -10
    yhigh = 10
    win.setCoords(xlow, ylow,xhigh,yhigh)
    res = .1
    x = xlow
    while x < xhigh:
        y = evaluatePostFix(postfix, x)
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