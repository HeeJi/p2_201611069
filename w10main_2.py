marks=list()
marks=[['English',100],['Math',200],['English',200],['Math',200],['English',100],['Math',300]]
engsum=0
for i in marks:
 if i[0].upper()=='ENGLISH':
  engsum=engsum+i[1]
englishsum=float(engsum)

masum=0
for i in marks:
 if i[0].upper()=='MATH':
  masum=masum+i[1]
mathsum=float(masum)

def EngAver():
 eng=0
 for i in marks:
  if i[0].upper()=='ENGLISH':
   eng=eng+1
 english=float(eng)
 engaver=englishsum/english
 print engaver
 

def MaAver():
 ma=0
 for i in marks:
  if i[0].upper()=='MATH':
   ma=ma+1
 math=float(ma)
 maaver=mathsum/math
 print maaver

def lab10():
 print englishsum
 print mathsum
 EngAver()
 MaAver()

def main():
 lab10()

main()
raw_input('201611069_order:english sum_math sum_english average_math average')