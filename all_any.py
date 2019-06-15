no1=[2,4,6,8,10]
no2=[1,2,4,6,8]

print(all([no%2==0 for no in no1]))
print(all([no%2==0 for no in no2]))
print(any([no%2==0 for no in no1]))
print(any([no%2==0 for no in no2]))

def sum(*args):
    if all([type(data)==int or type(data)==float for data in args]):
        total=0
        for i in args:
            total+=i
        return total
    else:
        return 'Wrong choice '

print(sum(1,2,3,4,5,6,7,8,9,10))
print(sum(1,2,3,4,5,'name',['ajay']))