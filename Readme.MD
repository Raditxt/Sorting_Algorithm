# Algoritma Pengurutan (Sorting Algorithms)

## Pendahuluan
Algoritma pengurutan adalah teknik untuk mengatur elemen-elemen dalam suatu koleksi (seperti array) ke dalam urutan tertentu. Urutan ini bisa berupa urutan menaik (ascending) atau menurun (descending). Di bawah ini adalah implementasi dari beberapa algoritma pengurutan yang umum digunakan dalam Python, beserta contoh output untuk setiap algoritma.

## Implementasi Algoritma Pengurutan

### 1. Bubble Sort
Algoritma ini bekerja dengan membandingkan setiap pasangan elemen yang berdekatan dan menukarnya jika berada dalam urutan yang salah. Proses ini diulangi sampai tidak ada lagi elemen yang perlu ditukar.
- Kompleksitas waktu: O(n^2)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
```
- Output
```Output
  Sorted array is: [11, 12, 22, 25, 34, 64, 90]
```
### 2. Selection Sort
Algoritma ini bekerja dengan menemukan elemen terkecil dari array dan menukarnya dengan elemen pertama, kemudian mengulangi proses ini untuk elemen kedua, dan seterusnya.
Kompleksitas waktu: O(n^2)
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Contoh penggunaan
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)
```
- Output
```Output
    Sorted array is: [11, 12, 22, 25, 64]
```
### 3.Insertion Sort
Algoritma ini bekerja dengan cara membangun urutan akhir satu elemen pada satu waktu, dengan secara berulang-ulang mengambil elemen berikutnya dari input dan menempatkannya di posisi yang benar.
- Kompleksitas waktu: O(n^2)
```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Contoh penggunaan
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array is:", arr)
```

- Output
```Output
Sorted array is: [5, 6, 11, 12, 13]
```
### 4. Merge Sort
Algoritma ini menggunakan pendekatan "divide and conquer" dengan membagi array menjadi dua bagian, mengurutkan masing-masing bagian, dan kemudian menggabungkannya kembali.

- Kompleksitas waktu: O(n log n)
```python
  def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
# Contoh penggunaan
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array is:", arr)
```
- Output
 ```Output
    Sorted array is: [5, 6, 7, 11, 12, 13]
```
### 5. Quick Sort
Algoritma ini juga menggunakan pendekatan "divide and conquer" dengan memilih sebuah elemen sebagai pivot, mempartisi array sehingga semua elemen yang lebih kecil dari pivot berada di sebelah kiri dan semua elemen yang lebih besar berada di sebelah kanan, kemudian mengurutkan kedua bagian tersebut secara rekursif.

- Kompleksitas waktu rata-rata: O(n log n), kompleksitas waktu terburuk: O(n^2)
```python
  def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Contoh penggunaan
arr = [10, 7, 8, 9, 1, 5]
arr = quick_sort(arr)
print("Sorted array is:", arr)
```
- Output
```Output
  Sorted array is: [1, 5, 7, 8, 9, 10]
```
### 6. Heap Sort
Algoritma ini mengubah array menjadi struktur data heap, kemudian berulang kali mengambil elemen terbesar dari heap dan menempatkannya di posisi akhir dari array yang belum diurutkan.

- Kompleksitas waktu: O(n log n)
```python
  def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Contoh penggunaan
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array is:", arr)

- Output
``` Output
Sorted array is: [5, 6, 7, 11, 12, 13]
```
### Kesimpulan
Setiap algoritma pengurutan memiliki kelebihan dan kekurangan, tergantung pada kasus penggunaan tertentu:

- Bubble Sort: Sederhana tapi tidak efisien untuk array besar.
- Selection Sort: Mudah diimplementasikan tetapi tidak efisien untuk array besar.
- Insertion Sort: Efisien untuk array kecil atau hampir terurut.
- Merge Sort: Efisien dan stabil dengan kompleksitas waktu O(n log n).
- Quick Sort: Cepat dan efisien dengan rata-rata kompleksitas waktu O(n log n), tetapi memiliki kompleksitas waktu terburuk O(n^2).
- Heap Sort: Efisien dengan kompleksitas waktu O(n log n), tetapi tidak stabil.
- Anda dapat memilih algoritma pengurutan yang paling sesuai dengan kebutuhan dan karakteristik data Anda.





