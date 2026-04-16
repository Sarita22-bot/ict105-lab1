courses = [
    [1, "Intro to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures", "Computer Science", "Intro to Programming"]
]

course_id = int(input("Enter course ID: "))

found = False

for c in courses:
    if c[0] == course_id:
        print("Course Name:", c[1])
        print("Department:", c[2])
        print("Prerequisite:", c[3])
        found = True
        break

if not found:
    print("Course not found")