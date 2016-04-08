def yunneun():
 year=raw_input("user input year: ")
 y1=int(year)
 if(y1%4==0) and (y1%100 !=0 or y1%400==0):
  print "o"
 else:
  print "x"

yunneun()
raw_input("201611069_w6main homework")
wn.exitonclick()