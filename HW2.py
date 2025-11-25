from random_tuples import create_random_tuples
#תרגיל ###1
tuples_list = create_random_tuples(5, 3, [int, float, str])

print("הרשימה המקורית:")
for t in tuples_list:
    print(t)

sorted_by_int = sorted(tuples_list, key=lambda x: x[0])
print("\nמיון לפי הרכיב הראשון (int):")
for t in sorted_by_int:
    print(t)

sorted_by_float = sorted(tuples_list, key=lambda x: x[1])
print("\nמיון לפי הרכיב השני (float):")
for t in sorted_by_float:
    print(t)

sorted_by_str = sorted(tuples_list, key=lambda x: x[2])
print("\nמיון לפי הרכיב השלישי (str):")
for t in sorted_by_str:
    print(t)

#תרגיל ###2
#א'
def merge(a, b, key):
    result = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    return result

a = [(1, "x"), (3, "y"), (7, "z")]
b = [(2, "a"), (4, "b"), (8, "c")]

merged = merge(a, b, key=lambda x: x[0])
print(merged)

#ב'
def is_sorted(a, key):
    i = 0
    while i < len(a) - 1:
        if key(a[i]) > key(a[i+1]):
            return False
        i += 1
    return True

#תרגיל ###3
#א'
def merge_sorted_lists( lists, key):
    merged = lists[0]
    i=1
    while i< len(lists):
      merged= merge(merged,lists[i],key) 
      i+=1

    return merged

a = [1, 3, 5]
b = [2, 4, 6]
c = [0, 7, 8]

result = merge_sorted_lists([a, b, c], key=lambda x: x)
print(result)

#תרגיל ###4
#א'
def lomuto_partition(a, key):
    pivot = a[-1]       
    i = -1               

    for j in range(len(a)-1):
        if key(a[j]) <= key(pivot):
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i+1], a[-1] = a[-1], a[i+1]
    return i+1

arr = [3, 2, 6, 1, 5]
index = lomuto_partition(arr, key=lambda x: x)
print("Pivot index:", index)
print("Array after partition:", arr)

#ב'
def hoare_partition(a, key):
    pivot = a[0]        
    i = 0             
    j = len(a) - 1    

    while True:
        while key(a[i]) < key(pivot):
            i += 1

        while key(a[j]) > key(pivot):
            j -= 1

        if i >= j:
            return j  

        a[i], a[j] = a[j], a[i]

        i += 1
        j -= 1

arr = [8, 3, 7, 1, 5, 6, 2, 4]
index = hoare_partition(arr, key=lambda x: x)
print("Partition index:", index)
print("Array after partition:", arr)

#תרגיל 5
def two_pivot_partition(a, key):
    if len(a) < 2:
        return a  

    pivot1 = a[0]
    pivot2 = a[-1]

    if key(pivot1) > key(pivot2):
        pivot1, pivot2 = pivot2, pivot1

    left, middle, right = [], [], []

    for x in a:
        if key(x) < key(pivot1):
            left.append(x)
        elif key(x) > key(pivot2):
            right.append(x)
        else:
            middle.append(x)

    return left + middle + right

arr = [4, 3, 7, 1, 5, 6, 2,10, 8, 9]
result = two_pivot_partition(arr, key=lambda x: x)
print(result)
