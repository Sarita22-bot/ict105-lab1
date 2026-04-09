# Variables
a = 15
b = 12

print("Type of a:", type(a))
print("Type of b:", type(b))

# Arithmetic
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Type casting
c = int(a / b)
print("Value of c:", c)
print("Type of c:", type(c))

c = float(c)
print("New value of c:", c)
print("New type of c:", type(c))

# Strings
message = "The result of a divided by b is: "
print(message + str(c))

# Comparison
print("Is a > b?", a > b)
print("Is a == b?", a == b)