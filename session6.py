# User Input Loop

students = []

while True:
    name = input("Enter student name (or type exit): ")

    if name.lower() == "exit":
        break

    students.append(name)
    print(name, "has been added to the class.")

print("Student List:")
for student in students:
    print(student)
    
    # Room Capacity Finder

rooms = {
    "Room 101": {"capacity": 15, "floor": "Ground Floor", "location": "Building A"},
    "Room 103": {"capacity": 20, "floor": "Ground Floor", "location": "Building A"},
    "Room 105": {"capacity": 25, "floor": "Ground Floor", "location": "Building A"},
    "Room 107": {"capacity": 30, "floor": "Ground Floor", "location": "Building A"}
}

students_needed = int(input("Enter number of students: "))

for room, details in rooms.items():
    if details["capacity"] >= students_needed:
        print("Suitable Room:", room)
        print("Capacity:", details["capacity"])
        print("Floor:", details["floor"])
        print("Location:", details["location"])
        break