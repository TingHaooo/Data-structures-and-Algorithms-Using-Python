def my_reverse (s, start, end):
    """Reverse elements in implict slice s[start:stop]"""
    if start < end - 1:
        s[start], s[end - 1] = s[end - 1], s[start]
        my_reverse(s, start + 1, end - 1)


if __name__ == "__main__":
    arr = list(range(0, 100))
    my_reverse(arr, 0, len(arr))
    print(arr)