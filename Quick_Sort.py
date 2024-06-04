def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Contoh penggunaan:
arr = [10, 7, 8, 9, 1, 5]
arr = quick_sort(arr)
print("Sorted array is:", arr)
