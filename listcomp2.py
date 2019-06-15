def new(l):
    return [str(i) for i in l if (type(i)==int or type(i)==float)]

print(new([1,2,3,[1,2,3],'ajay',4.2]))