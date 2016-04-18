import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
def drawSquareAtSave(size, pos):
 t1.penup()
 t1.setpos(pos)
 t1.pendown()
 tracks=list()
 for i in range(0,4):
  tracks.append(t1.pos())
  t1.fd(size)
  t1.right(90)
 return tracks

def lab7a():
 mytrack=drawSquareAtSave(150, (-150,-150))
 print mytrack

tracks=dict()
tracks=({1:(150,0),2:(150,150),3:(0,150),4:(0,0)})
def drawSquareFrom():
 for i in range(1,5):
  t1.goto(tracks[i])

def lab7b():
 t1.penup()
 t1.goto(0,0)
 t1.pendown()
 drawSquareFrom()
 
def main():
 lab7a()
 lab7b()

main()
raw_input("201611069")
wn.exitonclick()
