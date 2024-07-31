def manual_max(listn):
     
    minimal_value = listn[0]
    
    for i in listn:
        if i > minimal_value:
            minimal_value = i
    
    return minimal_value

listn = [ 10,2002,30 ,2,50,100]
print(manual_max(listn))