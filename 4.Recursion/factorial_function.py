def factorial (n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    print("0 factorial equal {ans}".format(ans=factorial(0)))
    print("5 factorial equal {ans}".format(ans=factorial(5)))
    print("10 factorial equal {ans}".format(ans=factorial(5)))