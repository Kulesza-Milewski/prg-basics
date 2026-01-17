class C:
    def __init__(self, sectors):
        # sectors to słownik np. {"A": 120, "D": 150}
        self.data = sectors
        
    def m1(self, s, n):
        # Przypisuje wartość n do sektora s (klucza słownika)
        self.data[s] = n
        
    def m2(self, s):
        # s to ciąg znaków, np "GD". Sumujemy wartości dla kluczy "G" i "D"
        total = 0
        for char in s:
            if char in self.data:
                total += self.data[char]
        return total