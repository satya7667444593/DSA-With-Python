# myvar = 3
# def fun():
#     myvar = 5
#     print(myvar)
# fun()    
# print(myvar)

# myvar = 4

# def fun():
#     myvar += 1
#     print(myvar)
# fun()    

myvar = 4

def fun():
    global myvar
    myvar += 1
    print(myvar)
fun()    