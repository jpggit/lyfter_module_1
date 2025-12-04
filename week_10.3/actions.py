from data import load_csv, read_external_csv, save_csv

students = []

#-----------------------------
# NEW STUDENT CLASS
#-----------------------------
class Student:
    def __init__(self, name, section, spanish, english, social_studies, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science
        self.average = self.calculate_average()

    def calculate_average(self):
        return round(
            (self.spanish + self.english + self.social_studies + self.science) / 4,
            2
        )

    def to_dict(self): #Convert the Student object into a dict for CSV export.
        return {
            "Name": self.name,
            "Section": self.section,
            "Spanish": self.spanish,
            "English": self.english,
            "Social Studies": self.social_studies,
            "Science": self.science,
            "Average": self.average,
        }

    def from_dict(cls, row): #Create a Student object from a CSV row (dict).
        return cls(
            row["Name"],
            row["Section"],
            row["Spanish"],
            row["English"],
            row["Social Studies"],
            row["Science"],
        )
# -----------------------------
# LOAD EXISTING STUDENTS (from main CSV)
# -----------------------------
def load_students():
    raw_students = load_csv()  # list of dicts
    students = [Student.from_dict(row) for row in raw_students]
    return students

# -----------------------------
# IMPORT NEW CSV DATA (from path)
# -----------------------------
def import_students(students, path):
    raw_students = read_external_csv(path)  # list of dicts

    imported_students = []
    for row in raw_students:
        s = Student.from_dict(row)
        imported_students.append(s)

    updated = students + imported_students
    return updated, imported_students

# -----------------------------
# ADD MANY STUDENTS (from user input)
# -----------------------------
def add_students(students):
    new_students = []

    while True:
        student = create_student()
        students.append(student)
        new_students.append(student)

        again = input("Add another student? (y/n): ").strip().lower()
        if again != "y":
            break

    return students, new_students

# -----------------------------
# CREATE ONE STUDENT
# -----------------------------
def create_student():
    name = get_full_name()
    section = input("Enter class section: ").strip()

    spanish = get_valid_grade("Spanish")
    english = get_valid_grade("English")
    social_studies = get_valid_grade("Social Studies")
    science = get_valid_grade("Science")

    return Student(name, section, spanish, english, social_studies, science)

# -----------------------------
# Supporting functions for creating a student
# -----------------------------
def get_full_name():
    while True:
        name = input("Enter student full name (first and last): ").strip()
        parts = name.split()
        if len(parts) >= 2:
            return name
        else:
            print("Please enter a full name (e.g., John Smith).")

def get_valid_grade(subject):
    while True:
        grade_input = input(f"Enter the grade for {subject} (0-100): ").strip()
        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0-100. Try again.")
        except ValueError:
            print("Enter a valid number.")

# -----------------------------
# SEE ALL STUDENTS
# -----------------------------
def see_all_students(students):
    if not students:
        print("No students available.")
        return

    print("All your student data:")
    for s in students:
        print(
            f"{s.name} - {s.section} | "
            f"Spanish: {s.spanish}, English: {s.english}, "
            f"Science: {s.science}, Social Studies: {s.social_studies} | "
            f"Average: {s.average}"
        )

# -----------------------------
# TOP 3 STUDENTS
# -----------------------------
def get_top_3_students(students):
    if not students:
        return []

    sorted_students = sorted(students, key=lambda s: s.average, reverse=True)
    return sorted_students[:3]

# -----------------------------
# CLASS AVERAGE
# -----------------------------
def get_class_average(students):
    if not students:
        return None

    averages = [s.average for s in students]
    class_average = round(sum(averages) / len(averages), 2)
    return class_average

# -----------------------------
# EXPORT STUDENTS TO CSV
# -----------------------------
def export_students(students):
    if not students:
        print("No students data available to export.")
        return False

    dict_students = [s.to_dict() for s in students]
    save_csv(dict_students)
    print("Students exported to CSV.")
    return True