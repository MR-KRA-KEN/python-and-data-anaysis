list=[]
n=1
while n==1:
    n=int(input("Choose any one \n1.Enter no.\n2.Exit \n"))
    if n==1:
        p=int(input(("Enter data : ")))
        list.append(p)
    else:
        break
print(list)
list.sort()
print(list)
    