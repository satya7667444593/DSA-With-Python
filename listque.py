# n = int(input())
# list = input().split()
# for i in range(n):
#     list[i] = int(list[i]) 

# print(sum(list))

# print("hellow world")
# Mode of list
# n = int(input('no:'))

# list = input().split()
# sum = 0 
# for var in list:
#     sum += int(var)

# print(sum)    
# print(sum / len(list))

n = int(input('no:'))

list = input().split()

for i in range(n):
    list[i] = int(list[i])

    
list.sort()

if n%2 ==1:
    print(list[n//2])
else:
    e1 = list[n//2 - 1]   
    e2 = list[n//2]
    print((e1+e2)/2)

print(list)    