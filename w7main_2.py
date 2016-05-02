import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.shape("turtle")
t1.speed(3)
def saveTracks():
 t1.penup()
 mytracks=list()
 t1.goto(-300,300)
 mytracks.append(t1.pos())
 t1.pendown()
 t1.pencolor("Red")
 t1.fd(310)
 mytracks.append(t1.pos())
 t1.right(90)
 t1.fd(600)
 mytracks.append(t1.pos())
 t1.left(90)
 t1.fd(110)
 mytracks.append(t1.pos())
 t1.left(90)
 t1.fd(270)
 mytracks.append(t1.pos())
 t1.right(90)
 t1.fd(160)
 mytracks.append(t1.pos())
 t1.right(90)
 t1.fd(270)
 mytracks.append(t1.pos())
 return mytracks

def replayTracks(mytracks):
 t1.penup()
 t1.home()
 t1.pendown()
 t1.pencolor("Blue")
 for i in mytracks:
  t1.goto(i)

def lab7():
 mytracks=saveTracks()
 replayTracks(mytracks)
 
def main():
 lab7()

main()
raw_input("201611069")
wn.exitonclick()