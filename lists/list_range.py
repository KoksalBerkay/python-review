for item in range(1,5):
    print(item)

# list() function makes an empty list.
numbers = list()
print(numbers)

# range function can be used in a list function
numbers = list(range(1,6))
print(numbers)

# we can use step in range. Here, the last parameter is the step.
odd_numbers = list(range(1,11,2))
print(odd_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# Lists are mutable.
squares[3] = 5
print(squares)

# simple statistics
digits = list(range(0,10))
print(digits)

min = min(digits)
max = max(digits)
sum = sum(digits)
print(min, max, sum)
print(digits)