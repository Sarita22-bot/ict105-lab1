departments = [
    (1, "Computer Science"),
    (2, "Mathematics"),
    (3, "Computer Science"),
    (4, "Mathematics"),
    (5, "Physics")
]

while True:
    user = input("Enter course ID (1-5) or 0 to quit: ")

    if user == "0":
        print("Exit")
        break

    if not user.isdigit():
        print("Invalid input")
        continue

    user = int(user)
    found = False

    for d in departments:
        if d[0] == user:
            print(f"Course ID {user} is in {d[1]} department")
            found = True
            break

    if not found:
        print("Course not found")