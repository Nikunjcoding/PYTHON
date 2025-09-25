''' BASIC OPERATION IN DICTIONARY.'''
# d={'A':10,'B':20,'C':30,'D':40,'E':50}           # conversion.(dict to list/tuple)       
# print(list(d))
# print(tuple(d))
# lst=[10,20,30]                                    # (list/tuple to dict)
# d=dict.fromkeys(lst,10)
# print(d)

# d1={'a':'nikunj','b':'uday','c':'nitish'}         # Aliacing.
# d2=d1
# d1['a']='aditya'
# print(d1,d2)

# d={1:'A',2:'B',3:'C'}                             # coloning.
# d1={}
# d1=d.copy()
# print(d,d1)
# d[1]='nikunj'
# print(d,d1)

# d={'a':11,'b':22,'c':33,'d':44,'e':55}        # searching.
# d1='a' in d
# d2='f' in d
# print(d1,d2)

# d={'A':10,'B':20,'C':30}                      # identity.
# d1={'A':10,'B':20,'C':30}
# d2=d
# print(d is d1)
# print(d is d2)
# print(d1 is not d2)

# d={}                                          # emptiness.
# print(bool(d))

# d={1:'p',2:'q',3:'r'}                         # Add.
# d[4]='n'
# d[5]='m'
# print(d)

# d={'a':10,'b':20,'c':30}                      # Delete.
# del(d['a'])
# print(d)
# del(d)
# print(d)

'''BUILT IN FUNCTION'''
# student={'name':'Nikunj','age':20,'grade':'A'}
# print(len(student))
# print(max(student))
# print(min(student))
# print(any(student))
# print(all(student))
# print(list(reversed(student.items())))
# print(tuple(reversed(student.keys())))
# print(list(reversed(student.values())))

# marks={'eng':49,'phy':89,'che':79}            #sum.
# total=sum(marks.values())
# print(total)

'''METHODS IN DICTIONARY'''
# c={101:'PPS',102:'PYTHON',103:'DSA',104:'OS'}
# d={201:'WORKSHOP',202:'DIGITAL',203:'MECHANIC'}
# print(c.get(101,'absent'))
# print(d.get(204,'hindi'))
# print(c[102])
# c.update(d)
# print(c)
# print(c.popitem())
# print(c)
# d.clear()
# print(d)

