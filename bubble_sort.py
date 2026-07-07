n = int(input())
mylist = [int(x) for x in input().split()]
for i in range(n-1):
    for j in range(n-i-1):
        if mylist[j] > mylist[j+1]:
            temp = mylist[j]
            mylist[j] = mylist[j+1]
            mylist[j+1] = temp
print(mylist)