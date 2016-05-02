def charCount(word):
 d=dict()
 for c in word:
  if c not in d:
   d[c]=1
  else:
   d[c]=d[c]+1
 print d
 import matplotlib.pyplot as plt
 plt.bar(range(len(d)), d.values(), align='center')
 plt.xticks(range(len(d)), list(d.keys()))
 plt.show()

def countDigitsLetters(word):
 d=dict()
 for c in word:
  if c not in d:
   d[c]=1
  else:
   d[c]=d[c]+1
 print d
 import matplotlib.pyplot as plt
 plt.bar(range(len(d)), d.values(), align='center')
 plt.xticks(range(len(d)), list(d.keys()))
 plt.show()

mine=set()
mine={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
friend=set()
friend={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}
def onlyMine():
 print mine.difference(friend)

def onlyFriend():
 print friend.difference(mine)

def both():
 print mine.intersection(friend)

def all():
 print mine.union(friend)

def Count():
 d=dict()
 for c in mine:
  if c not in d:
   d[c]=1
  else:
   d[c]=d[c]+1
 for c in friend:
  if c not in d:
   d[c]=1
  else:
   d[c]=d[c]+1
 print d

def lab9_1():
 word='sangmyung university'
 charCount(word)

def lab9_2():
 word='20,Hongjimun2-gil,Jongno-gu,Seoul,Korea'
 countDigitsLetters(word)

def lab9_3():
 onlyMine()
 onlyFriend()
 both()
 all()
 Count()

def main():
 lab9_1()
 lab9_2()
 lab9_3()

main()
raw_input('201611069_w9mainhw')