
# Chapter 9 Python Code - Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [5, 1, 4, 2, 8]
bubble_sort(arr)
print(arr)  # Output: [1, 2, 4, 5, 8]
