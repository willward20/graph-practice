# In the Fibonacci seqeucne, each element is the sum of the previous two. 

sequence = [0, 1]
length = 20

for ii in range(length - 2):
    # sequence.append(sequence[-1] + sequence[-2])
    sequence.append(sum(sequence[-2:]))

print(sequence)


# Using recursion

sequence = [0, 1]
length = 20

def fibonacci(sequence):
    new_number = sum(sequence[-2:])
    if len(sequence) == length:
        print(sequence)

    else:
        sequence.append(new_number)
        fibonacci(sequence)

fibonacci(sequence)
    