#defining fib function, fibonacci sequences are the sum of the previous 2 numbers
def fibonacci(i):
    fib = [0,1]
    #while the length of the fib list is shorter than the function arg, add the last and second to last num in list and append the sum to the list, and return for next iteration.
    while len(fib) < i:
        fib.append(fib[-1] + fib[-2])
    return fib
print(fibonacci(10))
