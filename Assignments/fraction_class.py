def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

class fraction(object):

    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d
        self.whole = 0
        self.reduce()

    def __str__(self):
        return "%s / %s" % (self.numerator,self.denominator)

    def reduce(self):
        thegcd = gcd(self.numerator,self.denominator)
        self.numerator /= thegcd
        self.denominator /= thegcd

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)

    def __add__(self,rhs):
        x = (self.numerator * rhs.denominator) + (rhs.numerator * self.denominator)
        y = self.denominator * rhs.denominator
        while(x>y):
            x-=y
            self.whole += 1
        if(self.whole>0):
            return " %s %s/%s" % (self.whole, int(x), int(y))
        if(x == y):
            return 1
        else:
            return "%s/%s" % (int(x), int(y))



if __name__ == '__main__':
    a = fraction(1,2)
    b = fraction(4,5)
    c = a + b
    print(c)