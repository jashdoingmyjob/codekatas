import re

def add(num):
    if not num:
        return 0
    if "//" in num:
        i = num.find("/")+2
        delimiter = num[i]
    else:
        delimiter = ','
    num = num.replace('\n',delimiter)
    print(num)
    num_list = [int(x) for x in num.split(delimiter) if x.strip().isdigit()]
    sum =0
    for i in num_list:
        sum = sum+i
    return sum
