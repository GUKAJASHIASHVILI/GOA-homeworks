def remove_dublicates(listn):
    seen = set()
    result = []
    for i in listn:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result

listn = [1,2,3,1,2,3]
print(remove_dublicates(listn))