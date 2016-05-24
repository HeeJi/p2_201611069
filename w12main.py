import os  
mydir=os.getcwd() 
def firstfile(): 
 filename='python.txt' 
 myfilename=os.path.join(mydir,filename) 
 try: 
  myfile=open(myfilename, 'r') 
  contents=myfile.readlines()
  for line in myfile: 
   if line.find('Python')>=0: 
    print line 
  myfile.close() 
 except IOError as e: 
  print e

sfilename='output.txt'
smyfilename=os.path.join(mydir,sfilename)
def secondfile():
 smyfile=open('output.txt','w')
 line1='first line\n'
 smyfile.write(line1)
 line2='\second line\n'
 smyfile.write(line2)
 line3='third line'
 smyfile.write(line3)
 smyfile.close()
 tmyfile=open('output.txt','r')
 scontents=tmyfile.readlines()
 for i in range(0,len(scontents)):
  if scontents[i].find('line')>=0:
   print 'line'.upper()
 tmyfile.close()

def lab12():
 print 'w12main_1'
 firstfile()
 print 'w12main_2'
 secondfile()

def main():
 lab12()

if __name__=="__main__": 
 main() 
          


