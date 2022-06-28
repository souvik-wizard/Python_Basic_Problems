from operator import le

def checking(num):
    sum = 0
    temp = num

    array = [int(x) for x in str(num)]
    length = len(array)

    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10

    if num == sum:
        print(num, "is an Armstrong number")
        print("And the cube root of each numbers are given below :")
        a=[]
        for i in range(length):
             a.append(array[i]**length)
        return a
    else:
        return num, 'is not an Armstrong number'
   
   
print(checking(370))

        

