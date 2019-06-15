def reverse_ele(l):
    x=[]
    for i in l:
        x.append(i[::-1])
    return x

n=['abc','def','pqr']
print(reverse_ele(n))