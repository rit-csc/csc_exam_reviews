def fib(n, table=None):
    """Compute the n'th number in the Fibonacci sequence."""
    if table == None:
        table = [0,1]
    if n < len(table):
        return table[n];
    else:
        table.append(fib(n-1,table) + fib(n-2,table))
        return table[n]
