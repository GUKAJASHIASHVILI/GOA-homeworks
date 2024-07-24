def devide(num):
    if num %5 == 0 and num %3 ==0:
        print("Your number can be devided by 5 and 3")
    elif num %3 == 0:
        print("Your number can be devided by 3")
    elif num %5 == 0:
        print("Your number can be devided by 5")
    else: print("Your number can not be devided by 5 or 3")


        

devide(17)