# Find the lowest value in an array.
import random

array = [random.randint(1, 100) for _ in range(10)]

lowest = array[0]

for value in array:
    if value < lowest:
        lowest = value

print(f"The lowest value in \n\n\t{array} \n\nis {lowest}.")