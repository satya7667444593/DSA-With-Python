def dnfAlgorithm(num):
    n = len(num)
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if num[mid] == 0:
            num[low], num[mid] = num[mid], num[low]
            low += 1
            mid += 1
        elif num[mid] == 1:
            mid += 1
        else:  # num[mid] == 2
            num[mid], num[high] = num[high], num[mid]
            high -= 1
    return num
num = [0, 1, 2, 0, 1, 2]
print(dnfAlgorithm(num)) 