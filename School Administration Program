class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        total_grades = sum(self.grades.values())
        return total_grades / len(self.grades)

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        print("List of Students:")
        for student in self.students:
            print(f"Roll Number: {student.roll_number}, Name: {student.name}")

    def list_student_grades(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Grades for {student.name} (Roll Number: {student.roll_number}):")
                for subject, grade in student.grades.items():
                    print(f"{subject}: {grade}")
                print(f"Average Grade: {student.get_average_grade()}")
                return
        print(f"Student with Roll Number {roll_number} not found.")

def main():
    school_name = "Sample School"
    school = School(school_name)

    while True:
        print("\nSchool Administration Menu:")
        print("1. Add Student")
        print("2. List Students")
        print("3. Add Grade")
        print("4. List Student Grades")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            student = Student(roll_number, name)
            school.add_student(student)
            print(f"Student {name} (Roll Number: {roll_number}) added successfully.")

        elif choice == "2":
            school.list_students()

        elif choice == "3":
            roll_number = input("Enter Roll Number of Student: ")
            subject = input("Enter Subject: ")
            grade = float(input("Enter Grade: "))
            for student in school.students:
                if student.roll_number == roll_number:
                    student.add_grade(subject, grade)
                    print(f"Grade {grade} added for {student.name} in {subject}.")
                    break
            else:
                print(f"Student with Roll Number {roll_number} not found.")

        elif choice == "4":
            roll_number = input("Enter Roll Number of Student: ")
            school.list_student_grades(roll_number)

        elif choice == "5":
            print("Exiting School Administration Program.")
            break

if __name__ == "__main__":
    main()
