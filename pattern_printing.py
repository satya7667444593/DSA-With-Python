n = int(input("row:"))

# m = int(input("colmn:"))

# for row in range(n):
#     for num in range(m):
#          print(num+1 , end=" ")
    
#     print("")


# n = int (input("n="))

# for row in range (n):
#     for colmn in range(n):
#         if colmn <= row:
#             print(colmn+1 , end ="")

#         else:
#             break
#             # print("" , end="")
#     print("")            

# for row in range(n):
#     print("* " * (row + 1))

# else:
#     for row in range(n-1,0,-1):
#         print("* " * row)    

for row in range(n):
    for colmn in range(n):
        if colmn <= row:
           
            print("* " * (colmn + 1))
        else:
            print("" )
print("")