# q2
from xml.dom.minidom import Node


def quick_kth(arr, left, right, k, key=lambda x: x):
    if left == right:
        return arr[left]

    pivot_index = partition(arr, left, right, key)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_kth(arr, left, pivot_index - 1, k, key)
    else:
        return quick_kth(arr, pivot_index + 1, right, k, key)


def partition(arr, left, right, key):
    pivot = arr[right]
    pivot_value = key(pivot)
    i = left

    for j in range(left, right):
        if key(arr[j]) <= pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i

arr = [7, 2, 1, 6, 8, 5, 3, 4]
print(quick_kth(arr, 0, len(arr) - 1, 3))  # האיבר ה־4 בגודלו

# q4 ו- q5 בדף השני