#WAP to create a list of 5 odd integers repplacec thew third element with the  list of 4 even inyegers. FLATTEN,SORT AND PRINT THR LIST.
def flatten(lst):
    flat=[]
    for item in lst:
        if isinstance(item,list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat
lst=[3,9,7,5,11]
lst[2]=[2,4,6,8]
print(lst) 
result=flatten(lst)
print(result)
print(sorted(result))
