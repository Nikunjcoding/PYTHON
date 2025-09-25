# a list contain tuples containing roll n. ,names,and ages of students.write a program to gather all names from the list into another list.
lst=[("nikunj",26,22),("nitish",17,22),("uday",52,21)]
a=[]
for i in lst:
    a.append(i[0])
print(a)
    