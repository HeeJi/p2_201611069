import os
mydir=os.getcwd()
def Combination():
 try:
  file1=open('python.txt','a')
  file2=open('number.txt','r')
  for line in file2:
   file1.write(line)
  file1.close()
  file2.close()
 except Exception as e:
  print e

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def getCoordsFromFile():
 frec=open('recoords.txt')
 mycoords=[]
 for line in frec:
  line1=line.split(',')
  mycoords.append([(line1[0],line1[1]),(line1[2],line1[3].strip())])
  for coord in mycoords:
   x1=int(coord[0][0])
   x2=int(coord[1][0])
   y1=int(coord[0][1])
   y2=int(coord[1][1])
  coordline=((x1,y1),(x2,y1),(x2,y2),(x1,y2),(x1,y1))
  t1.penup()
  t1.setpos(coordline[0])
  t1.pendown()
  for a in coordline:
   t1.goto(a)
 frec.close()

def lab13():
 Combination()
 getCoordsFromFile()

def main():
 lab13()
 wn.exitonclick()
 raw_input('w13 homework')

if __name__=="__main__":
 main()