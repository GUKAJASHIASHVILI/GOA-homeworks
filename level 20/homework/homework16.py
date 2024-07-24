def average(listn):
    sum = 0
    length_of_list = len(listn)
    for i in listn:
        sum += i
    
    average_num = sum / length_of_list
    print(average_num)




average(listn=[10,20,30,40,50])