class Student:
    amount_of_students = 0

    def __init__(self, height=160, name=None):
        self.height = height
        self.name = name
        Student.amount_of_students += 1

    def __bool__(self):
        return self.name is not None

    def grow(self, height=1):
        self.height += height

    def __del__(self):
        print(f"{self.name} bye bye!!")

    def showStudentInfo(self):
        print(f"Hi I am {self.name}. height = {self.height}")

unknown = Student(name="unknown")
print(bool(unknown))
del unknown

nick = Student(name='Nick')
kate = Student(height=170, name='Kate')

print(nick.height)
print(kate.height)
print(kate.name)

nick.grow(height=6)
print(nick.height)

print(nick.amount_of_students)
print(Student.amount_of_students)