allData=list()
allData=[['Coffee','Water','Milk','Icecream'],['Espresso','No','No','No'],['Long Black','Yes','No','No'],["Flat White","No","Yes","No"],["Cappuccino","No","Yes - Frothy","No"],["Affogato","No","No","Yes"]]
Data=allData[1:]
def Coffee():
 for i in Data:
  print i[0]

def how_many_MilkCoffee():
 none=0
 for i in Data:
  if i[2]=='No':
   none=none+1
  often=len(Data)-none
 print often

def MilkCoffee():
 for i in Data:
  if i[2]!='No':
   print i[0]

def lab10():
 Coffee()
 how_many_MilkCoffee()
 MilkCoffee()

def main():
 lab10()

main()
raw_input('20161106_w10main')