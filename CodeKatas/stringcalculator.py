import re

def add(num):
    if not num:
        return 0
    num = num.replace('\n',',')
    print(num)
    num_list = [int(x) for x in num.split(',') if x.strip().isdigit()]
    sum =0
    for i in num_list:
        sum = sum+i
    return sum
