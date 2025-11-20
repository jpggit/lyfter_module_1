import csv

CSV_FILE = "students_db.csv"
FIELDS = ["Name", "Section", "Spanish", "English", "Social Studies", "Science", "Average"]

#-------MAIN--------#
def load_csv(): #Load the existing CSV
    return _read_csv_file(CSV_FILE)

def read_external_csv(path): #Load an external CSV
    return _read_csv_file(path)

def save_csv(data):
    with open(CSV_FILE, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(data)

#------INTERNAL------#
#Function to read the CSV
def _read_csv_file(path):
    students = [] #Store students locally
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key in row:
                if key in ["Spanish", "English", "Social Studies", "Science", "Average"]:
                    try:
                        row[key] = float(row[key]) #convert each row[key] to a float
                    except (ValueError):
                        row[key]=0.0 #if it's not a number, convert to 0.0
            students.append(row)
    return students