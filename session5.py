# Student Course Enrollment Dictionary

course_enrollments = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101", "MATH102"],
    1003: ["CS202", "PHY101"],
    1004: ["CS202", "CHEM101"]
}

print("Student Course Enrollments:")
for student_id, courses in course_enrollments.items():
    print("Student ID:", student_id)
    print("Courses:", courses)
    print()
    
    # Department Courses Dictionary

departments = {
    "Computer Science": [("CS101", "Introduction to Computer Science"),
                         ("CS202", "Data Structures and Algorithms")],
    "Mathematics": [("MATH101", "Calculus I"),
                    ("MATH102", "Calculus II")],
    "Physics": [("PHY101", "General Physics I")]
}

print("Department Courses:")
for department, courses in departments.items():
    print("Department:", department)
    for course in courses:
        print("Course ID:", course[0], "-", course[1])
    print()
    # Lecturer Assignments Dictionary

lecturer_assignments = {
    "Dr. Emily Brown": ["CS101", "MATH102"],
    "Mr. Michael Johnson": ["CS202", "PHY102"],
    "Prof. David Lee": ["PHY101"]
}

print("Lecturer Assignments:")
for lecturer, courses in lecturer_assignments.items():
    print("Lecturer:", lecturer)
    print("Courses:", courses)
    print()