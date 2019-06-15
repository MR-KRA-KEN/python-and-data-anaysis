import random
winning_no= random.randint(1,100)
for i in range(1,100):
    n=int(input('Enter an number : '))
    if n==winning_no:
        print('You won the game ')
        print(f'Take {i} turns ')
        break
    elif n<winning_no:
        print('To less ')
    else:
        print('to high')