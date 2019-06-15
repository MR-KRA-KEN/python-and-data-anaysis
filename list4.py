def odd_even(l):
    e=[]
    o=[]
    f=[]
    for i in l:
        if i%2==0:
            e.append(i)
        else:
            o.append(i)
    f.append(e)
    f.append(o)
    return f

n=[1,2,3,4,5,6,7,8,9,10]
print(odd_even(n))