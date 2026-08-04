print("STUDENT MANAGEMENT SYSTEM")
print()
students = []

for j in range(2):   
    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))

    subjects = {}   

    for i in range(3):  
        subject = input("Enter student subjects: ")
        marks = int(input("Enter student marks: "))
        subjects[subject] = marks

    student = {    
        "name": name,
        "roll_no": roll_no,
        "subjects": subjects
    }

    students.append(student)  
for student in students:
    print("Name:", student["name"])
    print("Roll No:", student["roll_no"])

    for subject, marks in student["subjects"].items():
        print(subject, ":", marks)

    print() 

print("SEARCH STUDENT:") 

search_name = input("Enter student name : ")
found = False
for student in students:
    if search_name == student["name"]:
        print("name of the student", student["name"])
        print("roll no :", student["roll_no"])
        for subject, marks in student["subjects"].items():
            print(subject, ":", marks)
        found = True
        break
if not found:
    print("student not found")

print("STUDENT'S PERCENTAGE:")

for student in students:
    total_marks = sum(student["subjects"].values())
    total_percentage = (total_marks/200)*100
    print("name:",student["name"])
    print ("roll no:",student["roll_no"])
    for subject, marks in student["subjects"].items():
            print(subject, ":", marks)
    print("percentage:",total_percentage)
    print()

print("CLASS TOPPER:")

cl_topper = None
highest_marks = 0
for student in students:
    total_marks = sum(student["subjects"].values())
    if total_marks > highest_marks:
        highest_marks = total_marks
        cl_topper = student

if cl_topper is not None:
    print("Class topper:")
    print("Name:", cl_topper["name"])
    print("Roll No:", cl_topper["roll_no"])
    print("Total Marks:", highest_marks)

search_name = input("Enter student name : ")
subject_name = input("Enter subject name to update: ")
new_marks = int(input("Enter new marks: "))
found = False
for student in students:
    if search_name == student["name"]:
        print("name of the student", student["name"])
        print("roll no :", student["roll_no"])
        student["subjects"][subject_name] = new_marks
        for subject, marks in student["subjects"].items():
            print(subject, ":",marks)
        found = True
        break
    print("marks updated!")
if not found:
    print("subject not found")

print("DELETE STUDENT:") 

search_name = input("Enter student name : ")
found = False
for student in students:
    if search_name == student["name"]:
        students.remove(student)
        found = True
        break
if not found:
    print("student not found")
print("DELETE STUDENT:") 
