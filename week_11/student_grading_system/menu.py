from actions import (
    load_students,
    import_students,
    add_students,
    see_all_students,
    get_top_students,
    export_students,
    get_class_average,
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

        choice = input ("Enter your choice: ").strip()

        if choice == "1":
            students = load_students()
            print(f"{len(students)} students loaded into memory.")

        elif choice == "2":
            path = input ("Enter the path of the CSV file: ")
            students = import_students(path)
            print (f"{len(students)} students have been imported.")

        elif choice == "3":
            students, new_students = add_students()
            print (f"{len(new_students)} students have been added.")

        elif choice == "4":
            students = see_all_students(students)

        elif choice == "5":
            top_students = get_top_students(students)
            for s in top_students:
                print(s)

        elif choice == "6":
            average = get_class_average()
            print (f"Class average: {average}")

        elif choice == "7":
            success = export_students(students)
            if success:
                print("Export completed")

        elif choice == "8":
            print("Exiting the Student Grading System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
