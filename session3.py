courses = [
    "Physics I",
    "Introduction to Programming",
    "Biology I",
    "Calculus I",
    "History I"
]

print("Original list:")
print(courses)

print("\nSorted list (A-Z):")
print(sorted(courses))

print("\nSorted list (Z-A):")
print(sorted(courses, reverse=True))

courses.reverse()
print("\nReversed list:")
print(courses)

courses.reverse()
print("\nOriginal again:")
print(courses)

courses.sort()
print("\nSorted list:")
print(courses)

courses.sort(reverse=True)
print("\nReverse sorted list:")
print(courses)