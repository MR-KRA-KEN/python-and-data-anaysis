winning_number =55
number=int(input('Enter any number : '))
if number==winning_number:
    print('You WON ')
else:
    if number<winning_number:
        print('No. is to low ')
    else:
        print('No. is to high ')
