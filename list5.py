def common(l,m):
    x=[]
    for i in l:
        for j in m:
            if j==i:
                x.append(j)
    return x

n=[1,2,3,4,5]
m=[1,2,6,7]
print(common(n,m))