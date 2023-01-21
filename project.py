# manage a school
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

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
