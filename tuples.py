courses = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms")
]

new_list = []

for c in courses:
    new_list.append(c[1])

print("Course names:")
for name in new_list:
    print(name)