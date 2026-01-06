# F(n) = F(n−1) + F(n−2)

def fibonacci(sequence, n):

    # Run the algorithm until the n-th element is found.
    while len(sequence) < n:

        # Append the next element to the sequence
        sequence.append(sum(sequence[-2:]))

        # Continue the algorithm
        fibonacci(sequence, n)

    return sequence[-1]

def F(n):
    if n == 1:
        return 0
    if n == 2: 
        return 1
    else:
        return F(n-1) + F(n-2)


# Initialize the Fibonacci sequence.
sequence = [0, 1]

n = 9
nth = fibonacci(sequence, n)
print(f"The {n}-th element is {nth}")
print(f"The {n}-th element is {F(n)}")

