from actions import (
    load_students,
    import_students,
    add_students,
    see_all_students,
    get_top_3_students,
    get_class_average,
    export_students,
)

def run_menu():
    students = []

    while True:
        print("---STUDENT GRADING SYSTEM---")
        print("1. Load existing students from main CSV")
        print("2. Import students from another CSV")
        print("3. Add new students")
        print("4. See all student data")
        print("5. See top 3 averages")
        print("6. See class average")
        print("7. Export data to CSV")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            students = load_students()
            print(f"{len(students)} students loaded into memory.")

        elif choice == "2":
            path = input("Enter the path of the file to import: ").strip()
            students, imported_students = import_students(students, path)
            print(f"Imported {len(imported_students)} students from {path}")

        elif choice == "3":
            students, added_students = add_students(students)
            print(f"{len(added_students)} student(s) have been added.")

        elif choice == "4":
            see_all_students(students)

        elif choice == "5":
            top_students = get_top_3_students(students)
            if not top_students:
                print("There are no students available.")
            else:
                print("Your top 3 students by average:")
                for i, s in enumerate(top_students, start=1):
                    print(f"{i}: {s.name} - {s.section} :: Average: {s.average}")

        elif choice == "6":
            average = get_class_average(students)
            if average is None:
                print("No students to claculate class average.")
            else:
                print(f"The class avg is {average}")

        elif choice == "7":
            success = export_students(students)
            if success:
                print("All student data has been successfully exported to students_db.csv.")

        elif choice == "8":
            print("Exiting the Student Grading System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")