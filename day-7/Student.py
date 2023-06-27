class Student:
    raise_grade = 1.1

    def __init__(self,name,rollNo,grade):
        self.name = name
        self.rollNo = rollNo
        self.grade = grade

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.name,self.rollNo)

    @property
    def applyRaise(self):
        self.grade = int(self.grade * self.raise_grade)
