import re

def add(num):
    if not num:
        return 0
    delimiter = ','
    negatives =[]
    if "//" in num:
        delimiter = num[num.find("/")+2]
    if '-' in num and '-' is not delimiter:
        #print("first if")
        num_list = num.split(delimiter)
        for i in num_list:
            if '-' in i:
                negatives.append(i)
        raise Exception(('No negatives: %s', negatives))

    num = num.replace('\n',delimiter)
    print(num)
    num_list = [int(x) for x in num.split(delimiter) if x.strip().isdigit()]
    sum =0
    for i in num_list:
        sum = sum+i
    return sum
