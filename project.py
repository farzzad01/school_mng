# manage a school

class Person:
    def __init__(self,fname,lname,bdate,natcode):
        self.fname=fname
        self.lname = lname
        self.bdate= bdate
        self.natcode = natcode
    def full_name(self,fname,lname):
        return f'name is : {fname} lname is {lname}'
    def show_brithday(self,bdate):
        return f'brith date is {bdate}'
    def show_natcode(self,natcode):
        return f'national code is {natcode}'

class Student(Person):
    def __init__(self, major):
        self.major = major
    def show_major(self,major):
        return f'major is {major}'

class Teacher(Person):
    def __init__(self, teacher_code,hire_t):
        self.teacher_code = teacher_code
        self.hire = hire
    def show_teach_code(self,teacher_code):
        return f'teacher code is {teacher_code}'

    def show_hire_time(self,hire_t):
        return f'hire time is {hire_t}'




######################################## sudo code
class School:
    def __init__(self, name, students, teachers):
        self.name = name
        self.students = students
        self.teachers = teachers

    def get_student_names(self):
        return [s.name for s in self.students]

    def get_teacher_names(self):
        return [t.name for t in self.teachers]

students = [Student("Alice", "9th"), Student("Bob", "10th")]
teachers = [Teacher("Charlie", "Math"), Teacher("Dave", "Science")]
school = School("My School", students, teachers)

print("Student names:", school.get_student_names())
print("Teacher names:", school.get_teacher_names())
