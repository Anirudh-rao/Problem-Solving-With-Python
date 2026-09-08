
def ArrayRot(arr):
    res = arr[::-1]
    print(f"Original Array:{arr}")
    print(f"Rotation Array:{res}")
    d = 2
    n = len(arr)
    arr.reverse()
    arr[:n-d] = arr[:n-d][::-1]
    arr[n-d:] = arr[n-d:][::-1]
    print(f"Rotation Array:{arr}")

arr = [1, 2, 3, 4, 5, 6, 7, 8]
ArrayRot(arr)