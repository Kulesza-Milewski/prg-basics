import math

class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):

        if self.x == 0 or self.y == 0:
            return 0
        elif self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        
    def m2(self, a, b):
        nowy_obiekt = C(a, b)
        if self.m1() == nowy_obiekt.m1():
            return True
        else:
            return False
        
    def m3(self, a, b):
        wynik = math.sqrt((self.x - a) ** 2 + (self.y - b) ** 2)

        if wynik > 5:
            return True
        else:
            return False