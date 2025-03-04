def insert_sort(a):
    for j in range(1, len(a)):
        # assume a[0, ..., j-1] is sorted
        key = a[j]  # make a hole at a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            # initial case: a[j-1] > a[j], move hole one step left
            a[i + 1] = a[i]
            i = i - 1
        # termination:
        # i >= 0, a[i] < key, i+1 is the place for key (hole)
        # i < 0, all values checked, i = 0 is the place for key (hole)
        a[i + 1] = key


def median3(a, left, right):
    center = (left + right) // 2
    if a[center] < a[left]:
        a[left], a[center] = a[center], a[left]
    if a[right] < a[left]:
        a[right], a[left] = a[left], a[right]
    if a[right] < a[center]:
        a[right], a[center] = a[center], a[right]
    a[center], a[right - 1] = a[right - 1], a[center]
    return a[right - 1]


def quick_sort(a, left, right):
    if len(a) <= 1 or left >= right:
        return
    pivot = median3(a, left, right)
    if right - left <= 2:
        return

    i, j = left, right - 1
    while i < j:
        while a[i] <= pivot and i < right - 1:
            i += 1
        while a[j] >= pivot and j > left:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[i], a[right - 1] = a[right - 1], a[i]
    quick_sort(a, left, i - 1)
    quick_sort(a, i + 1, right)


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quick_sort_v2(a, left, right):
    if len(a) <= 1 or left >= right:
        return

    p = partition(a, left, right)
    quick_sort_v2(a, left, p - 1)
    quick_sort_v2(a, p + 1, right)
