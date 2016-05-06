people=list()
people=[[74425,76326],[61164,61636],[109688,115744],[144796,146776],[174996,181676],[177841,177434],[204630,205980],[223373,232245],[161055,166130],[171576,176735],[279169,293772],[239450,251066],[148690,156510],[182977,196992],[237792,242641],[283869,296762],[209344,210282],[118965,114441],[186503,186856],[195734,203014],[254381,249472],[212401,229111],[271654,295354],[319197,335045],[229829,231671]]
def man():
 mansum=0
 for i in range(0,len(people)):
  mansum=mansum+people[i][0]
 print mansum

def woman():
 womansum=0
 for i in range(0,len(people)):
  womansum=womansum+people[i][1]
 print womansum

def averman():
 mansum=0
 for i in range(0,len(people)):
  mansum=mansum+people[i][0]
 aver=mansum/len(people)
 print aver

def averwoman():
 womansum=0
 for i in range(0,len(people)):
  womansum=womansum+people[i][1]
 aver=womansum/len(people)
 print aver

def charGupeople():
 p=dict()
 for d in range(0,len(people)):
  p[d]=people[d][0]+people[d][1]
 print p
 import matplotlib.pyplot as plt
 plt.bar(range(len(p)), p.values(), align='center')
 plt.xticks(range(len(p)), list(p.keys()))
 plt.show()

def lab9():
 man()
 woman()
 averman()
 averwoman()
 charGupeople()

def main():
 lab9()

main()
if _name_=="_main_":
 main()
