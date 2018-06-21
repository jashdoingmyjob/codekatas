import re

def add(num):
    if not num:
        return 0
    print(num)
    num_list = [int(x) for x in num.split(',') if x.strip().isdigit()]
    sum =0
    for i in num_list:
        sum = sum+i
    return sum

if __name__ == '__main__':
    numbers = raw_input("\nEnter 1-3 numbers separated by commas.\n")
    print(add(numbers))
