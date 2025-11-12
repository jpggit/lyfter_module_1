# 5. Dada `n` cantidad de notas de un estudiante, calcular:
#    1. Cuantas notas tiene aprobadas (mayor a 70).
#    2. Cuantas notas tiene desaprobadas (menor a 70).
#    3. El promedio de todas.
#    4. El promedio de las aprobadas.
#    5. El promedio de las desaprobadas.

grades = []
passed = []
failed = []
entry = ""


#RCollect data into a list
while entry != 'end': 
    entry = input("Enter a grade (or write 'end' to finish): ") 
    if entry != 'end':
        grades.append(int(entry)) #convert to int to avoid issues later


#Divide into lists of pass / fail
for grade in grades:
    if grade < 70:
        failed.append(grade)
    else:
        passed.append(grade)

#count pass / fail
def grades_count(list):
    return len(list)

passed_count = grades_count(passed)
failed_count = grades_count(failed)

#get averages
def avg(list):
    if list:
        return (sum(list) / len(list))
    else: return "0"

passed_avg = avg(passed)
failed_avg = avg(failed)
total_avg = avg(grades)


#Results
print(f'You passed {passed_count} ({passed}) and failed {failed_count} ({failed}).')
print(f'The average of your passed grades is of {passed_avg}.')
print(f'The average of your failed grades is of {failed_avg}.')
print(f'The total average is {total_avg}.')