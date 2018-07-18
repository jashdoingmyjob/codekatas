
#add
#INPUTS: num = string passed in
#OUTPUTS: sum of the numbers inputed if no exception raised. Or returns 0 if empty string
#FUNCTIONALITY: adds numbers passed in as a string by user
def add(num):
    if not num:
        return 0
    delimiter = ','
    if "//" in num:
        delimiter = num[num.find("/")+2]
    _check_negatives_exist(num, delimiter)
    num = num.replace('\n',delimiter)
    num_list = [int(x) for x in num.split(delimiter) if x.strip().isdigit()]
    sum =0
    for i in num_list:
        if i > 1000:
            i =0
        sum = sum+i
    return sum


#check_negatives_exist
#INPUTS: number = string passed in,   delim = delimiter set
#OUTPUTS: if contains negative numbers then raise exception. else return nothing
#FUNCTIONALITY: Helper function that checks if user inputted negative numbers.
def _check_negatives_exist(number, delim):
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

#only use if want to manually test
if __name__ == '__main__':
    input = raw_input("\nEnter numbers to add\n")
    print(add(input))
