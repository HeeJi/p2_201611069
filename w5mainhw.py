def main():
 p1=raw_input("p1 choose rsp: ")
 p2=raw_input("p2 choose rsp: ")
 def tool(p):
  if(p=='r'):
   return 5.0
  elif(p=='s'):
   return 10.0
  elif(p=='p'):
   return 20.0
  else:
    print "input error"
  hj=tool(p1)/tool(p2)
  if(hj==1.0):
   print "draw"
  elif(hj==0.5)1:
   print "p1 win"
  elif(hj=0.25):
   print "p2 win"
  elif(hj==2.0):
   print "p2 win"
  elif(hj==4.0):
   print "p1 win"
  else:
   print "input error"

main()
sel=raw_input("HI")
wn.exitonclick()