class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def m1(self):
        if self.x == 0 or self.y == 0:
            return 0
        else:
            return 1
        
    def m2(self, a, b):
        self.a = a
        self.b = b
        if self.x >= 0 and self.y >= 0:
            wynik = 1
        elif self.x <= 0 and self.y >= 0:
            wynik = 2
        elif self.x <= 0 and self.y <= 0:
            wynik = 3
        elif self.x >= 0 and self.y <= 0:
            wynik = 4

        if self.a >= 0 and self.b >= 0:
            wynik2 = 1
        elif self.a <= 0 and self.b >= 0:
            wynik2 = 2
        elif self.a <= 0 and self.b <= 0:
            wynik2 = 3
        elif self.a >= 0 and self.b <= 0:
            wynik2 = 4

        if wynik == wynik2:
            return True
        else:
            return False
        
    def m3(self, a, b):
        self.a = a
        self.b = b
        import math

        dystans = math.sqrt((self.a - self.x) ** 2 + (self.b - self.y) ** 2)

        if dystans > 5:
            return True
        else:
            return False
        

p = C(2,3)
print(p.m1()) #returns 1
print(p.m2(7,4)) #returns True
print(p.m2(-3,1)) #returns False
print(p.m3(8,5)) #returns True
print(p.m3(4,7)) #returns False
p1 = C(0,5)
print(p1.m1()) #returns 0
print(p1.m2(4,7)) #returns False
print(p1.m2(-7,0)) #returns True


