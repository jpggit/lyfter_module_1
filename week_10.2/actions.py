from data import load_csv, read_external_csv, save_csv

students = []
#-----------------------------
# LOAD EXISTING STUDENTS
#-----------------------------
def load_students():
    global students
    students = load_csv()
    return students


#-----------------------------
# IMPORT NEW CSV DATA
#-----------------------------
def import_students(path):
    global students
    new_students = read_external_csv(path)
    students.extend(new_students)
    save_csv(students)
    return new_students


#-----------------------------
# ADD MANY STUDENTS
#-----------------------------
def add_students():
    global students

    # Load existing students first
    existing_students = read_external_csv("students_db.csv")

    # Work on a copy
    students = existing_students.copy()

    new_students = []  # store the new entries

    while True:
        student = create_student()
        students.append(student)
        new_students.append(student)
        again = input("Add another student? (y/n): ").strip().lower()
        if again != "y":
            break

    # Save updated list (existing + new)
    save_csv(students)

    print(f"{len(new_students)} new student(s) added and saved successfully.")
    return new_students

#-----------------------------
# CREATE ONE STUDENT
#-----------------------------
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

#-----------------------------
# Supporting functions for creating a student
#-----------------------------
#Get a valid name
def get_full_name():
    while True:
        name = input("Enter student full name (first and last): ").strip()
        parts = name.split()
        if len(parts) >= 2:
            return name
        else:
            print("Please enter a full name (e.g., John Smith).")

#Get a valid grade
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

#-----------------------------
# Function to average grades 
#-----------------------------
def grade_average(grades):
    if not grades:
        return 0
    return round(sum(grades.values()) / len(grades), 2)

#-----------------------------
# Function return all students from the main db
#-----------------------------
def see_all_students():
    students = read_external_csv("students_db.csv")
    return students

#-----------------------------
# Function return top 3 students
#-----------------------------
def get_top_3_students():
    students = read_external_csv("students_db.csv")
    if not students: 
        return None
    sorted_students = sorted(students, key=lambda s: s["Average"], reverse = True)
    return sorted_students[:3]

#-----------------------------
# Function see the class average
#-----------------------------
def get_class_average():
    students = read_external_csv("students_db.csv")
    if not students:
        return None
    averages = [s["Average"] for s in students]
    class_average = round(sum(averages) / len(averages), 2)
    return class_average

#-----------------------------
# Function to export students to the main CSV
#-----------------------------
def export_students():
    global students

    if not students:
        students = read_external_csv("students_db.csv") #load them first
    
    if not students:
        print ("No students data available to export.")
    
    save_csv(students)
    return True