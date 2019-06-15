n=input('Enter any two digit no. : ')
i=0
total=0
while i<len(n):
    total+=int(n[i])
    i=i+1
print(f'sum is {total}')