def all_total(*args):
    sum=0
    for num in args:
        sum+=num
    return sum

print(all_total(1,3,5,7,9,11))