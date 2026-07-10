def mergesort(my_list, left, right):
    if left < right:
        mid = left + (left + right) // 2
        mergesort(my_list, left, mid)
        mergesort(my_list, mid + 1, right)
        merge(my_list, left, mid, right)