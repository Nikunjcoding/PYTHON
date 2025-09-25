#variable lenth positional arguments.
def add_number(*args):
    total=0
    for num in args:
        total += num
    return total
print(add_number(5,6,4,7,7,90))