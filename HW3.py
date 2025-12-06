#Q3
def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2


#Q4
def is_max_heap(arr, i=0, key=lambda x: x):
    n = len(arr)
    for child in range(i + 1, n):
        parent = (child - 1) // 2
        if key(arr[parent]) < key(arr[child]):
            return False

    return True


#Q5
def max_heapify(arr, i, heap_size, key=lambda x: x):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and key(arr[left]) > key(arr[largest]):
        largest = left
    if right < heap_size and key(arr[right]) > key(arr[largest]):
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size, key)

arr = [4, 5, 8, 3, 4, 9, 2]
max_heapify(arr, 0, len(arr))
print(arr)


#Q6
def build_max_heap(arr, key=lambda x: x):
    for i in range(len(arr)//2 - 1, -1, -1): max_heapify(arr, i, len(arr), key)
    return arr

arr = [3, 1, 6, 5, 2, 4]
build_max_heap(arr)
print(arr)


#Q7
def heap_sort(arr, key=lambda x: x):
    build_max_heap(arr, key)
    heap_size = len(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, 0, heap_size, key)
    return arr

arr = [3, 1, 6, 5, 2, 4]
heap_sort(arr)
print(arr)