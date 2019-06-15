name=input('Enter your name : ')
def palindrome(string):
    if string==string[-1::-1]:
        print('String is Palindrome ')
    else:
        print('String is not Palindrome ')

palindrome(name)