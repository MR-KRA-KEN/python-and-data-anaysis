num1=int(input('Enter first number : '))
num2=int(input('Enter second number : '))
def greatest(a,b):
    if a>b:
        return a
    else:
        return b

print(f'greatest of two number is {greatest(num1,num2)}')