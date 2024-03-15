#task 1
squares = [x**2 for x in range(1, 11)]
print(squares)


#task 2
def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

#usage
squares_example = generate_squares(1, 10)
print(squares_example)
