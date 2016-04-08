def yunneun():
 year=raw_input("user input year: ")
 y1=int(year)
 if(y1%4==0) and (y1%100 !=0 or y1%400==0):
  print "o"
 else:
  print "x"

def HighLow():
 import random
 a=input("range: ")
 r1=random.randrange(1,a+1)
 global n1
 print "GO!"
 def game():
  n1=input("choose number: ")
  if(r1>n1):
   result="HIgh"
   print result
   game()
  elif(r1<n1):
   result="Low"
   print result
   game()
  else:
   result="Correct"
   print result
 game()

def lab6():
 yunneun()
 HighLow()

def main():
 lab6()

main()
if _name_=="_main_":
 main()

raw_input("201611069_w6main homework")
wn.exitonclick()