# numbers = [1, 2, 3, 4]


# # Define the function to square a number
# def square(x):
#     return x**2


# # Apply to every item in the list
# result = map(square, numbers)

# # Convert to a list and print
# print(list(result))  # Output: [1, 4, 9, 16]


# numbers = [1, 2, 3, 4]


# def name(x):
#     return x**2


# lambda x: x**2

# result = list(map(lambda x: x**2, numbers))
# print(result)  # Output: [1, 4, 9, 16]


words = ["hello", "world", "python"]

# Convert each word to uppercase
uppercase_words = list(map(str.upper, words))

# print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

print(enumerate(words))
