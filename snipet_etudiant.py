class StudentReport:
    def __init__(self, student_name, math_grade, literature_grade, science_grade):
        self.student_name = student_name
        self.math_grade = math_grade
        self.literature_grade = literature_grade
        self.science_grade = science_grade

    def generate_report(self):
        average_grade = (self.math_grade + self.literature_grade + self.science_grade) / 3
        print(f"Student: {self.student_name}")
        print(f"Math Grade: {self.math_grade}")
        print(f"Literature Grade: {self.literature_grade}")
        print(f"Science Grade: {self.science_grade}")
        print(f"Average Grade: {average_grade}")


# Exemple d'utilisation de la classe
student1 = StudentReport("John Doe", 90, 85, 95)
student1.generate_report()


class Student:
    def __init__(self, name, math_grade, literature_grade, science_grade):
        self.name = name
        self.math_grade = math_grade
        self.literature_grade = literature_grade
        self.science_grade = science_grade

    def average_grade(self):
        return (self.math_grade + self.literature_grade + self.science_grade) / 3


class ReportGenerator:
    def generate_report(self, student):
        print(f"Student: {student.name}")
        print(f"Math Grade: {student.math_grade}")
        print(f"Literature Grade: {student.literature_grade}")
        print(f"Science Grade: {student.science_grade}")
        print(f"Average Grade: {student.average_grade()}")


# Exemple d'utilisation des classes refactorées
student2 = Student("Jane Doe", 80, 75, 85)
report_generator = ReportGenerator()
report_generator.generate_report(student2)

* Créer la classe report
* Copier e

