import re

def add(num):
    if not num:
        return 0
    delimiter = ','
    if "//" in num:
        delimiter = num[num.find("/")+2]
    check_negatives_exist(num, delimiter)
    num = num.replace('\n',delimiter)
    num_list = [int(x) for x in num.split(delimiter) if x.strip().isdigit()]
    sum =0
    for i in num_list:
        sum = sum+i
    return sum


def check_negatives_exist(number, delim):
    if '-' in number and '-' is not delim:
        #print("first if")
        num_list = number.split(delim)
        negatives =[]
        for i in num_list:
            if '-' in i:
                negatives.append(i)
        neg_exception = Exception(('No negatives: {}'.format(negatives)))
        print(neg_exception)
        raise neg_exception
    else:
        return

if __name__ == '__main__':
    input = raw_input("\nEnter numbers to add\n")
    print(add(input))
