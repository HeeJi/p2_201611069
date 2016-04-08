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

HighLow()
raw_input("w6main homework_highlow game_p2_201611069")