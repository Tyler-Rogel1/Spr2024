from graphics import *
class Stack:
    def __init__(self):
        self.list = []
    def push(self, x):
        self.list.append(x)
    def pop(self):
        if not self.isEmpty():
            return self.list.pop()
    def isEmpty(self):
        return len(self.list) == 0
    def top(self):
        if not self.isEmpty():
            return self.list[-1]

def infixToPostfix(infix):
# infix and postfix are strings
# postfix does not need parenthesis
# all operators get pushed onto the stack
# new pushes to the stack go on top of stack
# if new push is lower or equal priority by pemdas then it pops of whats under it unless protected by left paren
# numbers go straight to postfix
# once characters are all on postfix, pop things from stack to postfix
# "3*4 + 5*6" at infix becomes "3 4 * 5 6 *+" at postfix
# "3+4/2-5" at infix becomes "342/+5-" 
# "x*x/(x-3)" to "xx*x3-/"
# "1+2/(3*4-(5+6/7)+8)-9" to "1234*567/+-8+/+9-"

# "x+2*(x-3+(4/x-5)*6)/7"
# "x2x3-4x/5-6*++*7/" is a guess its actually "x2x3-4x/5-6*+*7/+"
# 
    postfix = ""
    S = Stack()
    for c in infix:
        if c in "0123456789x":
            postfix += c
        if c in "+-":
            while not S.isEmpty() and S.top() in "+-*/":
                postfix += S.pop()
            S.push(c)
        if c in "*/":
            while not S.isEmpty() and S.top() in "*/":
                postfix += S.pop()
            S.push(c)
        if c == "(":
            S.push(c)
        if c == ")":
            while S.top() != "(":
                postfix += S.pop()
            S.pop()
    while not S.isEmpty():
        postfix += S.pop()
    return postfix

def evaluatePostfix(postfix, x):
    # "342/+5-"
    # numbers go to stack
    # divide here does last two on stack, lower operator upper format
    # "x2+x4-/" current x = 5 -> "7"
    S = Stack()
    for c in postfix:
        if c in "0123456789":
            S.push(float(c))
        if c == "x":
            S.push(x)
        if c == "+":
            R = S.pop()
            L = S.pop()
            S.push(L + R)
        if c == "-":
            R = S.pop()
            L = S.pop()
            S.push(L - R)
        if c == "*":
            R = S.pop()
            L = S.pop()
            S.push(L * R)
        if c == "/":
            R = S.pop()
            L = S.pop()
            S.push(L / R)
    
    return S.pop()

def main():
    infix = input("infix? ")
    print("INFIX: ", infix)
    postfix = infixToPostfix(infix)
    print("POSTFIX: ", postfix)
    print("EVALUATE with x = 1: ", evaluatePostfix(postfix, 1))
    win = GraphWin("Graphing Calc", 1000, 1000)
    xlow = -10
    xhigh = 10
    ylow = -10
    yhigh = 10
    win.setCoords(xlow, ylow,xhigh,yhigh)
    res = .005
    x = xlow
    while x < xhigh:
        y = evaluatePostfix(postfix, x)
        # x2 = x + res
        # y2 = x2 *x2
        l = Point(x, y)
        l.draw(win)
        x +=res

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()