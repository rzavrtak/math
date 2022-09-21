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

a = ggT(int(sys.argv[1]), int(sys.argv[2]))
a.PrintggT()
