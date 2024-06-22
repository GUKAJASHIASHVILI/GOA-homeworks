num = 0
sum = 0 
for num in range(1,1001):
    sum += num
    num += 1
    if sum in range(500,600):
        continue
    print(sum)