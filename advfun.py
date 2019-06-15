def avg_find(*args):
    average=[]
    for i in zip(*args):
        average.append(sum(i)/len(i))
    return average

avg = lambda *args:[sum(i)/len(i) for i in zip(*args)]

print(avg_find([1,2,3,4],[5,6,7,8],[8,9,10,11]))
print(avg([1,2,3,4],[5,6,7,8],[8,9,10,11]))