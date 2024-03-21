import math
from abc import ABC, abstractmethod
#task 1
squares = [x**2 for x in range(1, 11)]
print(squares)


#task 2
def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

#task 3
squares_example = generate_squares(1, 10)
print(squares_example)


class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end + 1)]


square_gen = SquareGenerator()
result = square_gen.generate_squares(1, 5)
print(result)


#task 4
square_roots = [math.sqrt(number) for number in result]
print(square_roots)


#task 5
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to the start.")
        return [x**2 for x in range(start, end + 1)]

square_gen = SquareGenerator()
try:
    result = square_gen.generate_squares(5, 1)
except ValueError as e:
    print(e)



#task 6
#from square_generator import SquareGenerator

square_gen = SquareGenerator()
result = square_gen.generate_squares(1, 5)
print(result)



#task 7

from square_generator.square_generator import SquareGenerator

square_gen = SquareGenerator()
result = square_gen.generate_squares(1, 5)
print(result)

#task 8

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to the start.")
        return [x**3 for x in range(start, end + 1)]


cubic_gen = CubicGenerator()
cubes_result = cubic_gen.generate_squares(1, 5)
print(cubes_result)

# Task 9: Function Overriding already implemented


#Task 10
class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to the start.")
        return [x**3 for x in range(start, end + 1)]


cubic_gen = CubicGenerator()
cubes_result = cubic_gen.generate_squares(1, 5)
print(cubes_result)
