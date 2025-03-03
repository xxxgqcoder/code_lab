def insert_sort(a):
    for j in range(1, len(a)):
        # assume a[0, ..., j-1] is sorted
        key = a[j] # make a hole at a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            # initial case: a[j-1] > a[j], move hole one step left
            a[i+1]  = a[i]
            i = i - 1
        # termination:
        # i >= 0, a[i] < key, i+1 is the place for key (hole)
        # i < 0, all values checked, i = 0 is the place for key (hole)
        a[i+1] = key
