
def quick_sort(mylist , low, high):
   if low < high:
       pi = partition(mylist, low, high)
       quick_sort(mylist, low, pi - 1)
       quick_sort(mylist, pi + 1, high)
def partition(mylist, low, high):
   pivot = mylist[high]
   i = low - 1
   for j in range(low, high):
       if mylist[j] <= pivot:
           i += 1
           mylist[i], mylist[j] = mylist[j], mylist[i]
   mylist[i + 1], mylist[high] = mylist[high], mylist[i + 1]
   return i + 1 
n = int(input())
mylist = [int(ele) for ele in input().split()]      
quick_sort(mylist, 0, n - 1)
print(mylist)