
# Chapter 20 Python Code - Quick Sort (Divide and Conquer)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [38, 27, 43, 3, 9, 82, 10]
print(quick_sort(arr))  # Output: [3, 9, 10, 27, 38, 43, 82]
