import turtle
wn=turtle.Screen()
wn.bgpic('myMaze.gif')
t1=turtle.Turtle()
t1.shape('turtle')
t1.color('Green')
t2=turtle.Turtle()
import math
def t1set():
 t1.penup()
 t1.setpos(0,0)
 t1.pendown()

def drawCircle():
 t2.penup()
 t2.setpos(150,150)
 t2.pendown()
 t2.circle(100)

def drawRectangle():
 t2.penup()
 t2.setpos(150,50)
 t2.pendown()
 for i in range(0,4):
  t2.fd(100)
  t2.right(90)

def drawLine():
 t2.penup()
 t2.setpos(-200,-50)
 t2.pendown()
 t2.fd(200)

def isInCircle(center,radius,pos):
 c=center
 return 0<(math.sqrt(math.pow(c[0]-pos[0],2)+math.pow(c[1]-pos[1],2)))<(radius)

def isInRectangle(curpos,coord):
 xs=coord[0][0]
 xe=coord[1][0]
 ys=coord[0][1]
 ye=coord[1][1]
 return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye

def isOnLine(pt,pos1,pos2):
 x1=pos1[0]-2
 y1=pos1[1]-2
 x2=pos2[0]+2
 y2=pos2[1]+2
 return isInRectangle(pt,[(x1,y1),(x2,y2)])

def keyup():
 pt=t1.pos()
 t1.fd(50)
 if isInCircle(center,radius,pt):
  t2.pencolor('red')
  drawCircle()
  t1set()
  t2.penup()
  t2.home()
  t2.pendown()
 elif isInRectangle(pt,coord):
  t2.pencolor('red')
  drawRectangle()
  t1set()
  t2.penup()
  t2.home()
  t2.pendown()
 elif isOnLine(pt,pos1,pos2):
  t2.pencolor('red')
  drawLine()
  t1set()
  t2.penup()
  t2.home()
  t2.pendown()

def keyleft():
 t1.left(45)

def keyright():
 t1.right(45)

def keydown():
 pt=t1.pos()
 t1.backward(25)
 if isInCircle(center,radius,pt):
  t2.pencolor('red')
  drawCircle()
  t1set()
  t2.penup()
  t2.home()
  t2.pendown()
 elif isInRectangle(pt,coord):
  t2.pencolor('red')
  drawRectangle()
  t1set()
  t2.penup()
  t2.home()
  t2.pendown()
 elif isOnLine(pt,pos1,pos2):
  t2.pencolor('red')
  drawLine()
  t1set()
  t2.penup()
  t2.home()
  t2.pendown()

def addKeys():
 wn.onkey(keyup,'Up')
 wn.onkey(keydown,'Down')
 wn.onkey(keyright,'Right')
 wn.onkey(keyleft,'Left')
 wn.onkey(wn.bye,'q')

def mousegoto(x,y):
 t1.setpos(x,y)
 pt=t1.pos()
 if isInCircle(center,radius,pt):
  t2.pencolor('red')
  drawCircle()
  t1set()
  t2.penup()
  t2.home()
  t2.pendown()
 elif isInRectangle(pt,coord):
  t2.pencolor('red')
  drawRectangle()
  t1set()
  t2.penup()
  t2.home()
  t2.pendown()
 elif isOnLine(pt,pos1,pos2):
  t2.pencolor('red')
  drawLine()
  t1set()
  t2.penup()
  t2.home()
  t2.pendown()

def addmouse():
 wn.onclick(mousegoto)

center=(150,250)
coord=[(-200,20),(-50,170)]
line1=[(-200,-80),(0,-80)]
pos1=line1[0]
pos2=line1[1]
radius=100
def playGame():
 t1set()
 drawCircle()
 drawRectangle()
 drawLine()
 addKeys()
 addmouse()
 wn.listen()
 turtle.mainloop()

def lab11_main4_5_6():
 playGame()

def main():
 lab11_main4_5_6()

main()
if __name__=="__main__":
 main()