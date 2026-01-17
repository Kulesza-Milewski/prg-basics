class C:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        
    def __str__(self):
        # Tworzymy bazowy ciąg: pierwsza litera imienia + pierwsza nazwiska + wiek
        base = self.first[0] + self.last[0] + str(self.age)
        
        if self.age < 18:
            return base.lower()
        else:
            return base.upper()