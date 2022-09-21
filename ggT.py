import sys

class ggT(object):
    def __init__(self, a, b):
        
        n, d = gt(self, a, b)
        r = rem(self, n, d)
        self.a = a
        self.b = b
        self.r = r

    def PrintggT(self):
        print (f"ggT({self.a}, {self.b}) = {self.r}")

def gt(self, a, b):
    if a > b:
    	return a, b
    else:
    	return b, a

def rem(self, n, d):
    r = int(n/d)
    while n%d > 0:
        r=n%d
        n=d
        d=r
    return r    

def usage():
  print(f"The script {sys.argv[0]} needs to be called with 2 integer numbers a and b.")
  print("example:")
  print(f">{sys.argv[0]} 256 16")
  print("ggT(256, 16) = 16")

def mymethod(argv):
 if(len(argv)<2):
  usage()
  sys.exit(2)
if __name__=='__main__':
        mymethod(sys.argv[1:])

a = ggT(int(sys.argv[1]), int(sys.argv[2]))
a.PrintggT()
