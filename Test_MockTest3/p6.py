class C:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        if self.age < 18:
            return (self.fname[0] + self.lname[0]).lower() + str(self.age)
        else:
            return (self.fname[0] + self.lname[0]).upper() + str(self.age)

print(C("John","May",21))