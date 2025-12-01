from data import (
    load_csv,
    save_csv,
    read_external_csv,
)

#--------------------------------------
# CLASS = STUDENT
#--------------------------------------
class Student:
    def __init__ (self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science
        self.average = self.calculate_average()
    
    def __str__(self):
        return f"{self.name}, Section {self.section} - Avg: {self.average}"

    def calculate_average(self):
        return round(
            (self.spanish+self.english+self.social+self.science)/4, 
            2
        )

    def student_to_dict (self):
        return {
            "Name": self.name,
            "Section": self.section,
            "Spanish": self.spanish,
            "English": self.english,
            "Social Studies": self.social,
            "Science": self.science,
            "Average": self.average,
        }

    @staticmethod #Added static method decorator because it doesn't take 'self' as the parameter
    def student_from_dict(row):
            return Student (
                name = row.get("Name"),
                section = row.get("Section"),
                spanish = row.get("Spanish"),
                english = row.get("English"),
                social = row.get("Social Studies"),
                science = row.get("Science"),
            )

#--------------------------------------
# LOAD STUDENTS
#--------------------------------------
def load_students():
    raw_students = load_csv()
    students = [Student.student_from_dict(row) for row in raw_students]
    return students


#--------------------------------------
# IMPORT STUDENTS
#--------------------------------------
def import_students(path):
    raw_students = read_external_csv(path)
    students = [Student.student_from_dict(row) for row in raw_students]
    return students


#--------------------------------------
# EXPORT STUDENTS
#--------------------------------------
def export_students(students):
    data = []
    for s in students:
        student_dict = s.student_to_dict()
        data.append(student_dict)

    save_csv(data)
    return True



#--------------------------------------
# SEE ALL 
#--------------------------------------
def see_all_students(students):
    if not students:
        print ("No students available.")
        return students # Important to return students such that the user can continue to add students... 

    print ("All your student data:")
    for s in students:
        print (f"Name: {s.name} | Section: {s.section}")
        print (f"Spanish: {s.spanish} :: English: {s.english} :: Social Studies: {s.social} :: Science: {s.science}.")
        print (f"Average Grade: {s.average}.")
        print ("---")

    return students


#--------------------------------------
# SEE TOP 3 STUDENTS
#--------------------------------------
def get_top_students(students):
    if not students:
        print ("There are no students yet.")

    else:
        top_students = sorted(students, key=lambda s: s.average,reverse=True)
        top_3_students = top_students[:3]
        return top_3_students


#--------------------------------------
# CLASS AVERAGE
#--------------------------------------
def get_class_average(students):
    if not students:
        print("There are no students yet.")
        return None

    averages = []
    for s in students:
        averages.append(s.average)
    return round(sum(averages)/len(averages), 2)


#--------------------------------------
# ADD STUDENTS FUNCTIONS START
#--------------------------------------
#--------------------------------------
# ADD MANY STUDENTS
#--------------------------------------
def add_students(students):
    new_students = []
    while True:
        student = _add_student()
        students.append(student)
        new_students.append(student)

        again = input("Add another student? y/n: ").strip().lower()
        if again != "y":
            break

    return students, new_students


#--------------------------------------
# ADD A SINGLE STUDENT
#--------------------------------------
def _add_student():
    name = _get_full_name()
    section = input("Enter the student section: ")
    spanish = _get_valid_grade("Spanish")
    english = _get_valid_grade("English")
    social = _get_valid_grade("Social Studies")
    science = _get_valid_grade("Science")

    return Student(name, section, spanish, english, social, science)


#--------------------------------------
# SUPPORTING FUNCTIONS
#--------------------------------------
def _get_full_name():
    full_name = input("Enter the full name of the student: ").strip()
    parts = full_name.split()
    if len(parts) >= 2:
        return full_name
    else:
        print("Please enter a full name (e.g., John Smith).")


def _get_valid_grade(subject):
    grade_input = input(f"Enter grade for {subject} (0-100): ").strip()
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
                return grade
        else: 
            print("Grade must be between 0-100.")
    except ValueError:
        print("Enter a valid number.")

#--------------------------------------
# ADD STUDENTS FUNCTIONS END
#--------------------------------------