class C:
    def __init__(self, base):
        self.base = base

    def __str__(self):
        return str(self.base)

    def m1(self):
        return self.base
    
    def m2(self):
        self.base += 1
    
    def m3(self):
        self.base -= 1
    
    def m4(self, n):
        self.base += n 
    
c = C(5)

c.m1()
c.m2()
c.m1()
c.m3()
c.m1()
c.m4(7)
c.m1()
c.__str__()
c.m1()