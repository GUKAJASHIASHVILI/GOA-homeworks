def manual_find(text,str_to_find):
    for index,element in enumerate(text):
        if element == str_to_find:
            return index


txt = [20,60,100,200,600,1,5]
print(manual_find(txt,600))