class Student:
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept


student1 = Student("Yeswanth", 21, "IT")
student2 = Student("Hari", 21, "CS")
student3 = Student("vk", 21, "MEch")


stuList = [student1,student2,student3]

for student in stuList:
    print(student.name)