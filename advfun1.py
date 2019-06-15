name=['Nishchal','Bhuria','harshit']
print(max(name , key= lambda item:len(item)))
print(min(name , key= lambda item:len(item)))

x=[
    {'name':'nishchal','score':79,'age':21},
    {'name':'Bhuria','score':75,'age':24},
    {'name':'Harshit','score':89,'age':22}
]

print(max(x,key=lambda item:item.get('score'))['name'])