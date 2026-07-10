n= int (input())
mylist = [int(ele) for ele in input().split()]

for i in range(1, n):
    key = mylist[i]
    j = i - 1
    while j >= 0 and mylist[j] > key:
        mylist[j + 1] = mylist[j]
        j -= 1
    mylist[j + 1] = key
    print(mylist)
    print("------")

print(mylist)