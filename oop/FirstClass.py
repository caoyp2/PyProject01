class Student:
    #初始化类的属性
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def printMessage(self):
        print(self.name,self.score)

    def get_grade(self):
        if self.score >= 90:
            return  "A"
        elif self.score >= 80:
            return "B"
        else:
            return "C"

student = Student("lisi",66)
print(student.name)
print(student.score)
print(student.printMessage())
print(student.get_grade())





