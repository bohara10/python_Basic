class employee:
    
    language = "python"   # This is class attribute
    salary = 200000


rajan = employee()
rajan.name = "Rajan" # this is a object/instance attribute
print(rajan.name,rajan.language, rajan.salary)

rohan = employee()
rohan.name = "Rohan"
print(rohan.name, rohan.salary,rohan.language)


# Here name is object/instance attribute and salary 
# and language are class attributes that are directly 
# belong to class