from actions import (
    load_students,
    import_students,
    add_students,
    see_all_students,
    get_top_3_students,
    get_class_average,
    export_students
)

def run_menu():
    while True: 
        print("---STUDENT GRADING SYSTEM---")
        print("1. Load existing students")
        print("2. Import students from CSV")
        print("3. Add new students")
        print("4. See all student data")
        print("5. See top 3 averages")
        print("6. See class average")
        print("7. Export data to CSV")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            students = load_students()
            print (f"{len(students)} students loaded")
            print({f"{students}"})
        elif choice == "2":
            path = input("Enter the path of the file to import: ").strip()
            imported_students = import_students(path)
            print(f"Imported {len(imported_students)} students from {path}")
        elif choice == "3":
            added_students = add_students()
            print(f"{len(added_students)} have been added.")
        elif choice == "4":
            students = see_all_students()
            if not students:
                print ("No students data found")
            else:
                print ("All your student data: ")
                for s in students:
                    print(
                        f"{s["Name"]} - {s["Section"]} | " 
                        f"Spanish: {s["Spanish"]}, English: {s["English"]}, Science: {s["Science"]}, Social Studies: {s["Social Studies"]}"
                        f"Average: {s["Average"]}"
                    )
        elif choice == "5":
            top_students = get_top_3_students()
            if not top_students:
                print ("There are no students available")
            else: 
                print ("Your top 3 students by average: ")
                for i, s in enumerate(top_students, start = 1):
                    print(f"{1}: {s["Name"]} - {s["Section"]} :: Average: {s["Average"]}")
        elif choice == "6":
            average = get_class_average()
            print (f"The class average is of {average}")
            
        elif choice == "7":
            success = export_students()
            if success:
                print("All student data has been successfully exported to students_db.csv.")
            else:
                print("No data to export.")
