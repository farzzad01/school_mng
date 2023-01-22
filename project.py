class School:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.classes = {}
        
    def add_class(self, class_name, class_code):
        self.classes[class_code] = Class(class_name, class_code)
        
    def get_class(self, class_code):
        return self.classes[class_code]
    
    def show_all_info(self):
        print("School Name: ", self.name)
        print("School Code: ", self.code)
        print("Classes: ")
        for class_code in self.classes:
            class_info = self.classes[class_code]
            print("   Class Name: ", class_info.name)
            print("   Class Code: ", class_info.code)
            print("   Students: ")
            for student in class_info.students:
                print("      Name: ", student.name)
                print("      Birthdate: ", student.birthdate)
                print("      ID: ", student.id)
                print("      Major: ", student.major)
            print("   Teachers: ")
            for teacher in class_info.teachers:
                print("      Name: ", teacher.name)
                print("      ID: ", teacher.id)
                print("      Birthdate: ", teacher.birthdate)
                print("      Teacher Code: ", teacher.teacher_code)
                print("      Hire Date: ", teacher.hire_date)

class Class:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []
        self.teachers = []
        
    def add_student(self, name, birthdate, id, major):
        self.students.append(Student(name, birthdate, id, major))
        
    def add_teacher(self, name, id, birthdate, teacher_code, hire_date):
        self.teachers.append(Teacher(name, id, birthdate, teacher_code, hire_date))

class Student:
    def __init__(self, name, birthdate, id, major):
        self.name = name
        self.birthdate = birthdate
        self.id = id
        self.major = major

class Teacher:
    def __init__(self, name, id, birthdate, teacher_code, hire_date):
        self.name = name
        self.id = id
        self.birthdate = birthdate
        self.teacher_code = teacher_code
        self.hire_date = hire_date
        
# Create an instance of School
high_school = School("Example High School", "EHS123")

# Get number of classes from user
num_classes = int(input("Enter the number of classes in the high school: "))

# Get information for each class
for i in range(num_classes):
    class_name = input("Enter the name of class: ")
    class_code = input("Enter the code of class: ")
    high_school.add_class(class_name, class_code)
    
