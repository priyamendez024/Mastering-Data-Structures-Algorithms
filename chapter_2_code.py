
# Chapter 2 Python Code - Array Rotation
arr = [1, 2, 3, 4]
print(arr[2])

def rotate(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5, 6]
print(rotate(arr, 2))
