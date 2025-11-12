from data import load_csv, read_external_csv, save_csv

# -----------------------------
# LOAD EXISTING STUDENTS FROM MAIN CSV
# -----------------------------
from data import load_csv

def load_students():
    return load_csv()

# -----------------------------
# IMPORT NEW CSV DATA
# -----------------------------
def import_students(students, path):
    new_students = read_external_csv(path)
    updated_students = students + new_students
    save_csv(updated_students)
    return updated_students, new_students

# -----------------------------
# ADD MANY STUDENTS
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
    grades = {
        "Spanish": get_valid_grade("Spanish"),
        "English": get_valid_grade("English"),
        "Social Studies": get_valid_grade("Social Studies"),
        "Science": get_valid_grade("Science")
    }

    return {
        "Name": name,
        "Section": section,
        **grades,
        "Average": grade_average(grades)
    }

# -----------------------------
# Helper functions
# -----------------------------
def get_full_name():
    while True:
        name = input("Enter student full name (first and last): ").strip()
        if len(name.split()) >= 2:
            return name
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

def grade_average(grades):
    if not grades:
        return 0
    return round(sum(grades.values()) / len(grades), 2)

# -----------------------------
# SEE STUDENTS
# -----------------------------
def see_all_students(students):
    if not students:
        print("No student data available.")
    else:
        print("All student data:")
        for s in students:
            print(
                f"{s['Name']} - {s['Section']} | "
                f"Spanish: {s['Spanish']}, English: {s['English']}, "
                f"Science: {s['Science']}, Social Studies: {s['Social Studies']} | "
                f"Average: {s['Average']}"
            )

# -----------------------------
# TOP 3 STUDENTS
# -----------------------------
def get_top_3_students(students):
    if not students:
        return []
    sorted_students = sorted(students, key=lambda s: s["Average"], reverse=True)
    return sorted_students[:3]

# -----------------------------
# CLASS AVERAGE
# -----------------------------
def get_class_average(students):
    if not students:
        return 0
    averages = [s["Average"] for s in students]
    return round(sum(averages) / len(averages), 2)

# -----------------------------
# EXPORT
# -----------------------------
def export_students(students):
    if not students:
        print("No student data available to export.")
        return False
    save_csv(students)
    return True