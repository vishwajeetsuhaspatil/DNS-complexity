def abc3(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum = sum + i
    return sum
print(abc3(1000))        