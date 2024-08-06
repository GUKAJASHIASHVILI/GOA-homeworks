def avrage(listn):
    sum_numbers = sum(listn)
    len_numbers = len(listn)

    total = sum_numbers/len_numbers
    return total

print(avrage([10,6,10,7,10,9,10,10]))