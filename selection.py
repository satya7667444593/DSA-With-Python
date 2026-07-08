n = int(input())
mylist = [int(x) for x in input().split()]
for i in range(n):
    min_index = i
    for j in range(i, n):
        if mylist[j] < mylist[min_index]:
            min_index = j
    temp = mylist[min_index]
    mylist[min_index] = mylist[i]
    mylist[i] = temp
print(mylist)