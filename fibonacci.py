num=int(input('Enter no. upto which you want to print fibonacci series : '))
i=0
total=0
def fibonacci(x):
    a=0
    b=1
    if x==1:
        print(a)
    elif x==2:
        print(a, b)
    else:
        print(a, b, end=(' '))
        for x in range(x-2):
            c=a+b
            a=b
            b=c
            print(b, end=' ')

fibonacci(num)
