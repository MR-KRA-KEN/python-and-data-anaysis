# name=['abc','def','ghi','jkl']
# for pos,name in enumerate(name):
#     print(f"{pos} ---> {name}")


def func(l,s):
    for pos,name in enumerate(l):
        if name==s:
            return pos
    return -1

name=['a','b','c','d','e']
print(func(name,'f'))