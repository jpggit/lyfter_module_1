import csv

CSV_FILE = "students_db.csv"
FIELDS = ["Name", "Section", "Spanish", "English", "Social Studies", "Science", "Average"]

# MAIN
def load_csv(): #Load the main CSV (students_db.csv) and return a list of dicts.
    return _read_csv_file(CSV_FILE)

def read_external_csv(path): #Load any external CSV and return a list of dicts.
    return _read_csv_file(path)

def save_csv(data): #Save a list of dicts to the main CSV file.
    with open(CSV_FILE, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(data)

# INTERNAL
def _read_csv_file(path):
    students = []
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key in row:
                if key in ["Spanish", "English", "Social Studies", "Science", "Average"]:
                    try:
                        row[key] = float(row[key])
                    except ValueError:
                        row[key] = 0.0
            students.append(row)
    return students