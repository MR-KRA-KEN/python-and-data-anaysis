def exp(num,*args):
    if args:
        return [i**num  for i in args]
    else:
        print("Pass some value")

l=[1,2,3,4,5,6,7]
print(exp(3,*l))