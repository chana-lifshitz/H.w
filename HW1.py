import random
import string

#תרגיל 4
def min_find(a, key):
    if not a:
        return None, None

    min_item = a[0]
    max_item = a[0]

    for item in a[1:]:
        if key(item) < key(min_item):
            min_item = item
        if key(item) > key(max_item):
            max_item = item

    return min_item, max_item


def create_random_tuples(num, size, types):
    res = []
    for _ in range(num):
        tup = []
        for t in types:
            if t is int:
                tup.append(random.randint(0, 1000))
            elif t is float:
                tup.append(random.uniform(0, 1000))
            elif t is str:
                tup.append(''.join(random.choices(string.ascii_letters + string.digits, k=5)))
        res.append(tuple(tup))
    return res


arr = create_random_tuples(100, 3, [int, float, str])


min_item, max_item = min_find(arr, key=lambda x: x[2])

print("min =", min_item)
print("max =", max_item)

##תרגיל 5

# פונקציה שמממשת Insertion Sort עם מפתח key
def sort_insertion(a, key=lambda x: x):
    for i in range(1, len(a)):
        current = a[i]
        j = i - 1
        while j >= 0 and key(a[j]) > key(current):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = current
    return a

# פונקציה ליצירת רשימת tuples אקראיים
def create_random_tuples(n, size):
    tuples_list = []
    for _ in range(n):
        t = tuple(random.randint(1, 100) if i % 2 == 0 else random.random() for i in range(size))
        tuples_list.append(t)
    return tuples_list

# קטע main
if __name__ == "__main__":
    # יצירת 3 רשימות שונות של tuples בגודל 3
    list1 = create_random_tuples(5, 3)
    list2 = create_random_tuples(5, 3)
    list3 = create_random_tuples(5, 3)

    print("Original lists:")
    print("List1:", list1)
    print("List2:", list2)
    print("List3:", list3)

    # מיון לפי הפריט הראשון של כל tuple
    sorted_list1 = sort_insertion(list1, key=lambda x: x[0])
    # מיון לפי הפריט השני של כל tuple
    sorted_list2 = sort_insertion(list2, key=lambda x: x[1])
    # מיון לפי הפריט השלישי של כל tuple
    sorted_list3 = sort_insertion(list3, key=lambda x: x[2])

    print("\nSorted lists:")
    print("List1 sorted by first element:", sorted_list1)
    print("List2 sorted by second element:", sorted_list2)
    print("List3 sorted by third element:", sorted_list3)
