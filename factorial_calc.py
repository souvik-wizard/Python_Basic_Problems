def factorial(num):
    count=1
    for i in range(1,num+1):
        count*=i
    return count
print(factorial(5))