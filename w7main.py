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
 mytrack=drawSquareAtSave(150, (100,100))
 print mytrack
    
def main():
 lab7a()

main()
raw_input("201611069")
wn.exitonclick()