n=int(input("Enter a no. "))
mul=1
for i in range(1,n):
    mul*=n
    n-=1
print(f"factorial is {mul}")