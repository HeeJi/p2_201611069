import turtle
wn=turtle.Screen()
d1=turtle.Turtle()
wn.bgcolor("Lightblue")
def Triangle():
 d1.penup()
 d1.goto(-320,200)
 d1.pendown()
 for i in range(0,3):
  d1.fd(130)
  d1.right(120)

def Star():
 d1.penup()
 d1.goto(280,200)
 d1.pendown()
 for i in range(0,5):
  d1.right(144)
  d1.fd(230)

def Square():
 d1.penup()
 d1.goto(-200,-20)
 d1.pendown()
 for i in range(0,4):
  d1.fd(180)
  d1.right(90)

def Circle():
 d1.penup()
 d1.goto(250,-200)
 d1.pendown()
 d1.circle(50)

d1.speed(7)
Triangle()
Star()
Square()
Circle()
d1.penup()
d1.goto(0,0)
d1.color("Lightblue")

t1=turtle.Turtle()
t1.shape("turtle")
t1.color("Blue")
def Goone():
 t1.penup()
 t1.goto(-250,170)

Goone()


raw_input("201611069")
wn.exitinclick()