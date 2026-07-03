mydict = {"student1": 47 , "student2": 48, "student3": 49}
# print(mydict)
# print(mydict["student1"])
# for key in mydict:
#     print(key, mydict[key])
# for value in mydict.values():
#     print(value)    
print(mydict.get("student5")) #it can't show any error 
print(mydict["student1"]) #it's show error because student5 is not present in the dictionary