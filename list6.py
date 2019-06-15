def sublist(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count

n=[1,2,[1,2,3,4],[5,6,7],[9,8]]
print(sublist(n))