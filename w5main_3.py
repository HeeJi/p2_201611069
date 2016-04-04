def lab5(): 
 w1=raw_input("input your weight: ") 
 h1=raw_input("input your height: ") 
 weight=float(w1) 
 height=float(h1) 
 goheight=height/100. 
 BMI=weight/(goheight*goheight) 
 if(BMI<18.5): 
  print "low weight" 
 elif(18.5<=BMI<25): 
  print "normal" 
 elif(25<=BMI<30): 
  print "mild obesity" 
 elif(30<=BMI): 
  print "high obesity" 
 else: 
  print "Error" 

lab5()
raw_input('w5main_3 homework')