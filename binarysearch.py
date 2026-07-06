mylist = []
target = 0
def binary_search(start, end):
    global mylist
    global target

    if end-start  <= 1:
        if mylist[start] == target:
            return start
        
        if mylist[end] == target:
            return end

        return -1
    middle = (start + end) // 2
    if mylist[middle] > target:
        return binary_search(start , middle)
    return binary_search(middle , end)
n = int(input())
target = int(input())
mylist = [int(x) for x in input().split()]

index = binary_search(0, n-1)
print(index)