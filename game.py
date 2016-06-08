import turtle
wn=turtle.Screen()
d1=turtle.Turtle()
wn.bgcolor("Lightblue")
oldheading=d1.heading()
t1=turtle.Turtle()
t1.shape("turtle")
t1.color("Blue")
def Start():
 raw_input('input anything you want: ')
 print 'GO!!!!'

def Triangle():
 d1.penup()
 d1.goto(-320,200)
 d1.pendown()
 for i in range(0,3):
  d1.fd(130)
  d1.right(120)
 d1.setheading(oldheading)

def Star():
 d1.penup()
 d1.goto(280,200)
 d1.pendown()
 for i in range(0,5):
  d1.right(144)
  d1.fd(230)
 d1.setheading(oldheading)

def Square():
 d1.penup()
 d1.goto(-200,-20)
 d1.pendown()
 for i in range(0,4):
  d1.fd(180)
  d1.right(90)
 d1.setheading(oldheading)

def Circle():
 d1.penup()
 d1.goto(250,-200)
 d1.pendown()
 d1.circle(50)

import random
d2=turtle.Turtle() 
d2.color('Yellow')
a=random.randrange(-340,340)
b=random.randrange(-340,340)
c=random.randrange(-340,340)
d=random.randrange(-340,340)
e=random.randrange(-340,340)
f=random.randrange(-340,340)
g=random.randrange(-340,340)
h=random.randrange(-340,340)
i=random.randrange(-340,340)
j=random.randrange(-340,340)
k=random.randrange(-340,340)
l=random.randrange(-340,340)
m=random.randrange(-340,340)
n=random.randrange(-340,340)
o=random.randrange(-340,340)
p=random.randrange(-340,340)
q=random.randrange(-340,340)
r=random.randrange(-340,340)
s=random.randrange(-340,340)
t=random.randrange(-340,340)
u=random.randrange(-340,340)
v=random.randrange(-340,340)
w=random.randrange(-340,340)
x=random.randrange(-340,340)
def power():
 myfile=open('tracks.txt','w')
 tracks=dict()
 tracks=({1:(a,b),2:(c,d),3:(e,f),4:(g,h),5:(i,j),6:(k,l),7:(m,n),8:(o,p),9:(q,r),10:(s,t),11:(u,v),12:(w,x)})
 myfile.close()
 print 'p means power!'
 for po in range(1,9):
  d2.penup()
  d2.setpos(tracks[po])
  d2.pendown()
  d2.circle(20)
  d2.left(90)
  d2.penup()
  d2.fd(10)
  d2.pendown()
  d2.fd(20)
  d2.right(90)
  d2.fd(10)
  d2.right(90)
  d2.fd(10)
  d2.right(90)
  d2.fd(10)
  d2.setheading(oldheading)
 d2.penup()
 d2.home()
 d2.color("Red")
 print 'go to get powers!! red circle means that you get it!!!'
 print 'whenever you change power red, press key r'

d1.speed(7) 
d2.speed(10)
import math
count=0
def reding():
 (wi,chi)=t1.pos()
 dis_1=0
 dis_1=math.sqrt(math.pow((wi-a),2)+math.pow((chi-(b+20)),2))
 dis_2=0
 dis_2=math.sqrt(math.pow((wi-c),2)+math.pow((chi-(d+20)),2))
 dis_3=0
 dis_3=math.sqrt(math.pow((wi-e),2)+math.pow((chi-(f+20)),2))
 dis_4=0
 dis_4=math.sqrt(math.pow((wi-g),2)+math.pow((chi-(h+20)),2))
 dis_5=0
 dis_5=math.sqrt(math.pow((wi-i),2)+math.pow((chi-(j+20)),2))
 dis_6=0
 dis_6=math.sqrt(math.pow((wi-k),2)+math.pow((chi-(l+20)),2))
 dis_7=0
 dis_7=math.sqrt(math.pow((wi-m),2)+math.pow((chi-(n+20)),2))
 dis_8=0
 dis_8=math.sqrt(math.pow((wi-o),2)+math.pow((chi-(p+20)),2))
 global count
 if dis_1<=20:
  print 'you get the first power!'
  d2.penup()
  d2.goto(a,b)
  d2.pendown()
  d2.setheading(oldheading)
  d2.circle(20)
  count=count+1
 elif dis_2<=20:
  print 'you get the second power!'
  d2.penup()
  d2.goto(c,d)
  d2.setheading(oldheading)
  d2.pendown()
  d2.circle(20)
  count=count+1
 elif dis_3<=20:
  print 'you get the third power!'
  d2.penup()
  d2.goto(e,f)
  d2.setheading(oldheading)
  d2.pendown()
  d2.circle(20)
  count=count+1
 elif dis_4<=20:
  print 'you get the fourth power!'
  d2.penup()
  d2.goto(g,h)
  d2.setheading(oldheading)
  d2.pendown()
  d2.circle(20)
  count=count+1
 elif dis_5<=20:
  print 'you get the fifth power!'
  d2.penup()
  d2.goto(i,j)
  d2.setheading(oldheading)
  d2.pendown()
  d2.circle(20)
  count=count+1
 elif dis_6<=20:
  print 'you get the sixth power!'
  d2.penup()
  d2.goto(k,l)
  d2.setheading(oldheading)
  d2.pendown()
  d2.circle(20)
  count=count+1
 elif dis_7<=20:
  print 'you get the seventh power!'
  d2.penup()
  d2.goto(m,n)
  d2.setheading(oldheading)
  d2.pendown()
  d2.circle(20)
  count=count+1
 elif dis_8<=20:
  print 'you get the eight power!'
  d2.penup()
  d2.goto(o,p)
  d2.setheading(oldheading)
  d2.pendown()
  d2.circle(20)
  count=count+1
 else:
  print 'cheer up!'
 return count

def Drawing():
 if count==1:   
  d1.setheading(oldheading)
  Circle()
 elif count==2:
  d1.setheading(oldheading)
  Triangle()
 elif count==3: 
  d1.setheading(oldheading)
  Square()
 elif count==4:
  d1.setheading(oldheading)
  Star()
 elif count==5:
  d1.setheading(oldheading)
  d1.color('Purple')
  Circle()
 elif count==6:
  d1.setheading(oldheading)
  d1.color('Purple')
  Triangle()
 elif count==7:
  d1.setheading(oldheading)
  d1.color('Purple')
  Square()
 elif count==8:
  d1.setheading(oldheading)
  d1.color('Purple')
  Star()
  name=raw_input('your name: ')
  print 'Good job', name
  print 'press q to quit'
 else:
  print 'game over! you lose..'

def pressR():
 Drawing()

def pressUp():
 t1.fd(25)
 reding()

def pressDown():
 t1.backward(25)
 reding()

def pressRight():
 t1.right(15)

def pressLeft():
 t1.left(15)

def pressQ():
 wn.bye()

def mousegoto(x,y):
 t1.setpos(x,y)
 reding()
 t1.setheading(oldheading)

def addKeys():
 wn.onkey(pressUp,'Up')
 wn.onkey(pressDown,'Down')
 wn.onkey(pressRight,'Right')
 wn.onkey(pressLeft,'Left')
 wn.onkey(pressR,'r')
 wn.onkey(pressQ,'q')

def addMouse():
 wn.onclick(mousegoto)

Start()
power()
wn.listen()
addKeys()
addMouse()

turtle.mainloop()