import re

def add(num):
    if not num:
        return 0
    delimiter = ','
    if "//" in num:
        delimiter = num[num.find("/")+2]
    if '-' in num and '-' is not delimiter:
        raise Exception(('No negatives: %s', num))

    num = num.replace('\n',delimiter)
    print(num)
    num_list = [int(x) for x in num.split(delimiter) if x.strip().isdigit()]
    sum =0
    for i in num_list:
        sum = sum+i
    return sum

# def negative_exception(negative_number):
#     exception_string = ("No negatives allowed: %s", negative_number)
#     return exception_string
