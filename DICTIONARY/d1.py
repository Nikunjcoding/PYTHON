# d={10:'A',20:'A',30:'B'}               # unordered eg.
# print(d)
# e={10:'A',20:'B',10:'A'}
# print(e)
# f={10:'A',20:'B',10:'P'}
# print(f)

#d={1:'nikunj',2:'nitish',3:'uday'}
#print(d[1])
# for k ,v in d.items():                    # looping.
#     print(k,v)
# for k in d.keys():
#     print(k)
# for k in d:
#     print(k)
# for v in d.values():
#     print(v)

# course={1:'cse',2:'python',3:'dsa',4:'ece',5:'mechanics'}         # Enumeration function.
# for index,(k,v) in enumerate(course.items()):
#     print(index,k,v)

# d={'a':12,'b':24,'c':36}                                          # mutabilitty.
# d['d']=48
# print(d)
# del(d['b'])
# print(d)

'''DICTIONARY VERITIES.'''

# contact={                                                       # Nested dictionary.
#     'Anil':{'DOB':'23/5/23','Favourite':'Ice cream'},
#     'Anmol':{'DOB':'12/5/23','Favourite':'Mango'},
#     'Ravi':{'DOB':'14/9/25','Favourite':'Apple'}
# }
# print(contact)
# d={(1,5):'ee101',(1,4):'ece105',(4,1):'ece104'}
# print(d)

# animal={'tiger':141,'lion':142,'leopard':143}                 # Merge by unpacking.
# birds={'eagle':23,'parrot':104,'crow':96}
# combine={**animal,**birds}
# print(combine)

# lst=[12,13,14,15,16]                                          # Fromkey function.
# d=dict.fromkeys(lst,25)
# print(d)

'''WAP to reads a string from the keyboard and creates dictionary containing frequency of each charactor occuring in the string ?'''
# text=input("Enter the string: ")
# dict={}
# for char in sorted(text):
#     dict[char]=text.count(char)
# print(dict)

# student={}
# n=int(input("Enter the number of student: "))
# for i in range(n):
#     name=input("Enter the name :")
#     Maths=int(input("Enter the marks of Maths: "))
#     english=int(input("Enter the marks of English: "))
#     pps=int(input("Enter the marks of pps: "))
#     student[name]={'Maths':Maths,'English':english,'PPS':pps}
# print(student)
# marks={}
# for i in student:
#     val=sum(student[i].values())
#     marks[i]=val
#     for j in student[i]:
#         student[i][j]=val
# print("updatyed student\n",student)
# print(marks)
# print("average of the class is :",sum(marks.values())/len(marks))

# for k,w in marks.items():
#     if w==max(marks.values()):
#         print("topper of the class is :",k)
