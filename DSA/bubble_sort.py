# Sort an array from lowest to highest using a bubble sort. 
import random

array = [random.randint(1, 100) for _ in range(10)]
print(array)


# Loop through the array
for idx, value in enumerate(array):

    # For each preceding element...
    for ii in range(idx-1, -1, -1):

        # If the precding is higher, swap
        if value > array[ii]:
            highest = array.pop(ii+1)
            array.insert(ii, highest)
        else:
            break

print(array)