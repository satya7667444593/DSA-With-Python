n = int(input())
m = int(input())
matrix = []
for i in range(n):
    row = [int(item)for item in input().split()]
    matrix.append(row)
print(matrix)
