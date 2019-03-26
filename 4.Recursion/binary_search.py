arr = [1, 2, 4, 7, 8, 12, 15, 17, 20]

def binary_search(S, target, low, high):
    if low > high: return -1
    mid = (high + low) // 2
    if S[mid] == target: return mid
    elif S[mid] < target: return binary_search(S, target, mid + 1, high)
    else: return binary_search(S, target, low, mid - 1)

if __name__ == "__main__":
    print(binary_search(arr, 20, 0, len(arr))) # 8
    print(binary_search(arr, 7, 0, len(arr))) # 3
    print(binary_search(arr, 5, 0, len(arr))) # -1