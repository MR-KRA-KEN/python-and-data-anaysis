number = list(range(1,11))
print(number)
def square(num):
    temp=[]
    for i in num:
        x=i**2
        temp.append(x)
    return temp

print(square(number))