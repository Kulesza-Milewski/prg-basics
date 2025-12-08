# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.index = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.index = 111111
    student2.name = "Olivia"
    student2.age = 21
    student2.index = 222222
    student3.name = "Alan"
    student3.age = 18
    student3.index = 333333
    

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student1.index} is the index')
    print(f'{student2.name}, {student2.age} years old, {student2.index} is the index')
    print(f'{student3.name}, {student3.age} years old, {student3.index} is the index')

if __name__ == "__main__":
    main()