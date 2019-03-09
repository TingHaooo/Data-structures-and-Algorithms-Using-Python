def fib(n, a = 1, b = 1):
    """Return Fibonacci number"""
    # if n < 0 raise error
    if n < 0: raise ValueError
    if n == 1: return b
    return fib(n - 1, a = b, b = a + b)

if __name__ == "__main__":
    print(fib(1))# 1
    print(fib(2))# 2
    print(fib(5))# 8