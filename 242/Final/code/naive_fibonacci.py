def fib(n):
    """Compute the n'th number in the Fibonacci sequence."""
    if n in (0,1):
        return n
    else:
        return fib(n-1) + fib(n-2)
