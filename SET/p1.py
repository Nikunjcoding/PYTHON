# a=set()                            #Empty set.
# print(a)
# print(bool(a))

# a={10,20,"python",40,50}            # Mutability.
# print(a)
# a.add("CSE")
# print(a)

# s={23,45,67,11,32}                  # for loop in set./while loop is not possible.
# for ele in s:
#     print(s)

# s={10,20,30,50,70}                      # enumeration of sets.
# for index,n in enumerate(s):
#     print(index,n)

# s=frozenset({"nikunj","nitish","ashish","uday","aaditya"})    # immutable set by frozenet()function.
# s.add("nitesh")
# print(s)

# s={90,100,110,104,105,101,10,20,30,150,130,40,117,50,60}        # built-in function.
# print(len(s))
# print(max(s))
# print(min(s))
# print(sorted(s))
# print(sum(s))
# print(any(s))
# print(all(s))

# s={12,15,13,23,22,16,19}                                    #  Basic-Method in set.
# t={'A','B','C'}
# u=set()
# s.add("Hello")
# print(s)
# s.update(t)
# print(s)
# u=s.copy()
# print(u)
# s.remove(13)
# print(s,u)
# s.discard(101)
# print(s)
# s.discard('A')
# print(s)
# s.clear()
# print(s)

# s={15,20,23,32,96,45,39,104,203,14,90}                      #  set.Method
# t={14,45,90,39,104}
# r={21,29,89}
# print(s.issuperset(t))
# print(s.issubset(t))
# print(s.isdisjoint(t))
# print(t.issubset(s))
# print(s.isdisjoint(r))

# engineer={'vijay','sanjay','ajay','suraj','aahana','dipkshakshi','sayana','aanya'}  # Mathematical set operation(1).
# manager={'suraj','dipkshakshi','sayana','rimjhim','varsha'}
# print(engineer|manager)
# print(engineer&manager)
# print(engineer-manager)
# print(engineer^manager)

# s1={2,3,4,78,90,23,14,16,78,90}                       #eg.(2)
# s2={78,45,67,54,63,81,104,105,16,90}
# print(s1|s2)
# print(s1&s2)
# print(s2-s1)
# print(s1^s2)

# s={1,2,3,4,5,{6,7,8},9,10}                            # Set varities.
# print(s) # not possible

# s={1,2,3,4,5} #possible
# print(*s)

 