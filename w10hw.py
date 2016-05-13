satis=list()
satis=[['Section','very satisfied','satisfied','normal','unsatisfied','very unsatisfied'],['education level', 13.1, 37.1, 39.6, 8.7, 1.5],['education system', 10.6, 34.6, 39.5, 13.4, 1.9],['friend associate', 27.1, 40.0, 28.5, 2.9, 1.5],['teacher associate', 16.2, 7.8, 38.4, 6.8, 0.8],['facility', 11.4, 29.8, 39.0, 14.8, 4.9],['environment around school(college)', 12.2, 26.5, 42.0, 14.9, 4.4],['major', 13.5, 29.7, 43.4, 11.1, 2.4],['overall', 13.7, 37.6, 43.4, 4.1, 1.2]]
s=satis[1:]
sum1=0
for i in s:
 sum1=sum1+i[1]+i[2]

def goodaver():
 print 'positive average: ', sum1/len(s)

sum2=0
for i in s:
 sum2=sum2+i[4]+i[5]

def badaver():
 print 'negative average: ', sum2/len(s)

def lab10():
 goodaver()
 badaver()

def main():
 lab10()

main()
raw_input('201611069_w10_homework')