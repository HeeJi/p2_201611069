class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print 'my dog name is ',self.name
    def talk(self):
        print 'normal dogs say : mung mung'

class ShihTzuDog(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print 'ShihTzu says : si si'

class Maltese(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print 'Maltese says : mal mal'

def DogsSay():
    mydog=Dog('dogs')
    mydog.talk()
    myshihtzu=ShihTzuDog('ShihTzu')
    myshihtzu.talk()
    mymaltese=Maltese('Maltese')
    mymaltese.talk()

def lab14():
    DogsSay()

def main():
    lab14()

if __name__=="__main__":
 main()

raw_input('201611069_w14 homework')